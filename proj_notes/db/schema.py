from pydantic import BaseModel, Field
from typing import List,Optional
from datetime import datetime



class UserBase(BaseModel):
    username: str = Field(max_length=50)
    role: str = Field(max_length=6, default="user")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=255)

class UserListRead(UserBase):
    id: int

    class Config:
            from_attributes  = True



class NoteBase(BaseModel):
    content: str = Field(min_length=2)

class NoteRead(NoteBase):
    id: int
    created_date: datetime
    updated_date: Optional[datetime] = None
    user_id: int

    class Config:
        from_attributes  = True

class UserRead(UserBase):
    id: int
    notes: List[NoteRead] = []

    class Config:
        from_attributes  = True


class TaskRequest(BaseModel):
    task_data: str
    callback_url: str
    data: Optional[dict] = None