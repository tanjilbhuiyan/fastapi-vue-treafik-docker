# app/main.py

from fastapi import FastAPI

app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get("/api")
def read_root():
    return {"hello": "world"}