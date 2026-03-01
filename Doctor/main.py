from utils.auth import AuthService
from models.doctor import Doctor
from utils.decorators import role_required


auth = AuthService()


# -----------------------------------
# DOCTOR DASHBOARD
# -----------------------------------
@role_required("Doctor")
def doctor_menu(doctor):
    while True:
        print("\n--- Doctor Dashboard ---")
        print("1. View Patient Record")
        print("2. Add Diagnosis")
        print("3. Prescribe Medication")
        print("4. Request Lab Test")
        print("5. Add Lab Result")
        print("6. Update Treatment Plan")
        print("7. Update Status")
        print("0. Logout")

        choice = input("Choice: ")

        if choice == "1":
            pid = input("Patient ID: ")
            patient, records = doctor.view_patient_record(pid)

            if not patient:
                print("Patient not found.")
                continue

            print("\n--- Patient Info ---")
            print(f"ID: {patient[0]}")
            print(f"Name: {patient[1]}")
            print(f"Age: {patient[2]}")
            print(f"Contact: {patient[3]}")
            print(f"Gender: {patient[4]}")
            print(f"Status: {patient[5]}")

            print("\n--- Medical History ---")
            if records:
                for r in records:
                    print(f"[{r[2]}] {r[0]}: {r[1]}")
            else:
                print("No medical records yet.")

        elif choice == "2":
            pid = input("Patient ID: ")
            diagnosis = input("Diagnosis: ")
            doctor.add_diagnosis(pid, diagnosis)
            print("Diagnosis added successfully.")

        elif choice == "3":
            pid = input("Patient ID: ")
            medication = input("Medication: ")
            doctor.prescribe_medication(pid, medication)
            print("Prescription added successfully.")

        elif choice == "4":
            pid = input("Patient ID: ")
            test = input("Lab Test: ")
            doctor.request_lab_test(pid, test)
            print("Lab request added successfully.")

        elif choice == "5":
            pid = input("Patient ID: ")
            result = input("Lab Result: ")
            doctor.review_lab_results(pid, result)
            print("Lab result added successfully.")

        elif choice == "6":
            pid = input("Patient ID: ")
            treatment = input("Treatment Plan: ")
            doctor.update_treatment(pid, treatment)
            print("Treatment plan updated successfully.")

        elif choice == "7":
            pid = input("Patient ID: ")
            status = input("New Status (Admitted/Discharged): ")
            doctor.update_status(pid, status)
            print("Status updated successfully.")

        elif choice == "0":
            print("Logging out...")
            break

        else:
            print("Invalid option.")


# -----------------------------------
# MAIN SYSTEM MENU
# -----------------------------------
def main():
    print("=== Health Clinic Patient Management System ===")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("0. Exit")

        choice = input("Choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            role = input("Role (Doctor): ")

            auth.register(name, email, password, role)
            print("Registration successful.")

        elif choice == "2":
            email = input("Email: ")
            password = input("Password: ")

            user = auth.login(email, password)

            if user:
                print("Login successful.")

                # user structure:
                # (id, name, email, password_hash, role)
                if user[4] == "Doctor":
                    doctor = Doctor(user[0], user[1], user[2], user[3])
                    doctor_menu(doctor)
                else:
                    print("Role not supported in this module.")
            else:
                print("Invalid email or password.")

        elif choice == "0":
            print("Exiting system...")
            break

        else:
            print("Invalid option.")


# -----------------------------------
# ENTRY POINT
# -----------------------------------
if __name__ == "__main__":
    main()