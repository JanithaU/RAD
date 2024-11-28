from fastapi import APIRouter
from db.schema import NoteRead, NoteBase, UserCreate, UserRead,UserBase,UserListRead
from services.note_service import get_all_notes,create_note,change_note,remove_note,view_note
from services.user_service import get_all_users,create_user
from core.permission import admin_only , get_current_user

from db.session import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List 
from db.models import User


note_router = APIRouter(dependencies=[Depends(get_current_user)])
user_router = APIRouter()



## Users
@user_router.get("/", response_model=List[UserListRead])
def get_users( users: UserListRead = Depends(admin_only), db: Session = Depends(get_db)): # Only Admins can see the userlist
    response = get_all_users(db=db)
    return response

@user_router.post("/create",response_model=UserListRead)
def add_user(user: UserCreate, db: Session = Depends(get_db) ):
    response = create_user(user=user,db=db)
    return response






## Notes
@note_router.get("/",response_model=List[NoteRead])
def get_notes(db: Session = Depends(get_db)):
    notes = get_all_notes(db=db)
    return notes

@note_router.get("/view/{note_id}", response_model=NoteRead)
def get_note(note_id: int,  db: Session = Depends(get_db)):
    response = view_note(id=note_id, db=db)
    return response


@note_router.post("/create",response_model=NoteRead)
def add_note(note: NoteBase , db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    data_note = create_note(data=note, db=db,current_user=current_user)
    return data_note


@note_router.put("/update/{note_id}", response_model=NoteRead)
def update_note(note_id: int, note: NoteBase, db: Session = Depends(get_db)):
    response = change_note(id=note_id,data=note, db=db)
    return response


@note_router.delete("/delete/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    response = remove_note(id=note_id,db=db)
    return response
    