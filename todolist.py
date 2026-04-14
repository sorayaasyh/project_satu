# todo.py
def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("Belum ada tugas.")

print("To-Do App")
show_tasks()