import os
import json
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.models  import VectorParams, Distance

client = QdrantClient("http://localhost:6333")
CNAME = 'startups'

if __name__ == "__main__":
    if not client.collection_exists(CNAME):
        client.create_collection(
            collection_name=CNAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )
    
    fd = open('backend/data/startups_demo.json')

    payload = map(json.loads, fd)
    print(list(payload)[0]) # check an item 
    
    vectors = np.load("backend/data/startup_vectors.npy")
    client.upload_collection(
        collection_name=CNAME,
        vectors=vectors, 
        payload=payload,
        ids=None,
        batch_size=256
    )

