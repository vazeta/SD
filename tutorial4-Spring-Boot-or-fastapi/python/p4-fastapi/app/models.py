from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Counter:
    def __init__(self):
        self.n = 0

    def next(self):
        self.n += 1
        return self.n

class Project(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = ""
    type: Optional[str] = ""
    color: Optional[str] = ""
    description: Optional[str] = ""
    days: Optional[int] = 0
    price: Optional[float] = 0.0
    featured: Optional[bool] = False
    launchDate: Optional[datetime] = None

class Employee(BaseModel):
    id: int
    name: str
    telephone: str
    salary: float
