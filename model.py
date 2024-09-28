from pydantic import BaseModel,Field,constr
from typing import Optional

class NewEvent(BaseModel):
    event_name:constr(strip_whitespace=True,min_length=1)
    location:str
    time:str
    description:str
    uuid:int=Field(...,gt=0)

class UpdateEvent(BaseModel):
    event_name:Optional[str]
    location:Optional[str]
    time:Optional[str]
    description:Optional[str]
