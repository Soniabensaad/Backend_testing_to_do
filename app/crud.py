from sqlalchemy.orm import Session
from . import models, schemas
from .models import Todo

# In crud.py
def get_todos(db: Session):
    return db.query(Todo).all()


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
