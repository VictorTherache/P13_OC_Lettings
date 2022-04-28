from django.test import TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from profiles.views import index, profile
from profiles.models import Profile


class TestProfileViewsandUrls(TestCase):
    """
    Django Test class for the lettings views and
    urls
    """

    def setUp(self):
        """
        Mocking a User profile to run the tests
        """
        self.user = User.objects.create(
            username='TestUser',
            password='123doe',
        )
        self.profile = Profile.objects.create(
            favorite_city='Montpellier',
            user_id=self.user.id
        )

    def test_profile_index_url(self):
        """
        Testing that the profile index url is valid
        """
        profile_route = reverse('profiles:index')
        self.assertEqual(resolve(profile_route).func, index)

    def test_profile_url(self):
        """
        Testing profile url with a username
        """
        profile_route = reverse('profiles:profile', kwargs={'username': 'TestUser'})
        self.assertEqual(resolve(profile_route).func, profile)

    def test_profile_index_view(self):
        """
        Testing that the profile index view is valid
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_detail_view(self):
        """
        Testing that the profile view is valid
        """
        response = self.client.get(reverse('profiles:profile', kwargs={'username': 'TestUser'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
