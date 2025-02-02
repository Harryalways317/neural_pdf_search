import json
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config import COLLECTION_NAME, STATIC_DIR
from neural_search.llm_chain import generate_chain, generate_summary_chain
from neural_search.neural_searcher import NeuralSearcher

from fastapi.middleware.cors import CORSMiddleware


from diskcache import Cache

# Cache directory
cache_dir = "../cache"
cache = Cache(cache_dir)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    yield
    # Clean up the ML models and release the resources

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

neural_searcher = NeuralSearcher(collection_name=COLLECTION_NAME)
chain = generate_chain()
summary_chain = generate_summary_chain()


def get_summary(contexts, search_query, ticker):
    cache_key = f"summary-{ticker}-{search_query}"

    # Result from the cache
    cached_result = cache.get(cache_key)
    if cached_result:
        print("Returning cached result")
        return cached_result
    for context in contexts:
        context.pop('tickers', None)
        print('context', context)
    print(contexts[0])
    res = summary_chain.invoke({'context':contexts,'search_query':search_query,'ticker':ticker})
    print(f'summary {res}')
    print(type(res))
    if type(res) == dict:
        cache.set(cache_key, res.get('content',''))
        return res.get('content','')
    else:
        res = json.loads(res)
        cache.set(cache_key, res.get('content', ''))
        return res.get('content','')

def get_similar_keywords(keyword):
    cache_key = f"keywords-{keyword}"

    # Result from the cache
    cached_keywords = cache.get(cache_key)
    if cached_keywords:
        print("Returning cached keywords")
        return cached_keywords
    res = chain.invoke({"keyword": keyword})
    print(res)
    if res and type(res) == dict:
        keywords = res["keywords"]
    else:
        res = json.loads(res)
        keywords = res["keywords"]
    print(keywords)
    keywords.insert(0, keyword)
    cache.set(cache_key, keywords)
    return keywords



@app.get("/api/search")
async def read_item(ticker: str,keyword:str, neural: bool = True):
    print('invoking chain')

    keywords = get_similar_keywords(keyword)
    print(f'keywords {keywords}')
    search_term = ','.join(keywords)
    print(f'search_term {search_term}')
    search_result = neural_searcher.search(text=search_term,ticker = ticker)
    summary = get_summary(search_result,search_term,ticker)
    return {
        'summary':summary,
        "search_result": search_result,
        'keywords': keywords
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
    # res = neural_searcher.search('vedanta limited , vedanta holdings')
    # for item in res:
    #     item.pop('tickers')
    #     #check if the ticker is there
    #     print(item)
