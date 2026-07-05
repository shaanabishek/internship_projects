emails = [
    "alice@gmail.com",
    "bob@gmail.com",
    "charlie@gmail.com",
    "alice@gmail.com",
    "david@gmail.com",
    "eve@gmail.com",
    "bob@gmail.com",
    "frank@gmail.com"
]

print("ORIGINAL EMAIL LIST")
for i in emails:
    print(i)

unique = set(emails)
dup = len(emails) - len(unique)

print("\nUNIQUE EMAILS")
for i in unique:
    print(i)

print("\nOriginal Count:", len(emails))
print("Unique Count:", len(unique))
print("Duplicates Removed:", dup)