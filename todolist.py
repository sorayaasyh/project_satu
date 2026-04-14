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

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Keluar")

    choice = input("Pilih: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Masukkan tugas: ")
        add_task(task)
    elif choice == "3":
        print("Bye!")
        break