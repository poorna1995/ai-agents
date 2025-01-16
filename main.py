from src.crawler import GitHubCrawler
from fastapi import APIRouter, HTTPException
from fastapi import FastAPI
from dataclasses import dataclass, asdict
from pydantic import BaseModel


import logging
logger = logging.getLogger(__name__)


app = FastAPI()

class URLRequest(BaseModel):
    url: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/crawl/")
async def crawl_github(url_request: URLRequest):
    crawler = GitHubCrawler()
    meta_data = crawler.invoke()
    return meta_data