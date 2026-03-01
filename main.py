from Admin.admin_main import admin_main
from Nurse import nurse_main
from Doctor import doctor_main
from Receptionist import receptionist_main

def main():
    while True:
        print("\n=== Hospital Management System ===")
        print("1. Receptionist")
        print("2. Nurse")
        print("3. Doctor")
        print("4. Admin")
        print("5. Exit")

        role = input("Select your role: ")

        if role == "1":
            receptionist_main()
        elif role == "2":
            nurse_main()
        elif role == "3":
            doctor_main()
        elif role == "4":
            admin_main()
        elif role == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
