import pytest
from lettings.models import Letting, Address


@pytest.fixture
def address_data():
    return {'number': '1', 'street': 'street_name', 'city': 'city_name', 'state': 'state_name',
            'zip_code': '1', 'country_iso_code': 'iso_code'}


@pytest.fixture
def letting_data():
    return {'title': 'title_name'}


@pytest.fixture
def create_test_address(address_data):
    address = Address.objects.create(**address_data)
    return address


@pytest.fixture
def create_test_letting(letting_data, address_data):
    address = Address.objects.get(**address_data)
    letting = Letting.objects.create(title=letting_data.get('title'), address=address)
    return letting
