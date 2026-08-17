from sqlalchemy.orm import Session
from typing import List, Tuple, Optional
from app.models.task import Task
from app.repositories.task_repo import create_task, get_task, delete_task, update_task, search_tasks
from app.schemas.task import TaskCreate, TaskUpdate

def create_new_task(db: Session, payload: TaskCreate, created_by: int) -> Task:
    task = Task(
        title=payload.title,
        description=payload.description,
        due_date=payload.due_date,
        priority=payload.priority,
        assignee_id=payload.assignee_id,
        created_by=created_by
    )
    return create_task(db, task)

def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:
    return get_task(db, task_id)

def remove_task(db: Session, task: Task) -> None:
    return delete_task(db, task)

def modify_task(db: Session, task: Task, payload: TaskUpdate) -> Task:
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(task, field, value)
    return update_task(db, task)

def list_tasks(db: Session, q: Optional[str], status: Optional[str], priority: Optional[str], page: int, per_page: int) -> Tuple[List[Task], int]:
    skip = (page - 1) * per_page
    return search_tasks(db, q, status, priority, skip, per_page)
