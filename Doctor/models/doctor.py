from models.user import User
from database.db_manager import DatabaseManager


class Doctor(User):
    """
    Doctor inherits from User.
    Adds medical functionality specific to doctors.
    """

    def __init__(self, id, name, email, password_hash):
        super().__init__(id, name, email, password_hash, role="Doctor")
        self._db = DatabaseManager()

    # -----------------------------------
    # VIEW FULL PATIENT RECORD
    # -----------------------------------
    def view_patient_record(self, patient_id):
        """
        Returns patient details and their medical history.
        """
        return self._db.get_patient_full_record(patient_id)

    # -----------------------------------
    # ADD DIAGNOSIS
    # -----------------------------------
    def add_diagnosis(self, patient_id, diagnosis):
        """
        Adds diagnosis to patient medical record.
        """
        self._db.add_medical_record(patient_id, "Diagnosis", diagnosis)

    # -----------------------------------
    # PRESCRIBE MEDICATION
    # -----------------------------------
    def prescribe_medication(self, patient_id, medication):
        """
        Adds prescription record.
        """
        self._db.add_medical_record(patient_id, "Prescription", medication)

    # -----------------------------------
    # REQUEST LAB TEST
    # -----------------------------------
    def request_lab_test(self, patient_id, test):
        """
        Adds lab test request to medical history.
        """
        self._db.add_medical_record(patient_id, "Lab Request", test)

    # -----------------------------------
    # REVIEW LAB RESULTS
    # -----------------------------------
    def review_lab_results(self, patient_id, result):
        """
        Adds lab result to patient history.
        """
        self._db.add_medical_record(patient_id, "Lab Result", result)

    # -----------------------------------
    # UPDATE TREATMENT PLAN
    # -----------------------------------
    def update_treatment(self, patient_id, treatment):
        """
        Updates treatment plan.
        """
        self._db.add_medical_record(patient_id, "Treatment Plan", treatment)

    # -----------------------------------
    # ADMIT OR DISCHARGE PATIENT
    # -----------------------------------
    def update_status(self, patient_id, status):
        """
        Updates patient admission status.
        """
        self._db.add_medical_record(patient_id, "Status Update", status)