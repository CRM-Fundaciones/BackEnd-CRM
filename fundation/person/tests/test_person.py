import pytest

from person.models import Patient

@pytest.mark.django_db
class TestPersonModel:

    def test_patient_with_one_person(self, person1, person2):
        pat = Patient(person=person1, care_taker=person2)

        assert pat.person == person1
        assert pat.care_taker == person2
        assert pat.person != pat.care_taker

    def test_patient_with_two_persons(self, person1, person2, person3):
        pat1 = Patient(person=person1, care_taker=person2)
        pat2 = Patient(person=person3, care_taker=person2)

        assert pat1.person.name == person1.name
        assert pat2.person.name == person3.name
        assert pat1.care_taker == person2
        assert pat2.care_taker == person2
        assert pat1.person != pat1.care_taker 
        assert pat2.person != pat2.care_taker 
        assert pat1.care_taker == pat2.care_taker