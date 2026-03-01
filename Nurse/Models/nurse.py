import json
from Nurse.Models.patient import Patient   


class Nurse:
    
    def __init__(self, username, password):
        # save nurse login details
        self.username = username
        self.password = password
        
        # list to store patients added by this nurse
        self.patients = []


    @staticmethod
    def load_nurses(filename="Nurse/data/data.json"):
        # this reads nurse data from a JSON file
        
        try:
            # open the file in read mode
            with open(filename, "r") as file:
                return json.load(file)  # convert JSON data into Python list
        
        except FileNotFoundError:
            return []


    @staticmethod
    def authenticate(username, password, filename="Nurse/data/data.json"):
        # this method checks if login details are correct
        
        nurses = Nurse.load_nurses(filename)

        # check each nurse in the list
        for nurse_data in nurses:
            
            # compare username and password
            if nurse_data["name"] == username and nurse_data["password"] == password:
                print("Login successful ✅")
                
                return Nurse(username, password)
        print("Wrong username or password ❌")
        return None

    def add_patient(self, patient_id, name, age):
        patient = Patient(patient_id, name, age)
        
        # add the patient to the nurse's patient list
        self.patients.append(patient)
        
        print("Patient added successfully ✅")


    def record_vitals(self, patient_id, temperature, blood_pressure):
        # search for patient by ID
        for patient in self.patients:
            
            # if ID matches, update temperature and blood pressure
            if patient.patient_id == patient_id:
                patient.temperature = temperature
                patient.blood_pressure = blood_pressure
                
                print("Vitals recorded successfully ✅")
                return
        print("Patient not found ❌")


    def view_patients(self):
        if not self.patients:
            print("No patients available.")
            return

        # display details of each patient
        for patient in self.patients:
            print("\n--- Patient Details ---")
            patient.display_info()  # call display_info method from Patient class

    
  