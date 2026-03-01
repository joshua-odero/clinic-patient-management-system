from unittest.mock import MagicMock
from models.doctor import Doctor


def test_doctor_initialization():
    """Doctor should initialize correctly."""
    doc = Doctor(1, "Dr Test", "test@test.com", "hash")

    assert doc.id == 1
    assert doc.name == "Dr Test"
    assert doc.email == "test@test.com"


def test_add_diagnosis_calls_db():
    """add_diagnosis should add a medical record entry."""
    doc = Doctor(1, "Dr Test", "test@test.com", "hash")

    doc._db = MagicMock()

    doc.add_diagnosis(1, "Flu")

    doc._db.add_medical_record.assert_called_once_with(
        1, "Diagnosis", "Flu"
    )


def test_prescribe_medication_calls_db():
    """prescribe_medication should add prescription record."""
    doc = Doctor(1, "Dr Test", "test@test.com", "hash")

    doc._db = MagicMock()

    doc.prescribe_medication(1, "Paracetamol")

    doc._db.add_medical_record.assert_called_once_with(
        1, "Prescription", "Paracetamol"
    )


def test_request_lab_test_calls_db():
    """request_lab_test should add lab request record."""
    doc = Doctor(1, "Dr Test", "test@test.com", "hash")

    doc._db = MagicMock()

    doc.request_lab_test(1, "Blood Test")

    doc._db.add_medical_record.assert_called_once_with(
        1, "Lab Request", "Blood Test"
    )