# Дженеричний клас планувальника завдань
class TaskScheduler<TTask, TPriority>:

    # Черга завдань з пріоритетами

    _queue = PriorityQueue()

    # Делегат для виконання завдань

    _task_execution = None

    # Створити новий планувальник завдань

    def __init__(self, task_execution: TaskExecution<TTask>):
        self._task_execution = task_execution

    # Додати завдання до планувальника

    def add_task(self, task: TTask, priority: TPriority):
        self._queue.put((priority, task))

    # Виконати наступне завдання

    def execute_next(self):
        priority, task = self._queue.get()
        self._task_execution(task)

    # Отримати об'єкт з пулу

    def get_from_pool(self):
        return self._task_execution.get_from_pool()

    # Повернути об'єкт в пул

    def return_to_pool(self, task: TTask):
        self._task_execution.return_to_pool(task)

    # Введення завдань з консолі

    def read_tasks(self):
        while True:
            print("Введіть завдання (порожній рядок для завершення):")
            task = input()
            if not task:
                break

            priority = int(input("Введіть пріоритет (1-10):"))
            self.add_task(task, priority)


# Делегат для виконання завдань

def task_execution(task: str):
    print("Виконується завдання:", task)
    time.sleep(random.randint(1, 10))
    print("Завдання виконано:", task)


# Приклад використання планувальника завдань

def main():
    scheduler = TaskScheduler(task_execution)

    # Введення завдань з консолі

    scheduler.read_tasks()

    # Виконання завдань

    while not scheduler._queue.empty():
        scheduler.execute_next()


if __name__ == "__main__":
    main()
