from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RecipeURLSTest(TestCase):

    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')