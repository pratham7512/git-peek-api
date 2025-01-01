# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from gitingest import ingest
import asyncio

app = FastAPI()

class Repository(BaseModel):
    repo_url: str

@app.post("/analyze")
async def analyze_repo(repo: Repository):
    # Get the current event loop
    loop = asyncio.get_event_loop()
    
    # Create a wrapper function to run synchronous code
    def run_ingest():
        return ingest(repo.repo_url)
    
    # Run the synchronous function in a thread pool
    summary, tree, content = await loop.run_in_executor(None, run_ingest)
    
    return {
        "summary": summary,
        "tree": tree,
        "content": content
    }
