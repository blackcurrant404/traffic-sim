from data_loader import csv_to_dictionary
from simulator import generate_auth_traffic

def main():
    users = csv_to_dictionary()
    generate_auth_traffic(users)
    
if __name__ == "__main__":
    main()