import json
import os.path

from fastapi.openapi import docs
from qdrant_client import QdrantClient, models
from tqdm import tqdm

from neural_search.config import DATA_DIR, QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME, TEXT_FIELD_NAME, EMBEDDINGS_MODEL


def upload_embeddings():
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        prefer_grpc=True,
    )

    client.set_model(EMBEDDINGS_MODEL)

    payload_path = os.path.join(DATA_DIR, 'chunks.json')
    payload = []
    documents = []

    with open(payload_path, 'r') as fd:
        json_data = json.load(fd)

    for obj in json_data:
        # payload.append(obj)
        documents.append(obj.pop('text'))
        obj["tickers"] = obj.pop("tickers")
        obj["pdf_name"] = obj.pop("pdf_name")
        obj['page_number'] = obj.pop('page_number')
        payload.append(obj)

    # with open(payload_path) as fd:
    #     for line in fd:
    #         obj = json.loads(line)
    #         print(f'obj = {obj}')
    #         # Rename fields to unified schema
    #         documents.append(obj.pop('text'))
    #         obj["tickers"] = obj.pop("tickers")
    #         obj["pdf_name"] = obj.pop("pdf_name")
    #         obj['page_number'] = obj.pop('page_number')
    #
    #         payload.append(obj)

    collections = client.get_collections()
    if COLLECTION_NAME in collections:
        print("exists")
        exit()
    # exists = client.get_collection(COLLECTION_NAME)
    # print(exists)
    # print(client.get_collections())
    # if client.get_collection(COLLECTION_NAME):
    #     print(f'Collection {COLLECTION_NAME} extsts')
    #     client.delete_collection(COLLECTION_NAME)
    #     print(f'Collection {COLLECTION_NAME} deleted')

    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=client.get_fastembed_vector_params(on_disk=True),
        # Quantization is optional, but it can significantly reduce the memory usage
        quantization_config=models.ScalarQuantization(
            scalar=models.ScalarQuantizationConfig(
                type=models.ScalarType.INT8,
                quantile=0.99,
                always_ram=True
            )
        )
    )

    # Create a payload index for text field.
    # This index enables text search by the TEXT_FIELD_NAME field.
    client.create_payload_index(
        collection_name=COLLECTION_NAME,
        field_name=TEXT_FIELD_NAME,
        field_schema=models.TextIndexParams(
            type=models.TextIndexType.TEXT,
            tokenizer=models.TokenizerType.WORD,
            min_token_len=2,
            max_token_len=20,
            lowercase=True,
        )
    )

    print(f'payload: {len(payload)}')
    print(f'collection: {COLLECTION_NAME}')
    print(f'docs: {len(documents)}')
    print(f'doc {documents[0]}')

    client.add(
        collection_name=COLLECTION_NAME,
        documents=documents,
        metadata=payload,
        ids=tqdm(range(len(payload))),
        parallel=0,
    )


if __name__ == '__main__':
    upload_embeddings()
