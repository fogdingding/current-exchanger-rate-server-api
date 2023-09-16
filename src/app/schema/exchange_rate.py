from typing import Union, List
from pydantic import BaseModel
from .base import ApiErrorResponse

# User Order

class change_info(BaseModel):
    source: str
    target:str
    amount:str

class changed_data(BaseModel):
    msg: str = 'success'
    amount: str
