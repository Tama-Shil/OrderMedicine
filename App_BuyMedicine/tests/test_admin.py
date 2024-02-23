import pytest
from django.contrib.admin.sites import AdminSite
from App_BuyMedicine.admin import PatientAdmin, MedicineAdmin
from App_BuyMedicine.models import Patient, Medicine

@pytest.fixture
def admin_site():
    """Fixture for creating an instance of the Django AdminSite."""
    return AdminSite()

@pytest.fixture
def patient_admin(admin_site):
    """
    Fixture for creating an instance of the PatientAdmin.

    Args:
        admin_site (AdminSite): Instance of the Django AdminSite.

    Returns:
        PatientAdmin: Instance of the PatientAdmin.
    """
    return PatientAdmin(Patient, admin_site)

@pytest.fixture
def medicine_admin(admin_site):
    """
    Fixture for creating an instance of the MedicineAdmin.

    Args:
        admin_site (AdminSite): Instance of the Django AdminSite.

    Returns:
        MedicineAdmin: Instance of the MedicineAdmin.
    """
    return MedicineAdmin(Medicine, admin_site)

def test_patient_display(patient_admin):
    """
    Test case for checking the list display attributes of PatientAdmin.

    Args:
        patient_admin (PatientAdmin): Instance of the PatientAdmin.

    Returns:
        None
    """
    assert list(patient_admin.list_display) == ['name', 'patientId', 'gender', 'cabinNo']

def test_medicine_display(medicine_admin):
    """
    Test case for checking the list display attributes of MedicineAdmin.

    Args:
        medicine_admin (MedicineAdmin): Instance of the MedicineAdmin.

    Returns:
        None
    """
    assert list(medicine_admin.list_display) == ['name', 'inStock', 'price']
