from typing import Dict




class TaskView:
"""Handles presentation of task data."""


def show_task(self, task: Dict[str, str]) -> str:
return f"Task {task['id']}: {task['description']} ({task['status']})"


def show_message(self, message: str) -> str:
return message


def show_not_found(self, task_id: str) -> str:
return f"Task {task_id} not found"
