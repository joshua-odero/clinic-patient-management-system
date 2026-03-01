import json
import re

class Staff:
    #initialize instance attributes
    def __init__(self,staff_id):
        self._staff_id = None #initialize empty staff_member id (instance attribute) => string
        self._credentials = {} #initialize empty credentials (instance attribute)=> dictionary

        self.staff_id = staff_id #use @property setter to validate instance attribute

    """ #use @static method to define reusable instance methods
    eg. reading json file """
    @staticmethod 
    def generate_dict_data():
        with open("../data/staff.json", "r") as file:
            staff_data = json.load(file)
        return staff_data

    #control the staff_id instance attribute with @property decorator
    # get instance's staff_id by @property getter => self.staff_id
    # set instance's staff_id by #property setter => self. staff_id = <some value>
    @property
    def staff_id(self):
        return self._staff_id
    
    @staff_id.setter
    def staff_id(self,search_patient_id):
        #check if staff_member id exists in the json file containing the patients data
        staff_data = self.generate_dict_data()
        
        found_staff = None

        #Loop through the patients data to ensure staff_member id exists
        for staff_member in staff_data:
            if staff_member["id"] == search_patient_id:
                found_staff = staff_member
                break #get out of the loop
        
        if found_staff:
            self._staff_id = found_staff["id"]
            print(f"\nstaff_member of staff_member id:{search_patient_id} can be found in the system")
        else:
            print(f"\nstaff_member of staff_member id:{search_patient_id} cannot be found in the system")

    #control the credentials instance attribute with @property decorator
    # get instance's credentials by @property getter => self.credentials
    # set instance's credentials by #property setter => self. credentials = <some value>
    @property #getter
    def credentials(self):
        return self._credentials

    @credentials.setter #setter
    def credentials(self,credentials_update):

        #Now search for staff_id of the staff_member in the system
        staff_data = self.generate_dict_data() #implementation of @static method to create reusable code
        found_staff = None #Can be reassigned and used for conditional statements

        for staff_member in staff_data:
            if staff_member["id"] == self.staff_id:
                found_staff = staff_member
                break #exit the loop if found
            
        if found_staff:
            #Loop through a list of tuples
            #.items() is used to convert a dict into a list of tuples
            for key,value in credentials_update.items(): 
                if key == "name": #check what the key is on each iteration
                    if not isinstance(value,str):
                        print("\nName should be a string to update")
                        continue #go to the next iteration
                    else:
                        self.credentials["name"] = value
                        found_staff["name"] = value
                
                if key == "contact":#check what the key is on each iteration
                    if not re.match("^\\d{10}$",value): #check if value is a string of 10 digits only
                        print("\nContact should be 10 digits only to update")
                        continue #go to the next iteration
                    else:
                        self.credentials["contact"] = value
                        found_staff["contact"] = value

                if key == "gender":#check what the key is on each iteration
                    if value == "M" or value == "F":
                        self.credentials["gender"] = value
                        found_staff["gender"] = value
                    else:
                        print(f"\nInvalid. Enter M or F to update")
                        continue #go to the next iteration
                if key == "role": #check what the key is on each iteration
                    if not isinstance(value,str):
                        print("\nRole should be a string to update")
                        continue #go to the next iteration
                    else:
                        self.credentials["name"] = value
                        found_staff["name"] = value

            print(f"\nThe updated data for id:{self.staff_id} is {found_staff}")