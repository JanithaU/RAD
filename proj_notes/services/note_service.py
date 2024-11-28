from fastapi import HTTPException
from db.models import Note
from core.permission import current_user_var



def get_all_notes(db):
    user_id = current_user_var.get(None)
    if user_id:
        notes = db.query(Note).filter(Note.user_id == user_id).all()
        return notes
    raise HTTPException(status_code=404, detail="No Notes found")


def create_note(data,db,current_user):
    data_note = Note(content=data.content, user_id=current_user.id)
    db.add(data_note)
    db.commit()
    return data_note


def change_note(id,data,db):
    user_id = current_user_var.get(None)
    note_user_id = db.query(Note).filter(Note.id == id).first()
    if user_id == note_user_id.user_id:
        existing_note = db.query(Note).filter(Note.id == id and Note.user_id == user_id).first()
    
    # existing_note = db.query(Note).filter(Note.id == id).first()
        if not existing_note:
            raise HTTPException(status_code=404, detail="Note not found")
    else:
        raise HTTPException(status_code=404, detail="Note is not belongs to you !")
    
    existing_note.content = data.content
    db.commit()
    db.refresh(existing_note)  
    return existing_note


def remove_note(id,db):
    user_id = current_user_var.get(None)
    existing_note = db.query(Note).filter(Note.id == id).first()
    if not existing_note:
        raise HTTPException(status_code=404, detail="Note not found")


    if user_id == existing_note.user_id:
        db.delete(existing_note)
        db.commit()
        return {"message": f"Note with ID {id} successfully deleted"}
    raise HTTPException(status_code=404, detail="Note is not belongs to you !")


def view_note(id,db):
    user_id = current_user_var.get(None)
    note = db.query(Note).filter(Note.id==id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    if user_id == note.user_id:
        return note
    else:
        raise HTTPException(status_code=404, detail="Note is not belongs to you !")