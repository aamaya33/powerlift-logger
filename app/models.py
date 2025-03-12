from pydantic import BaseModel
from typing import Optional

class Video(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    url: Optional[str] = None
    v