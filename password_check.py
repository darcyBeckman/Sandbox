MIN_LENGTH = 4
password = input("Password: ")
while len(password) < MIN_LENGTH:
    print(f"Your password must be {MIN_LENGTH} characters long")
    password = input("Password: ")
print(len(password) * "*")
