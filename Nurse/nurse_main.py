from Nurse.Models.nurse import Nurse  


def nurse_main():
    print("---- Nurse Login ----")
    
    # Get login credentials from user
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Authenticate nurse using stored data in nurses.json
    nurse = Nurse.authenticate(username, password, filename="nurses.json")
    
    # If authentication fails, exit the program
    if not nurse:
        print("Exiting program.")
        return

    # Main menu loop (runs until user chooses to exit)
    while True:
        print("\n--- Nurse Menu ---")
        print("1. Add Patient")
        print("2. Record Vitals")
        print("3. View Patients")
        print("4. Exit")

        # Get user choice
        choice = input("Enter your choice: ").strip()

        # Option 1: Add a new patient
        if choice == "1":
            pid = input("Patient ID: ").strip()
            name = input("Name: ").strip()
            age = input("Age: ").strip()
            
            # Call method from Nurse class to add patient
            nurse.add_patient(pid, name, age)

        # Option 2: Record patient vitals
        elif choice == "2":
            pid = input("Patient ID: ").strip()
            temp = input("Temperature: ").strip()
            bp = input("Blood Pressure: ").strip()
            
            # Call method from Nurse class to record vitals
            nurse.record_vitals(pid, temp, bp)

        # Option 3: View all patients
        elif choice == "3":
            # Display patient records
            nurse.view_patients()

        # Option 4: Exit program
        elif choice == "4":
            print("Exiting program...")
            break

        # Handle invalid menu choice
        else:
            print("Invalid choice ❌")
