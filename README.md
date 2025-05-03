# 🚀 Startup Semantic Search

Find the most relevant startups based on your sentence query — powered by neural search.

## 🧰 Technologies Used

<p align="left">
  <img src="https://cdn.worldvectorlogo.com/logos/python-5.svg" alt="Python" width="50"/>
  <img src="https://cdn.worldvectorlogo.com/logos/fastapi.svg" alt="FastAPI" width="50"/>
  <img src="https://cdn.worldvectorlogo.com/logos/react-2.svg" alt="React" width="50"/>
</p>

<p align="left">
  <img src="https://img.shields.io/badge/Uvicorn-ASGI%20Server-80d4fa?style=flat&logo=fastapi" alt="Uvicorn Badge"/>
  <img src="https://img.shields.io/badge/Qdrant-Vector%20DB-orange?style=flat&logo=databricks" alt="Qdrant Badge" />
  <img src="https://img.shields.io/badge/SentenceTransformers-BERT%20Embeddings-blueviolet?style=flat&logo=pytorch" alt="SentenceTransformers Badge"/>
</p>

## 📌 Project Overview

This app enables semantic search across a dataset of startup profiles.  
Users type a natural-language query, and the system returns the most relevant startups.

- 🔍 **Neural Search** with [`SentenceTransformer`](https://www.sbert.net/)
- 💾 **Qdrant** as the vector similarity engine
- ⚡ **FastAPI + Uvicorn** for backend API
- 🎯 **React** for the interactive frontend
