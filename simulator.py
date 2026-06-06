import random
import requests
from time import sleep

def generate_auth_traffic(users: dict, config: dict):

    url = config["login_url"]
    
    while True:

        user = choose_user_randomly(users)
        user_profile = choose_user_profile_randomly(config)
        delay_min = user_profile["delay"]["min"]
        delay_max = user_profile["delay"]["max"]
        session_break_min = config["session_break"]["min"]
        session_break_max = config["session_break"]["max"]
        max_retries = int(user_profile["retries"])

        for x in range(max_retries):
            password = choose_password_randomly(user, users)
    
            payload = {
                "username": user,
                "password": password
            }
            response = requests.post(url, data=payload)
            
            if is_login_successful(response):
                print("Login successful")
                sleep(random.randint(session_break_min, session_break_max))
                break
            else:
                print("Login failed")
                sleep(random.randint(delay_min, delay_max))
        sleep(random.randint(session_break_min, session_break_max))


def choose_user_randomly(users: dict):
    return random.choice(list(users.keys()))

def choose_password_randomly(username: str, users: dict):
    passwords = users[username]["wrong_passwords"] + [users[username]["correct_password"]] 
    return random.choice(passwords)

def choose_user_profile_randomly(config: dict):
    profile_name = random.choice(list(config["user_profiles"].keys()))
    return config["user_profiles"][profile_name]

def is_login_successful(response):
    return "successful" in response.text