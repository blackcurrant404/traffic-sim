import random

def generate_auth_traffic():
    pass

def choose_password_randomly(users: dict):
    for name, x in users.items():
        passwords = users[name]["wrong_passwords"]
        passwords.append(users[name]["correct_password"])
        y = random.choice(passwords)
    return y