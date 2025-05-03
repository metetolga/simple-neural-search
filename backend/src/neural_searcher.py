from qdrant_client import QdrantClient
from qdrant_client.models import Filter
from sentence_transformers import SentenceTransformer

class NeuralSearcher:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
        self.qdrant_client = QdrantClient("http://localhost:6333")
    
    def search(self, text:str, city:str = None):
        vector = self.model.encode(text).tolist()
        if city:
            city_filter = Filter(**{
                "must": [
                    {"key":"city", "match": {"value":city}}
                ]
            })
        search_result = self.qdrant_client.query_points(
            collection_name=self.collection_name, 
            query=vector, 
            query_filter= city_filter if city else None, 
            limit=5
        ).points
        print(f"Size of search result: {len(search_result)}")
        payloads = [hit.payload for hit in search_result]
        return payloads