from pydantic import BaseModel
from typing import Optional

class NewEvent(BaseModel):
    event_name:str
    location:str
    time:str
    description:str
    uuid:int

class UpdateEvent(BaseModel):
    event_name:Optional[str]
    location:Optional[str]
    time:Optional[str]
    description:Optional[str]

    