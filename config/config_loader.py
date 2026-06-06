from json import load

def config_to_dictionary():
    with open("config.json") as new_file:
        config = load(new_file)
        return config