from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI(title="Content Service")

class Article(BaseModel):
    id: str
    title: str
    body: str

class ArticleCreate(BaseModel):
    title: str
    body: str

db = {}

@app.get("/content", response_model=List[Article])
def list_articles():
    return list(db.values())

@app.get("/content/{article_id}", response_model=Article)
def get_article(article_id: str):
    article = db.get(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@app.post("/content", response_model=Article)
def create_article(payload: ArticleCreate):
    article_id = str(uuid.uuid4())
    article = {
        "id": article_id,
        "title": payload.title,
        "body": payload.body
    }
    db[article_id] = article
    return article
