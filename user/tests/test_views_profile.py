from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from user.models.User import Profile


class ProfileModelTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='unittest', password='123456')
        self.client = Client()
        self.url = reverse('get_user_profile')

    def test_status_code_returns_200(self):
        response = self.client.get(f'{self.url}?username=unittest')
        self.assertEqual(response.status_code, 200)

    def test_status_code_returns_404(self):
        response = self.client.get(f'{self.url}?username=unittest1')
        self.assertEqual(response.status_code, 404)

    def test_template_used_is_profile(self):
        response = self.client.get(f'{self.url}?username=unittest')
        self.assertTemplateUsed(response, 'profile.html')
