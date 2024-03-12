import time
from typing import List
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http.models.models import Filter, SearchParams

from config import QDRANT_URL, QDRANT_API_KEY, EMBEDDINGS_MODEL


class NeuralSearcher:

    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        self.qdrant_client = QdrantClient(host='localhost', port=6333)
        self.qdrant_client.set_model(EMBEDDINGS_MODEL)
        self.model = SentenceTransformer(EMBEDDINGS_MODEL)

    def search(self, text: str,ticker = None, filter_: dict = None) -> List[dict]:
        start_time = time.time()
        hits = self.qdrant_client.query(
            collection_name=self.collection_name,
            query_text=text,
            query_filter=Filter(**filter_) if filter_ else None,
            limit=100
        )
        print(f"Search took {time.time() - start_time} seconds")
        if ticker is None:
            return [hit.metadata for hit in hits]
        else:
            return [hit.metadata for hit in hits]

    # def search_with_vector(self, texts: list[str], filter_: dict = None, limit: int = 100) -> List[dict]:
    #     # Generate vectors for each text in the list
    #     query_vectors = self.model.encode(texts)
    #
    #     # Prepare results list
    #     results = []
    #
    #     # Search for each vector in Qdrant
    #     for vector in query_vectors:
    #         # Convert vector to list if it's a numpy array
    #         if not isinstance(vector, list):
    #             vector = vector.tolist()
    #         print(vector)
    #
    #         # Perform the search
    #         hits = self.qdrant_client.search(
    #             collection_name=self.collection_name,
    #             query_vector=vector,
    #             # search_params=SearchParams(k=limit),
    #             query_filter=Filter(**filter_) if filter_ else None,
    #         )
    #
    #         # Extract and store the results
    #         for hit in hits['result']:
    #             results.append(hit['payload'])  # Assuming you store useful information in 'payload'
    #
    #     return results