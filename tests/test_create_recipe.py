import allure 
from pages.recipes_page import RecipesPage
from pages.create_recipes_page import CreateRecipesPage
from data import TestData




class TestCreateRecipe:

    @allure.title('Проверка создания рецепта')
    def test_create_recipe(self, driver, login_user):

        recipes_page = RecipesPage(driver)
        create_recipe_page = CreateRecipesPage(driver)

        recipes_page.click_create_recipes_button()

        with allure.step('Создание рецепта'):
            create_recipe_page.enter_recipe_name(TestData.recipe_name)
            create_recipe_page.select_tag()
            create_recipe_page.select_ingredients(TestData.ingredient)
            create_recipe_page.enter_weight_ingredient(TestData.weight_ingredient)
            create_recipe_page.click_add_ingredient_button()
            create_recipe_page.enter_cooking_time(TestData.cooking_time)
            create_recipe_page.enter_description_recipe(TestData.description_recipe)
            create_recipe_page.upload_file_with_recipe(TestData.file)
            create_recipe_page.click_create_recipe_button()
        
        assert create_recipe_page.check_recipe_card(), 'Карточка рецепта не отображается'
        actual_name = create_recipe_page.check_name_recipe_in_card()
        assert actual_name == TestData.recipe_name, f'Ожидаемое название "{TestData.recipe_name}" не отображается'
   
        