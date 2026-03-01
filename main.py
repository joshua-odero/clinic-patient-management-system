#Importing Classes from modules
from Admin.admin_main import admin_main
from Receptionist.receptionist_main import MainApp

def main():
    while True:
        print("\n=== Hospital Management System ===")

        print("1. Admin")
        print("2. Reception")

        role = input("Select your role: ")

        if role == "1":
            admin_main()
            print("You have chosen 1")
        elif role == "2":
            MainApp.run()
        else:
            print("Invalid selection. Try again.")

main()
