from fastapi import FastAPI
from neural_searcher import NeuralSearcher

app = FastAPI()

searcher = NeuralSearcher(collection_name="startups")

@app.post("/api/search")
def search_startup(q:str, city:str=None):
    return {"result":searcher.search(text=q, city=city)}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)