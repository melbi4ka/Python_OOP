from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []


    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name):
        for current_task in self.tasks:
            if current_task.name == task_name:
                current_task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared = 0
        for current_task in self.tasks:
            if current_task.completed:
                self.tasks.remove(current_task)
                cleared += 1
        return f"Cleared {cleared} tasks."

    def view_section(self):
        x = "\n"
        result = f"Section {self.name}:{x}"
        for obj in self.tasks:
            result += obj.details()
            result += x

        return result.strip()


