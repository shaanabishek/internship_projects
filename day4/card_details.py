card = {
    "name": "Shaan Abishek",
    "role": "AI & Data Science Student",
    "email": "shaan@domain.com",
    "phone": "+91 1234567890",
}

def show():
    print("DIGITAL BUSINESS CARD")
    print("Name:", card["name"])
    print("Role:", card["role"])
    print("Email:", card["email"])
    print("Phone:", card["phone"])

show()

card["role"] = "Full Stack AI Developer Intern"

print("\nRole updated!")

show()