from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Engagement Service")

stats_db = {}

class Stats(BaseModel):
    views: int = 0
    likes: int = 0

@app.post("/engage/{article_id}/view", response_model=Stats)
def add_view(article_id: str):
    stats = stats_db.get(article_id, {"views": 0, "likes": 0})
    stats["views"] += 1
    stats_db[article_id] = stats
    return stats

@app.post("/engage/{article_id}/like", response_model=Stats)
def add_like(article_id: str):
    stats = stats_db.get(article_id, {"views": 0, "likes": 0})
    stats["likes"] += 1
    stats_db[article_id] = stats
    return stats

@app.get("/engage/{article_id}/stats", response_model=Stats)
def get_stats(article_id: str):
    return stats_db.get(article_id, {"views": 0, "likes": 0})
