"""Model: store tasks and provide basic CRUD operations."""
from typing import Dict, Optional




class TaskModel:
"""Simple in-memory model for tasks.


Each task is a dict with keys: id, description, status.
"""


def __init__(self) -> None:
self._tasks: Dict[str, Dict[str, str]] = {}


def create(self, task_id: str, description: str) -> Dict[str, str]:
if task_id in self._tasks:
raise ValueError(f"Task with id {task_id} already exists")


task = {"id": task_id, "description": description, "status": "pending"}
self._tasks[task_id] = task
return task


def get(self, task_id: str) -> Optional[Dict[str, str]]:
return self._tasks.get(task_id)


def update(self, task_id: str, description: Optional[str] = None, status: Optional[str] = None) -> Dict[str, str]:
if task_id not in self._tasks:
raise KeyError(f"Task with id {task_id} not found")


task = self._tasks[task_id]
if description is not None:
task["description"] = description
if status is not None:
task["status"] = status
return task


def delete(self, task_id: str) -> bool:
if task_id not in self._tasks:
raise KeyError(f"Task with id {task_id} not found")
del self._tasks[task_id]
return True