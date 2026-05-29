# Check username validity

username = input("Enter username: ")

valid = True

if len(username) < 3 or username[0] != 'x' or username[1] != 'm' or username[2] != '_':
    valid = False

if len(username) <= 8:
    valid = False

for ch in username:
    if not (
        ('a' <= ch <= 'z') or
        ('A' <= ch <= 'Z') or
        ('0' <= ch <= '9') or
        ch == '_'
    ):
        valid = False
        break

if valid:
    print("Valid username")
else:
    print("Invalid username")