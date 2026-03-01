#Importing Classes from modules
from patient import Patient
from staff import Staff
from admin import Admin

def admin_main():

    admin = Admin()

    while True:
        #Continue outputting options on program runime unless you choose EXIT
        print("\n\n------------Admin's sytem------------")
        print("1. Update Patient's Credentials")
        print("2. Update Staff's Credentials")
        print("3. Exit")

        choice = input("Choose one of the options above: ")

        if choice == "1":
            patient_id =  input("Enter the id of the patient to update: ")
            patient_updates = {}

            if patient_id:
                new_name = input("Enter the patient's new name(Leave blank if N/A): ")
                new_age = input("Enter the patient's new age(Leave blank if N/A): ")
                new_contact = input("Enter the patient's new contact(Leave blank if N/A): ")

                if new_name:
                    patient_updates["name"] = new_name
                if new_age:
                    patient_updates["age"] = int(new_age)
                if new_contact:
                    patient_updates["contact"] = new_contact

                #Abstraction => use of imported Class and methods
                patient = Patient(patient_id)
                admin.update_patient_credentials(patient, patient_updates)

            else:
                print("Patient ID cannot be empty")

        elif choice == "2":
            staff_id = input("Enter the id of the staff to update: ")
            staff_member_updates = {}

            if staff_id:
                new_name = input("Enter the patient's new name(Leave blank if N/A): ")
                new_contact = input("Enter the patient's new contact(Leave blank if N/A): ")
                new_role = input("Enter the patient's new role(Leave blank if N/A): ")

                if new_name:
                    staff_member_updates["name"] = new_name
                if new_contact:
                    staff_member_updates["contact"] = new_contact
                if new_role:
                    staff_member_updates["role"] = new_role

                #Abstraction => use of imported Class and methods
                staff_member = Staff(staff_id)
                admin.update_staff_credentials(staff_member, staff_member_updates)
            else:
                print("Staff ID cannot be empty")

        elif choice == "3":
            print("Exiting the system...")
            break #exit the loop and stop displaying options

        else: #condition for any other option apart from 1, 2, or 3
            print("Invalid option")

#You can call the function
# admin_main()

