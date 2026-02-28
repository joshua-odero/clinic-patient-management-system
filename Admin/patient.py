import json
import re

class Patient:
    #initialize instance attributes
    def __init__(self,patient_id):
        self._patient_id = None #initialize empty patient id (instance attribute) => string
        self._credentials = {} #initialize empty credentials (instance attribute)=> dictionary

        self.patient_id = patient_id #use @property setter to validate instance attribute

    """ #use @static method to define reusable instance methods
    eg. reading json file """
    @staticmethod 
    def generate_dict_data():
        with open("patients.json", "r") as file:
            patients_data = json.load(file)
        return patients_data 

    #control the patient_id instance attribute with @property decorator
    # get instance's patient_id by @property getter => self.patient_id
    # set instance's patient_id by #property setter => self. patient_id = <some value>
    @property
    def patient_id(self):
        return self._patient_id
    
    @patient_id.setter
    def patient_id(self,search_patient_id):
        #check if patient id exists in the json file containing the patients data
        patients_data = self.generate_dict_data()
        
        found_patient = None

        #Loop through the patients data to ensure patient id exists
        for patient in patients_data:
            if patient["id"] == search_patient_id:
                found_patient = patient
                break #get out of the loop
        
        if found_patient:
            self._patient_id = found_patient["id"]
            print(f"\nPatient of patient id:{search_patient_id} can be found in the system")
        else:
            print(f"\nPatient of patient id:{search_patient_id} cannot be found in the system")

    #control the credentials instance attribute with @property decorator
    # get instance's credentials by @property getter => self.credentials
    # set instance's credentials by #property setter => self. credentials = <some value>
    @property #getter
    def credentials(self):
        return self._credentials

    @credentials.setter #setter
    def credentials(self,credentials_update):

        #Now search for patient_id of the patient in the system
        patients_data = self.generate_dict_data() #implementation of @static method to create reusable code
        found_patient = None #Can be reassigned and used for conditional statements

        for patient in patients_data:
            if patient["id"] == self.patient_id:
                found_patient = patient
                break #exit the loop if found
            
        if found_patient:
            #Loop through a list of tuples
            #.items() is used to convert a dict into a list of tuples
            for key,value in credentials_update.items(): 
                if key == "name": #check what the key is on each iteration
                    if not isinstance(value,str):
                        print("\nName should be a string to update")
                        continue #go to the next iteration
                    else:
                        self.credentials["name"] = value
                        found_patient["name"] = value

                if key == "age":#check what the key is on each iteration
                    if not isinstance(value,int):
                        print("\nAge should be an integer to update")
                        continue #go to the next iteration
                    else:
                        self.credentials["age"] = value
                        found_patient["age"] = value
                
                if key == "contact":#check what the key is on each iteration
                    if not re.match("^\\d{10}$",value): #check if value is a string of 10 digits only
                        print("\nContact should be 10 digits only to update")
                        continue #go to the next iteration
                    else:
                        self.credentials["contact"] = value
                        found_patient["contact"] = value

                if key == "gender":#check what the key is on each iteration
                    if value == "M" or value == "F":
                        self.credentials["gender"] = value
                        found_patient["gender"] = value
                    else:
                        print(f"\nInvalid. Enter M or F to update")
                        continue #go to the next iteration

            print(f"\nThe updated data for id:{self.patient_id} is {found_patient}")
        