tasks = [
    "Complete Python assignment",
    "Attend internship",
    "Practice Data Structures"
]

def add(task):
    tasks.append(task)
    print(task, "added")

def done(task):
    if task in tasks:
        tasks.remove(task)
        print(task, "completed")
    else:
        print("Task not found")

def count():
    return len(tasks)

def show():
    print("TO-DO LIST")
    for i in range(len(tasks)):
        print(i + 1, ".", tasks[i])

show()

add("Review Day 4 tasks")

done("Attend internship")

show()

print("\nPending Tasks:", count())