from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        '''Test if user with email is created successfuly'''
        email = "test@test.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email, 
            password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalizaion(self):
        '''test email is normalized before saving'''
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "test")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Throw error the invalid email is provided'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test')

    
    def test_new_super_user_email(self):
        '''Test creating super users'''
        email = "test@test.com"
        password = "test123"
        user = get_user_model().objects.create_superuser(
            email=email, 
            password=password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)