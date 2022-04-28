from django.test import TestCase
from django.urls import resolve, reverse
from lettings.views import index, letting
from lettings.models import Address, Letting


class TestLettingsViewsandUrls(TestCase):
    """
    Django Test class for the lettings views and
    urls
    """
    def setUp(self):
        """
        Setting up mocked address and letting
        for the tests
        """
        self.mocked_address = Address.objects.create(
                number=588,
                street='Argyle Avenue',
                city='East Meadow',
                state='NY',
                zip_code=11554,
                country_iso_code='USA'
            )
        self.letting = Letting.objects.create(
            title='Underground Hygge',
            address_id=self.mocked_address.id
        )

    def test_letting_index_url(self):
        """
        Testing that the letting index url is valid
        """
        lettings_route = reverse('lettings:index')
        self.assertEqual(resolve(lettings_route).func, index)

    def test_letting_url(self):
        """
        Testing that the letting url is valid
        """
        lettings_detail_route = reverse('lettings:letting', args='1')
        self.assertEqual(resolve(lettings_detail_route).func, letting)

    def test_index_view(self):
        """
        Testing that the letting index view is valid
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_view(self):
        """
        Testing that the letting view is valid
        """
        response = self.client.get(reverse('lettings:letting', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
