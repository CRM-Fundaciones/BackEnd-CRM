import pytest
from person.models import Person, Patient, HealthInsurance

@pytest.fixture
def person1():
    return Person(name="Facundo", dni=1234, address="Obispo Trejo 123", phone_number=123456789, email="example@gmail.com")

@pytest.fixture
def person2():
    return Person(name="Valentín", dni=4321, address="San lorenzo 432", phone_number=987654321, email="example2@gmail.com")

@pytest.fixture
def person3():
    return Person(name="Diego", dni=6789, address="Laprida 24", phone_number=123459876, email="example3@gmail.com")

@pytest.fixture
def health_insurance():
    return HealthInsurance(name="Apross")

@pytest.fixture
def patient1(person1, person2, health_insurance):
    return Patient(person=person1, care_taker=person2, health_insurance=health_insurance)
