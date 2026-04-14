# todo.py
def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("Belum ada tugas.")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

print("To-Do App")
task = input("Tambah tugas: ")
add_task(task)
show_tasks()