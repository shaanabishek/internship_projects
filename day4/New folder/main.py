from grade_module import PASS_CUTOFFS

std = [
    {"name": "Arun", "subject": "Python", "score": 88},
    {"name": "Nisha", "subject": "Python", "score": 54},
    {"name": "Rahul", "subject": "DSA", "score": 22},
    {"name": "Priya", "subject": "DSA", "score": 95},
    {"name": "Karthik", "subject": "Python", "score": 71}
]

def status(score):
    if score >= PASS_CUTOFFS[2]:
        return "Distinction"
    elif score >= PASS_CUTOFFS[1]:
        return "Pass"
    else:
        return "Fail"

def subs():
    return {s["subject"] for s in std}

def add(name, subject, score):
    s = {
        "name": name,
        "subject": subject,
        "score": score,
        "status": status(score)
    }

    std.append(s)

    with open("grades_log.txt", "a") as f:
        f.write(f"{name}, {subject}, {score}, {status(score)}\n")

    print("\nStudent added!")

def show():
    print("\nGRADEVAULT")
    print("Name\t\tSubject\t\tScore\tStatus")

    for s in std:
        s["status"] = status(s["score"])
        print(f"{s['name']}\t\t{s['subject']}\t\t{s['score']}\t{s['status']}")

def avg(subject):
    marks = []

    for s in std:
        if s["subject"].lower() == subject.lower():
            marks.append(s["score"])

    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)

def top():
    best = std[0]

    for s in std:
        if s["score"] > best["score"]:
            best = s

    best["status"] = status(best["score"])
    return best

def search(name):
    for s in std:
        if s["name"].lower() == name.lower():
            s["status"] = status(s["score"])
            return s

    return "Not Found"

def dist():
    return [s["name"] for s in std if status(s["score"]) == "Distinction"]

show()

print("\nSubjects")
print(subs())

print("\nCutoffs")
print(PASS_CUTOFFS)

add("Sneha", "Python", 84)

show()

print("\nPython Average:", round(avg("Python"), 2))
print("DSA Average:", round(avg("DSA"), 2))

print("\nTop Scorer")
print(top())

print("\nSearch")
print(search("Rahul"))

print("\nDistinction Students")
print(dist())