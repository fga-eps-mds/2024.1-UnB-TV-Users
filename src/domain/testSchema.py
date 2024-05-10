from typing import Optional
from pydantic import BaseModel, ConfigDict
from fastapi_filter import FilterDepends, with_prefix
from sqlalchemy import or_
from fastapi_filter.contrib.sqlalchemy import Filter
from model import testModel

class Test(BaseModel):
    name: str
    liked: bool

class TestUpdate(BaseModel):
    name: str
    liked: bool