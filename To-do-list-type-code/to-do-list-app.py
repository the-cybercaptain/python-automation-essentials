class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name):
        self.tasks[task_name] = False

    def remove_task(self, task_name):
        del self.tasks[task_name]

    def mark_done(self, task_name):
        self.tasks[task_name] = True

    def display_tasks(self):
        print("To-Do List:")
        for task, done in self.tasks.items():
            print(f"[{'✅' if done else ' '}] {task}")

# Usage
todo = ToDoList()
while True:
    print("\n1. Add Task\n2. Remove Task\n3. Mark Done\n4. Display Tasks\n5. Quit")
    choice = input("Enter choice: ")
    if choice == "1":
        task_name = input("Enter task name: ")
        todo.add_task(task_name)
    elif choice == "2":
        task_name = input("Enter task name: ")
        todo.remove_task(task_name)
    elif choice == "3":
        task_name = input("Enter task name: ")
        todo.mark_done(task_name)
    elif choice == "4":
        todo.display_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")