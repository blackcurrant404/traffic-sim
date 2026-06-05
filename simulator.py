import random
import requests
from time import sleep

url = "http://127.0.0.1:5000/login"

def generate_auth_traffic(users: dict):
    
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
            sleep(60)
            return
        sleep(5)

    print("Login failed")
    sleep(60)

def choose_user_randomly(users: dict):
    namelist = []
    for username, x in users.items():
        namelist.append(username)
    return random.choice(namelist)

def choose_password_randomly(username: str, users: dict):
    passwords = users[username]["wrong_passwords"] + [users[username]["correct_password"]] 
    return random.choice(passwords)

def is_login_successful(response):
    return "successful" in response.text