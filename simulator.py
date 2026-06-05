import random
import requests
from time import sleep

url = "http://127.0.0.1:5000/login"

def generate_auth_traffic(users: dict):
    
    while True:
        user = choose_user_randomly(users)
        for x in range(6):
            password = choose_password_randomly(user, users)

            payload = {
                "username": user,
                "password": password
            }
            response = requests.post(url, data=payload)
            
            if is_login_successful(response):
                print("Login successful")
                sleep(random.randint(10, 60))
                break
            else:
                print("Login failed")
                sleep(random.randint(2, 7))
        sleep(random.randint(10, 60))


def choose_user_randomly(users: dict):
    return random.choice(list(users.keys()))

def choose_password_randomly(username: str, users: dict):
    passwords = users[username]["wrong_passwords"] + [users[username]["correct_password"]] 
    return random.choice(passwords)

def is_login_successful(response):
    return "successful" in response.text