import glob
import json
import os
from collections import Counter

import fitz #pymupdf
from joblib import dump, load


import spacy

# python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_lg")



def find_companies(text):
    doc = nlp(text)
    print(f'DOC {doc}')
    companies = set([ent.text for ent in doc.ents if ent.label_ in ['ORG']])
    print(f'companies: {companies}')
    return list(companies)



def get_top_tickers_for_chunk(text, top_n=10):
    tickers = find_companies(text)
    ticker_frequency = Counter(tickers)
    top_n_tickers = [ticker for ticker, _ in ticker_frequency.most_common(top_n)]
    print(f'topn tickers: {top_n_tickers}')
    return top_n_tickers


def pdf_to_text(path, start_page=1, end_page=None):
    doc = fitz.open(path)
    total_pages = doc.page_count
    print(f'Total pages: {total_pages}')

    if end_page is None:
        end_page = total_pages

    text_list = []

    for i in range(start_page - 1, end_page):
        text = doc.load_page(i).get_text("text")
        text = preprocess(text)
        text_list.append(text)

    doc.close()
    return text_list


def text_to_chunks(texts, word_length=150, start_page=1, pdf_name="", top_n=10):
    text_toks = [t.split(' ') for t in texts]
    chunks = []

    # global_tickers = set()  # To collect tickers from the entire document

    # for page_number, text in enumerate(texts):
    #     page_tickers = find_companies(text)
    #     global_tickers.update(page_tickers)
    # print(f'global tickers: {global_tickers}')

    for idx, words in enumerate(text_toks):
        for i in range(0, len(words), word_length):
            chunk = words[i:i + word_length]
            if (i + word_length) > len(words) and (len(chunk) < word_length) and (len(text_toks) != (idx + 1)):
                text_toks[idx + 1] = chunk + text_toks[idx + 1]
                continue
            chunk = ' '.join(chunk).strip()
            # Include PDF name along with the page number in the chunk
            # chunk = f'[PDF: {os.path.basename(pdf_name)}] [Page no. {idx + start_page}] ' + chunk
            # chunks.append(chunk)
            chunk_data = {
                "text": chunk,
                "tickers": get_top_tickers_for_chunk(chunk, top_n=top_n),  # Convert to list if needed
                "pdf_name": os.path.basename(pdf_name),
                "page_number": idx + start_page
            }
            chunks.append(chunk_data)
    return chunks


def preprocess():
    pdf_dir = '../data/pdfs'
    pdf_files = glob.glob(os.path.join(pdf_dir, '*.pdf'))
    print(f'total of length {len(pdf_files)}')
    chunks_cache_path = '../neural_search/chunks_cache.joblib'
    model_cache_path = 'model_cache.joblib'

    all_chunks = []

    # Check if cache exists
    if os.path.exists(chunks_cache_path):
        print("Loading chunks from cache...")
        all_chunks = load(chunks_cache_path)
    else:
        all_chunks = []
        # Process each pdf file
        idx = 0
        for pdf_path in pdf_files:
            idx += 1
            print(f"Processing {idx} {pdf_path}...")
            texts = pdf_to_text(pdf_path)
            chunks = text_to_chunks(texts, start_page=1, pdf_name=pdf_path)
            all_chunks.extend(chunks)
        # Save processed chunks to disk
        dump(all_chunks, chunks_cache_path)

    print(f"Total Chunks: {len(all_chunks)}")

    # save chunks to a json file
    chunks = load(chunks_cache_path)
    print(f"Total Chunks: {len(chunks)}")
    with open('../data/chunks.json', 'w') as json_file:
        json_file.write(json.dumps(chunks))
    print(f'saved to file')

preprocess()