from data_loader import csv_to_dictionary
from simulator import generate_auth_traffic
from config.config_loader import config_to_dictionary

def main():
    config = config_to_dictionary()
    users = csv_to_dictionary()
    generate_auth_traffic(users, config)
    
if __name__ == "__main__":
    main()