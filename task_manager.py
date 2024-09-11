# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (невыполненных) задач.


class Task:
    ''' Класс Task хранит информацию о задаче, включая описание, срок выполнения'''

    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        """Отметить задачу как выполненную."""
        self.completed = True

    def __str__(self):
        """Строковое представление задачи."""
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    '''Класс TaskManager управляет списком задач.'''

    def __init__(self):
        """Инициализация менеджера задач."""
        self.tasks = []

    def add_task(self, description, deadline):
        """Добавить новую задачу."""
        new_task = Task(description, deadline)
        self.tasks.append(new_task)
        print(f"Задача добавлена: {new_task}")

    def mark_task_completed(self, task_index):
        """Отметить задачу как выполненную по индексу."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print(f"Задача отмечена как выполненная: {self.tasks[task_index]}")
        else:
            print("Некорректный индекс задачи.")

    def show_current_tasks(self):
        """Вывести список текущих (не выполненных) задач."""
        print("Текущие задачи:")
        for index, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{index}. {task}")
