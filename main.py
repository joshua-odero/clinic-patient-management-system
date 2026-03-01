#Importing Classes from modules
from Admin.admin_main import admin_main
from Receptionist.receptionist_main import MainApp
from Nurse.nurse_main import nurse_main

#CLI entry point
def main():
    while True:
        #What to print on CLI entry point
        print("\n------------Clinic Management System------------")
        print("Choose your role")
        print("1. Admin")
        print("2. Reception")
        print("3. Nurse")
        print("4. Doctor")

        role = input("Select your role: ")

        if role == "1":
            admin_main()
        elif role == "2":
            MainApp.run()
        elif role == "3":
            nurse_main()
        elif role == "4":
            pass
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
