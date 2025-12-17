from typing import Dict, Optional


from model.task_model import TaskModel
from view.task_view import TaskView




class TaskController:
"""Controller connects the Model and View.
Methods match the tests' expectations.
"""


def __init__(self) -> None:
self._model = TaskModel()
self._view = TaskView()


def create_task(self, task_id: str, description: str) -> Dict[str, str]:
return self._model.create(task_id, description)


def get_task(self, task_id: str) -> Optional[Dict[str, str]]:
return self._model.get(task_id)


def update_task(
self,
task_id: str,
*,
description: Optional[str] = None,
status: Optional[str] = None,
) -> Dict[str, str]:
return self._model.update(task_id, description=description, status=status)


def delete_task(self, task_id: str) -> bool:
return self._model.delete(task_id)


def present_task(self, task_id: str) -> str:
task = self.get_task(task_id)
if not task:
return self._view.show_not_found(task_id)
return self._view.show_task(task)
