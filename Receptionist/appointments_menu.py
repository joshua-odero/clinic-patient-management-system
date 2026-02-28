from appointments import Appointment

class AppointmentMenu:

    @staticmethod
    def run():
        while True:
            print("\n*** Appointment Menu ***")
            print("1. Start Appointment")
            print("2. Update Appointment")
            print("3. Checkout Patient")
            print("4. Back")

            choice = input("Select option: ")

            if choice == "1":
                patient_id = input("Enter Patient ID: ")
                reason = input("Enter Reason: ")
                Appointment.new_appointment(patient_id, reason)

            elif choice == "2":
                appointment_id = input("Enter Appointment ID: ")
                key = input("Field to update: ")
                value = input("New value: ")
                Appointment.update_appointment(appointment_id, {key: value})

            elif choice == "3":
                appointment_id = input("Enter Appointment ID: ")
                Appointment.checkout_patient(appointment_id)

            elif choice == "4":
                break

            else:
                print("Invalid option")

if __name__ == "__main__":
    AppointmentMenu.run()