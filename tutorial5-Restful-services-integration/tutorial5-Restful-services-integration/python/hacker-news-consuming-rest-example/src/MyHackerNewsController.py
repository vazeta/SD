from fastapi import APIRouter, Query
from typing import List, Optional
import requests
import logging
from pydantic import BaseModel

router = APIRouter()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hn")

# Pydantic models
class HackerNewsItemRecord(BaseModel):
    id: Optional[int]
    title: Optional[str]
    by: Optional[str]
    url: Optional[str]
    time: Optional[int]
    score: Optional[int]
    type: Optional[str]
    descendants: Optional[int]
    kids: Optional[List[int]]
    text: Optional[str]

#TODO: method annotations 
def hacker_news_top_stories(search: Optional[str] = Query(None)):
    #TODO: Get IDs of top stories

    #TODO: Iterate through each ID and check if it contains the "search" terms

    return ""
