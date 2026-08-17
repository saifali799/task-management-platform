from sqlalchemy.orm import Session
from typing import List, Optional, Tuple
from sqlalchemy import or_
from app.models.task import Task, TaskStatus, TaskPriority

def create_task(db: Session, task: Task) -> Task:
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()

def delete_task(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()

def update_task(db: Session, task: Task) -> Task:
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def search_tasks(db: Session, q: Optional[str], status: Optional[str], priority: Optional[str], skip: int, limit: int) -> Tuple[List[Task], int]:
    query = db.query(Task)
    if q:
        qpattern = f"%{q}%"
        query = query.filter(or_(Task.title.ilike(qpattern), Task.description.ilike(qpattern)))
    if status:
        try:
            query = query.filter(Task.status == TaskStatus(status))
        except Exception:
            pass
    if priority:
        try:
            query = query.filter(Task.priority == TaskPriority(priority))
        except Exception:
            pass
    total = query.count()
    items = query.order_by(Task.created_at.desc()).offset(skip).limit(limit).all()
    return items, total
