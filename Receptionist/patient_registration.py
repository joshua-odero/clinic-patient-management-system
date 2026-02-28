# Patient registration
import json
import os, sys

class Patient:

    def __init__(self, name, age, gender, contact, patient_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.patient_id = patient_id

    # Check if patient is already registered/ get patient data by id
    @staticmethod
    def get_patient_by_patient_id(patient_id):
        # Build file path where patient JSON is stored
        file_path = f"patients/{patient_id}.json"
        # if file does not exist, return None -> patient not found
        if not os.path.exists(file_path):
            return None
        
        # Reading JSON data from file 
        with open(file_path, "r") as file:
            patient_data = json.load(file)
            #print(patient_data)
        return patient_data # returns actual patient data (a dictionary)
    
    # Update patient details
    @staticmethod
    def update_patient_details(patient):
        # Extract patient ID from dictionary
        patient_id = patient.get("patient_id")
        file_path = f"patients/{patient_id}.json"
        # Only updates if file exists -> no file, no update
        if not os.path.exists(file_path):
            return None
        
        # Overwrite file with updated patient dictionary
        with open(file_path, "w") as file:
            json.dump(patient, file, indent=4)
        return True
    
    # Function to generate patient ids (using first name, and contact)
    @staticmethod
    def generate_patient_id(first_name, contact):
        # Convert first_name to lower
        first_name_lower = first_name.lower()
        # Convert contact to str using the str() and get the last four digits
        contact_string = str(contact)
        last_four = contact_string[-4:] # get last four digits
        # Combine or join first_name with last four digits
        patient_id = first_name_lower + last_four
        return patient_id # to be used in register_patient()
        
    # Function to register patients
    @staticmethod
    def register_patient():
        print("\nRegister new patient")

        # enter details
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        gender = input("Enter Patient Gender: ")
        contact = input("Enter Contact Number: ")
        # generate a random patient ID
        first_name = name.split()[0] 
        # split()-> splits a string into a list based on delimeters/spaces
        patient_id = Patient.generate_patient_id(first_name, contact)

        patient = {
            "name": name,
            "age": age,
            "gender": gender,
            "contact": contact,
            "patient_id": patient_id
        }

        # Saves patient data as JSON file 
        file_path = f"patients/{patient_id}.json"

        with open(file_path, "w") as file:
            json.dump(patient, file, indent=4)
            file.write("\n")
        print("Patient registered successfully.")
        return patient # return patient data -> useful if caller needs it

# Use
# patient = Patient.register_patient()

# prevents auto-execution
if __name__ == "__main__":
    Patient.register_patient()