from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/tasks/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


@app.get("/tasks/", response_model=list[schemas.TaskOut])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit)


@app.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@app.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.update_task(db, task_id, task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
