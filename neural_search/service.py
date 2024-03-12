import json
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config import COLLECTION_NAME, STATIC_DIR
from neural_search.llm_chain import generate_chain, generate_summary_chain
from neural_search.neural_searcher import NeuralSearcher

from fastapi.middleware.cors import CORSMiddleware



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
    for context in contexts:
        context.pop('tickers', None)
        print('context', context)
    print(contexts[0])
    res = summary_chain.invoke({'context':contexts,'search_query':search_query,'ticker':ticker})
    print(f'summary {res}')
    return res



@app.get("/api/search")
async def read_item(ticker: str,keyword:str, neural: bool = True):
    print('invoking chain')
    res = chain.invoke({"keyword": keyword})
    print(res)
    if res and type(res) == dict:
        keywords = res["keywords"]
    else:
        res = json.loads(res)
        keywords = res["keywords"]
    print(keywords)
    keywords.insert(0,keyword)
    search_term = ','.join(keywords)
    print(search_term)
    search_result = neural_searcher.search(text=search_term,ticker = ticker)
    summary = get_summary(search_result,search_term,ticker)
    return {
        'summary':summary,
        "search_result": search_result,
        'keywords': res
    }

#
# # Mount the static files directory once the search endpoint is defined
# if os.path.exists(STATIC_DIR):
#     app.mount("/", StaticFiles(directory=STATIC_DIR, html=True))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
    # res = neural_searcher.search('vedanta limited , vedanta holdings')
    # for item in res:
    #     item.pop('tickers')
    #     #check if the ticker is there
    #     print(item)
