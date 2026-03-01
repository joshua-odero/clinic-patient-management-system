import sqlite3
import os
import json


class DatabaseManager:
    """
    Handles database connection and CRUD operations.
    Includes medical history support.
    """

    def __init__(self, db_path="data/clinic.db"):
        self.db_path = db_path
        self._initialize_database()
        self._load_dummy_patients()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    # -----------------------------
    # CREATE TABLES
    # -----------------------------
    def _initialize_database(self):
        os.makedirs("data", exist_ok=True)

        conn = self._connect()
        cursor = conn.cursor()

        # Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password_hash TEXT,
            role TEXT
        )
        """)

        # Patients table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id TEXT PRIMARY KEY,
            name TEXT,
            age INTEGER,
            contact TEXT,
            gender TEXT,
            status TEXT
        )
        """)

        # Medical history table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS medical_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            record_type TEXT,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(patient_id) REFERENCES patients(id)
        )
        """)

        conn.commit()
        conn.close()

    # -----------------------------
    # LOAD DUMMY PATIENTS
    # -----------------------------
    def _load_dummy_patients(self):
        """Loads patients from patients.json if DB is empty."""
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM patients")
        count = cursor.fetchone()[0]

        if count == 0:
            try:
                with open("patients.json", "r") as file:
                    patients = json.load(file)

                for p in patients:
                    cursor.execute("""
                        INSERT INTO patients (id, name, age, contact, gender, status)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (
                        p["id"],
                        p["name"],
                        p["age"],
                        p["contact"],
                        p["gender"],
                        "Admitted"
                    ))

                conn.commit()
            except Exception as e:
                print("Error loading dummy patients:", e)

        conn.close()

    # -----------------------------
    # USER METHODS
    # -----------------------------
    def create_user(self, name, email, password_hash, role):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, email, password_hash, role)
            VALUES (?, ?, ?, ?)
        """, (name, email, password_hash, role))
        conn.commit()
        conn.close()

    def get_user_by_email(self, email):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()
        conn.close()
        return user

    # -----------------------------
    # MEDICAL RECORD METHODS
    # -----------------------------
    def add_medical_record(self, patient_id, record_type, description):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO medical_records (patient_id, record_type, description)
            VALUES (?, ?, ?)
        """, (patient_id, record_type, description))
        conn.commit()
        conn.close()

    def get_patient_full_record(self, patient_id):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
        patient = cursor.fetchone()

        cursor.execute("""
            SELECT record_type, description, created_at
            FROM medical_records
            WHERE patient_id=?
            ORDER BY created_at ASC
        """, (patient_id,))
        records = cursor.fetchall()

        conn.close()
        return patient, records