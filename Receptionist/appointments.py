# Scheduling Appointments
import json
import os
from datetime import datetime
from patient_registration import Patient

class Appointment:
    # check if patient exists in the system
    @staticmethod
    def patient_exists(patient_id):
        # use Patient.get_patient_by_patient_id()
        # this verifies that patient record exists
        # returns True if patient exists, otherwise False
        return Patient.get_patient_by_patient_id(patient_id) is not None
    
    # check for active appointment
    @staticmethod 
    def active_appointment_exists(patient_id):
        # scans through all JSON files
        # finds an appointment with matching patient_id and active status
        # returns existing appointment if found, otherwise None
        # iterate through files
        for file in os.listdir("appointments"):
            # process only JSON files
            if not file.endswith(".json"):
                continue

            file_path = f"appointments/{file}"
            
            # load appointment data
            with open(file_path, "r") as file:
                appointment = json.load(file)

            # check for matching patient with active status
            if appointment.get("patient_id") == patient_id and appointment.get("status"):
                return appointment # active appointment found
            
        return None # if appointment not found
    

    # start new appointment
    @staticmethod
    def new_appointment(patient_id, reason):
        # creates a new appointments only if patient exists and no active appointment
        # saves appointment as JSON
        # patient validation
        if not Appointment.patient_exists(patient_id):
            print("Patient not found.")
            return None
        
        # prevent duplicate appointment
        existing = Appointment.active_appointment_exists(patient_id)
        if existing:
            print("Active appointment for patient {patient_id} already exists.")
            return existing # does not proceed to create a new one
        
        # unique appointment_id
        appointment_id = f"{patient_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # appointment data structure
        appointment = {
            "appointment_id": appointment_id,
            "patient_id": patient_id,
            "reason": reason,
            "status": "active",  # Active means appointment is ongoing
            "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Record start time
            "end_time": None  # No end time until checkout
        }

        # File path to store appointment data
        file_path = f"appointments/{appointment_id}.json"

        # Write appointment data to file
        with open(file_path, "w") as file:
            json.dump(appointment, file, indent=4)

        print(f"Appointment started: {appointment_id}")
        return appointment
    
    # Update existing appointment details
    @staticmethod
    def update_appointment(appointment_id, updates):
        # loads appointment files, applies updates, and writes back to file.
        # 'updates' -> key-value pair (dictionary)
        file_path = f"appointments/{appointment_id}.json"

        # file does not exist -> invalid appointment ID
        if not os.path.exists(file_path):
            print("Appointment not found")
            return None
        
        # load existing appointment data
        with open (file_path, "r") as file:
            appointment = json.load(file)

        # update fields with new values
        appointment.update(updates)

        # save updated appointment back to file
        with open (file_path, "w") as file:
            json.dump(appointment, file, indent=4)
        
        print("Appointment updated successfully")
        return appointment
    
    # Completing appointments/checkout
    @staticmethod
    def checkout_patient(appointment_id):
        # marks appointment as complete and records end time
        # prevents double checkout
        file_path = f"appointments/{appointment_id}.json"

        # If file not found, appointment ID is invalid
        if not os.path.exists(file_path):
            print("Appointment not found.")
            return None

        # Load appointment details
        with open(file_path, "r") as file:
            appointment = json.load(file)

        # If already completed, no need to process again
        if appointment.get("status") == "completed":
            print("Appointment already completed.")
            return appointment

        # Mark as completed and record end time
        appointment["status"] = "completed"
        appointment["end_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save updated appointment
        with open(file_path, "w") as file:
            json.dump(appointment, file, indent=4)
            file.write("\n")

        print(f"Appointment {appointment_id} completed.")
        return appointment
    
# Does not auto-execute
if __name__ == "__main__":
   patient_id = input("Enter patient ID: ")
   reason = input("Enter reason for appointment: ")
   Appointment.new_appointment(patient_id, reason)
   



