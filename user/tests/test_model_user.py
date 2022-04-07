from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from user.models.User import Profile


class UserModelTestCase(TestCase):

    def setUp(self):
        try:
            with transaction.atomic():
                user = User.objects.create(username='unittest', password='123456')
                profile = Profile.objects.get(user=user)
                profile.save()

        except IntegrityError as error:
            print(f'Error while creating user. Error: {error}')

        self.client = Client()

    def test_user_was_successfully_created_in_database(self):
        user = User.objects.first()
        self.assertEqual(user.__str__(), 'unittest')

    def test_user_profile_was_successfully_created_in_database(self):
        user = User.objects.first()
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.__str__(), user.username)
        self.assertIsNotNone(profile)