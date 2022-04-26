import pytest
from lettings.models import Letting, Address


@pytest.fixture
def letting_data():
    return {'title': 'title_name'}

@pytest.fixture
def letting_data():
    return {'title': 'title_name'}

@pytest.fixture
def create_test_letting(letting_data, address_data):
    address = Address.objects.get(**address_data)
    letting = Letting.objects.create(title=letting_data.get('title'), address=address)
    return letting
