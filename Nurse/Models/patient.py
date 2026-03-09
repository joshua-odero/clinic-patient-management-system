class Patient:
    #Initalizes instance attributes
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.temperature = None
        self.blood_pressure = None
    #patient class method for displying patient records
    def display_info(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Temperature:", self.temperature)
        print("Blood Pressure:", self.blood_pressure)