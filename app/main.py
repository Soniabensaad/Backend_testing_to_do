from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud, database
from .models import Todo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Allow CORS from your frontend (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend address
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos", response_model=List[schemas.TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@app.post("/todos", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@app.put("/todos/{todo_id}", response_model=schemas.TodoResponse)  # Response should be TodoResponse
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_task = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = todo.title
    db_task.description = todo.description
    db_task.completed = todo.completed

    db.commit()
    db.refresh(db_task)
    return db_task  # Returning the updated Todo as TodoResponse

@app.delete("/todos/{todo_id}", response_model=List[schemas.TodoResponse])  # Return a list of TodoResponse
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_delete = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_delete is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_delete)
    db.commit()

    # Fetch and return the updated list of todos
    todos = crud.get_todos(db)
    return todos
