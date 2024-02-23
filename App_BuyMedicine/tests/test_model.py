# tests/test_models.py

import pytest
from App_BuyMedicine.models import Patient, Medicine
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

@pytest.mark.django_db
def test_patient_model():
    """
    Test cases for the Patient model with valid data.
    """
    patient = Patient.objects.create(
        name='John Doe',
        patientId='12345',
        gender='M',
        cabinNo='C123'
    )
    assert patient.name == 'John Doe'
    assert patient.patientId == '12345'
    assert patient.gender == 'M'
    assert patient.cabinNo == 'C123'

    # Test creating a patient with a duplicate patientId (should raise IntegrityError)
    with pytest.raises(IntegrityError):
        Patient.objects.create(
            name='Jane Smith',
            patientId='12345',  # This patientId is a duplicate of the one created above
            gender='F',
            cabinNo='C456'
        )

@pytest.mark.django_db
def test_medicine_model():
    """
    Test cases for the Medicine model with valid data
    """
    
    medicine = Medicine.objects.create(
        name='Paracetamol',
        inStock=True,
        price=10.50
    )
    assert medicine.name == 'Paracetamol'
    assert medicine.inStock == True
    assert medicine.price == 10.50
    
      