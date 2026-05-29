username = input("Enter username: ")

if (username.startswith("xm_")
        and username.replace("_", "").isalnum()
        and len(username) > 8):
    print("Valid Username")
else:
    print("Invalid Username")