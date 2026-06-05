import csv

def csv_to_dictionary():
    users = {}
    with open("data/users.csv") as new_file:
        for line in csv.reader(new_file, delimiter=","):
            if line[0] == "Username" or line[0] == "":
                continue
            users[line[0]] = {
                "correct_password": line[1],
                "wrong_passwords": line[2:]
            }

    print(users)        
    return users