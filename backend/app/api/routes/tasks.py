from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import Optional
from sqlalchemy.orm import Session
from app.api.dependencies import get_db, get_current_user
from app.schemas.task import TaskCreate, TaskOut, TaskUpdate
from app.services.task_service import create_new_task, get_task_by_id, remove_task, modify_task, list_tasks

router = APIRouter()

@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = create_new_task(db, payload, created_by=current_user.id)
    return task

@router.get("/", response_model=list[TaskOut])
def read_tasks(q: Optional[str] = Query(None), status: Optional[str] = Query(None), priority: Optional[str] = Query(None), page: int = 1, per_page: int = 10, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    items, total = list_tasks(db, q, status, priority, page, per_page)
    return items

@router.get("/{task_id}", response_model=TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    if current_user.id != task.created_by and current_user.id != task.assignee_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update task")
    updated = modify_task(db, task, payload)
    return updated

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    if current_user.id != task.created_by:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete task")
    remove_task(db, task)
    return None
