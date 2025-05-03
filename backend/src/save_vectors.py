import json
import numpy as np
import pandas as pd 
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2", device="cuda")

df = pd.read_json("../data/startups_demo.json", lines=True)

print(df.loc[0])

# encode necessary information in json
# alt and description is necessary as you can see below
vectors = model.encode(
    [row.alt + ". " + row.description for row in df.itertuples()], 
    show_progress_bar=True
)

print(f"vectors shape: {vectors.shape}")
np.save("../data/startup_vectors.npy", vectors, allow_pickle=False)

