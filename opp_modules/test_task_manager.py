import unittest


from controller.task_controller import TaskController as TaskManager




class TestTaskManager(unittest.TestCase):


def setUp(self):
self.tm = TaskManager()


# Use Case 1 – Create Tasks
def test_create_task_success(self):
task = self.tm.create_task("1", "Buy groceries")
self.assertEqual(task["description"], "Buy groceries")
self.assertEqual(task["status"], "pending")


def test_create_task_duplicate_id(self):
self.tm.create_task("1", "Buy groceries")
with self.assertRaises(ValueError):
self.tm.create_task("1", "Another task")


# Use Case 2 – Update Tasks
def test_update_task_success(self):
self.tm.create_task("1", "Old description")
updated = self.tm.update_task("1", description="New description")
self.assertEqual(updated["description"], "New description")


def test_update_nonexistent_task(self):
with self.assertRaises(KeyError):
self.tm.update_task("99", description="Nothing")


# Use Case 3 – Delete Tasks
def test_delete_task_success(self):
self.tm.create_task("1", "Delete me")
result = self.tm.delete_task("1")
self.assertTrue(result)


def test_delete_nonexistent_task(self):
with self.assertRaises(KeyError):
self.tm.delete_task("55")




if __name__ == "__main__":
unittest.main()
