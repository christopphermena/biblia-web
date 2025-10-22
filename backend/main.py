#Importar FastAPI
from fastapi import FastAPI, Query
import json

app = FastAPI()

# Carga los versículos desde el archivo JSON
with open("../data/versiculos.json", "r", encoding="utf-8") as f:
    VERSES = json.load(f)

@app.get("/")
def root():
    return {"message": "API Biblia funcionando correctamente"}

@app.get("/versiculos")
def buscar(q: str = Query(..., min_length=1)):
    ql = q.lower()
    results = [v for v in VERSES if ql in v["text"].lower() or ql in v["book"].lower()]
    return {"results": results}
