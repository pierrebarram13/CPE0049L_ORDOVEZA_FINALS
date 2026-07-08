def login(username, password):
    print(f"{username} logged in.")

from database import users

def login(username, password):
    if username in users and users[username] == password:
        print("Login successful.")
        return True

    print("Invalid credentials.")
    return False