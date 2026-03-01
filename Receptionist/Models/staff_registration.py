# Staff registration
import json
import os, sys

class Staff:

    def __init__(self, name, gender, contact, staff_id):
        self.name = name
        self.gender = gender
        self.contact = contact
        self.staff_id = staff_id

    # Check if staff is already registered/ get staff data by id
    @staticmethod
    def get_staff_by_staff_id(staff_id):
        # Build file path where staff JSON is stored
        file_path = f"staff/{staff_id}.json"
        # if file does not exist, return None -> staff not found
        if not os.path.exists(file_path):
            return None
        
        # Reading JSON data from file 
        with open(file_path, "r") as file:
            staff_data = json.load(file)
            #print(staff_data)
        return staff_data # returns actual staff data (a dictionary)
    
    # Update staff details
    @staticmethod
    def update_staff_details(staff):
        # Extract staff ID from dictionary
        staff_id = staff.get("staff_id")
        file_path = f"staff/{staff_id}.json"
        # Only updates if file exists -> no file, no update
        if not os.path.exists(file_path):
            return None
        
        # Overwrite file with updated staff dictionary
        with open(file_path, "w") as file:
            json.dump(staff, file, indent=4)
        return True
    
    # Function to generate staff ids (using first name, and contact)
    @staticmethod
    def generate_staff_id(first_name, contact):
        # Convert first_name to lower
        first_name_lower = first_name.lower()
        # Convert contact to str using the str() and get the last four digits
        contact_string = str(contact)
        last_four = contact_string[-4:] # get last four digits
        # Combine or join first_name with last four digits
        staff_id = first_name_lower + last_four
        return staff_id # to be used in register_staff()
        
    # Function to register staff
    @staticmethod
    def register_staff():
        print("\nRegister new staff")

        # enter details
        name = input("Enter Staff Name: ")
        gender = input("Enter Staff Gender: ")
        contact = input("Enter Contact Number: ")
        # generate a random staff ID
        first_name = name.split()[0] 
        # split()-> splits a string into a list based on delimeters/spaces
        staff_id = Staff.generate_staff_id(first_name, contact)

        staff = {
            "name": name,
            "gender": gender,
            "contact": contact,
            "staff_id": staff_id
        }

        # Saves staff data as JSON file 
        file_path = f"staff/{staff_id}.json"

        with open(file_path, "w") as file:
            json.dump(staff, file, indent=4)
            file.write("\n")
        print("Staff registered successfully.")
        return staff # return staff data -> useful if caller needs it

# Use
# staff = Staff.register_staff()

# Does not auto-execute
if __name__ == "__main__":
    Staff.register_staff()