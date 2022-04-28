from django.test import TestCase
from django.urls import resolve, reverse
from oc_lettings_site.views import index


class TestOcLettingsViewsandUrls(TestCase):
    """
    Django Test class for the oc-lettings views
    and urls
    """

    def test_oc_index_url(self):
        """
        Testing that the index url is valid
        """
        oc_route = reverse('index')
        self.assertEqual(resolve(oc_route).func, index)

    def test_oc_view(self):
        """
        Testing that the homepage view is valid
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')
