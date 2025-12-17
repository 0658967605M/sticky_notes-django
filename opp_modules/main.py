from controller.task_controller import TaskController




def demo():
tm = TaskController()
tm.create_task("1", "Demo task inside OOP_Modules")
print(tm.present_task("1"))




if __name__ == "__main__":
    demo()
