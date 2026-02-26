from patient import Patient
from staff import Staff

class Admin:
    def update_patient_credentials(self,patient_id,updates):
        if isinstance(patient_id, Patient):
            patient_id.credentials = updates
        else:
            raise TypeError(f"The {patient_id} does not belong to class Patient")
        
    def update_staff_credentials(self,staff_id,updates):
        if isinstance(staff_id, Staff):
            staff_id.credentials = updates
        else:
            raise TypeError(f"The {staff_id} does not belong to class Staff")   

#Test cases
""" 
#patient
peter = Patient("peter6632")

#staff
angela = Staff("angela0922")


admin = Admin()
admin.update_patient_credentials(peter,{
    "name": "Nelson"
})

admin.update_staff_credentials(angela,{
    "name": "Emily"
}) """

#print(peter.credentials)

