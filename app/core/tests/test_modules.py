from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email="test@test.com", password="testpass123"):
    '''Create a sample user'''
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        '''Test if user with email is created successfuly'''
        email = "test@test.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email, password=password)
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
            email=email, password=password)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        '''Test tag string representation'''
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Vegan"
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        '''Test the ingredient string representations'''
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name="Cucumber"
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        '''Test the recipe string representations'''
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title="Steak and mushroom sauce",
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)
