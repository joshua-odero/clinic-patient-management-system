from patient_menu import PatientMenu
from staff_menu import StaffMenu
from appointments_menu import AppointmentMenu


class MainApp:

    @staticmethod
    def run():
        while True:
            print("\n*** Community Clinic Management System ***")
            print("1. Patient Management")
            print("2. Staff Management")
            print("3. Appointment Management")
            print("4. Exit")

            choice = input("Select option: ")

            if choice == "1":
                PatientMenu.run()

            elif choice == "2":
                StaffMenu.run()

            elif choice == "3":
                AppointmentMenu.run()

            elif choice == "4":
                print("Exiting system.")
                break

            else:
                print("Invalid option.")


if __name__ == "__main__":
    MainApp.run()