import pytest
from App_BuyMedicine.forms import PatientIDForm

@pytest.mark.django_db
class TestPatientIDForm:
    """
    Test cases for the PatientIDForm class.
    """
    
    def test_patient_id_form_valid(self):
        """
        Test case to validate a valid patient ID.

        Returns:
            None
        """
        form_data = {'patient_id': '1234567890'}
        form = PatientIDForm(data=form_data)
        assert form.is_valid() == True
    

    def test_patient_id_form_invalid_long_id(self):
        """
        Test case to validate an invalid patient ID that is too long.

        Returns:
            None
        """
        form_data = {'patient_id': '12345678901'}
        form = PatientIDForm(data=form_data)
        assert form.is_valid() == False
    
    def test_patient_id_form_invalid_empty_id(self):
        """
        Test case to validate an invalid empty patient ID.

        Returns:
            None
        """
        form_data = {}
        form = PatientIDForm(data=form_data)
        assert form.is_valid() == False
