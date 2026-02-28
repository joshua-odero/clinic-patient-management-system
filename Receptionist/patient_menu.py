from patient_registration import Patient

class PatientMenu:

    @staticmethod
    def run():
        while True:
            print("\n*** Patient Menu ***")
            print("1. Register Patient")
            print("2. Find Patient")
            print("3. Update Patient")
            print("4. Back")

            choice = input("Select option: ")

            if choice == "1":
                Patient.register_patient()

            elif choice == "2":
                patient_id = input("Patient ID: ")
                patient = Patient.get_patient_by_patient_id(patient_id)
                if not patient:
                    print("Not found.")
                else:
                    print("Patient found")
                    print(patient)

            elif choice == "3":
                patient_id = input("Patient ID: ")
                patient = Patient.get_patient_by_patient_id(patient_id)

                if not patient:
                    print("Not found.")
                    continue

                print("Leave a blank to keep current value")

                updated = {
                    "name": input("Name: "),
                    "age": int(input("Age: ")),
                    "gender": input("Gender: "),
                    "contact": input("Contact: "),
                    "patient_id": patient_id
                }

                Patient.update_patient_details(updated)

            elif choice == "4":
                break

if __name__ == "__main__":
    PatientMenu.run()