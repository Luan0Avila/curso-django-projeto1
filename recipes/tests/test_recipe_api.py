from unittest.mock import patch

from django.urls import reverse
from recipes.tests.test_recipe_base import RecipeMixin
from rest_framework import test


class RecipeAPIv2Test(test.APITestCase, RecipeMixin):

    def get_recipe_reverse_url(self, reverse_result=None):
        api_url = reverse_result or reverse('recipes:recipes-api-list')
        return api_url 
    
    def get_recipe_api_list(self, reverse_result=None):
        api_url = self.get_recipe_reverse_url(reverse_result)
        response = self.client.get(api_url)
        return response
    
    def get_jwt_access_token(self):
        userdata = {
            'username': 'user',
            'password': 'password'
        }
        self.make_author(username=userdata.get('username'),
                password=userdata.get('password'))
        
        response = self.client.post(reverse('recip:token_obtain_pair'), data={**userdata})
        return response.data.get('access')

    def test_recipe_api_list_returns_status_code_200(self):
        response = self.get_recipe_api_list()
        self.assertEqual(
            response.status_code,
            200
        )

    @patch('recipes.views.api.RecipeAPIv2Pagination.page_size', new=7)
    def test_recipe_api_list_loads_correct_number_of_recipes(self):
        wanted_number_of_recipes = 7
        self.make_recipe_in_batch(qtd=wanted_number_of_recipes)

        response = self.client.get(
            reverse('recipes:recipes-api-list') + '?page=1'
        )
        qtd_of_loaded_recipes = len(response.data.get('results'))

        self.assertEqual(
            wanted_number_of_recipes,
            qtd_of_loaded_recipes
        )

    def test_recipe_api_list_do_not_show_not_published_recipes(self):
        recipes = self.make_recipe_in_batch(qtd=2)
        recipe_not_published = recipes[0]
        recipe_not_published.is_published = False
        recipe_not_published.save()
        response = self.get_recipe_api_list()
        self.assertEqual(
            len(response.data.get('results')),
            1
        )
    
    @patch('recipes.views.api.RecipeAPIv2Pagination.page_size', new=10)
    def test_recipe_api_list_can_load_recipes_by_category_id(self):
        wanted_category = self.make_category(name='wanted_category')
        not_wanted_category = self.make_category(name='not wanted_category')
        recipes = self.make_recipe_in_batch(qtd=10)

        for recipe in recipes:
            recipe.category = wanted_category
            recipe.save()
        recipes[0].category = not_wanted_category
        recipes[0].save()

        api_url = reverse('recipes:recipes-api-list') + '?category_id=1'
        response = self.get_recipe_api_list(api_url)

        self.assertEqual(
            len(response.data.get('results')),
            9
        )
    
    def test_recipe_api_lits_user_must_send_jwt_token_to_create(self):
        api_url = self.get_recipe_reverse_url()
        response = self.client.post(api_url)
        self.assertEqual(
            response.status_code,
            401
        )
        
    def test_jwt_login(self):
        print(self.jwt_login())
