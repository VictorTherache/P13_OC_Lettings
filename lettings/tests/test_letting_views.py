from django.test import SimpleTestCase
from django.urls import resolve, reverse
from lettings.views import index, letting
from lettings.models import Address, Letting

class TestLettingsViewsandUrls(SimpleTestCase):


    def setUp(self):
        self.mocked_address = Address.objects.create(
                number=7217,
                street='Bedford Street',
                city='Brunswick',
                state='GA',
                zip_code=31525,
                country_iso_code='USA'
            )
        self.letting = Letting.objects.create(
            title='Joshua Tree Green Haus /w Hot Tub',
            address_id=self.mocked_address.id
        )
    def test_index_url(self):
        url = reverse('lettings:index')
        self.assertEqual(resolve(url).func, index)

    def test_letting_url(self):
        url = reverse('lettings:letting', args='1')
        self.assertEqual(resolve(url).func, letting)
