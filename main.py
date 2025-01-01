# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from gitingest import ingest

app = FastAPI()

class Repository(BaseModel):
    repo_url: str

@app.post("/analyze")
async def analyze_repo(repo: Repository):
    summary, tree, content = ingest(repo.repo_url)
    return {
        "summary": summary,
        "tree": tree,
        "content": content
    }
