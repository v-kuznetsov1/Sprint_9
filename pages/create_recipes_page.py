from pathlib import Path
import allure
from pages.base_page import BasePage
from locators.create_recipes_locators import CreateRecipesLocators


class CreateRecipesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    @allure.step('Ввод названия рецепта')
    def enter_recipe_name(self, name):
        return self.enter_text(CreateRecipesLocators.NAME_RECIPE, name)
    
    @allure.step('Выбор тега')
    def select_tag(self):
        return self.click_to_element(CreateRecipesLocators.SELECT_TAG)
    
    @allure.step('Выбор ингредиентов')
    def select_ingredients(self, ingredient):
        ingredient = self.enter_text(CreateRecipesLocators.INGREDIENT_FIELD, ingredient)
        self.click_to_element(CreateRecipesLocators.DROPDOWN_WITH_INGREDIENTS)

    @allure.step('Ввод массы ингредиента')
    def enter_weight_ingredient(self, weight):
        return self.enter_text(CreateRecipesLocators.WEIGHT_FIELD, weight)
    
    @allure.step('Клик по кнопке "Добавить ингредиент"')
    def click_add_ingredient_button(self):
        return self.click_to_element(CreateRecipesLocators.ADD_INGREDIENT_BUTTON)
    
    @allure.step('Ввод времени приготовления')
    def enter_cooking_time(self, time):
        return self.enter_text(CreateRecipesLocators.COOKING_TIME_FIELD, time)
    
    @allure.step('Ввод описания рецепта')
    def enter_description_recipe(self, description):
        return self.enter_text(CreateRecipesLocators.DESCRIPTION_TEXTAREA, description)
    
    @allure.step('Загрузка файла')
    def upload_file_with_recipe(self, file_path):
        file_path = Path(file_path)
        file_path = str(file_path.absolute())
        self.upload_file(CreateRecipesLocators.FILE_INPUT, file_path)

    @allure.step('Клик по кнопке "Создать рецепт"')
    def click_create_recipe_button(self):
        return self.click_to_element(CreateRecipesLocators.CREATE_RECIPE_BUTTON)
    
    @allure.step('Проверка отображения карточки рецепта после создания')
    def check_recipe_card(self):
        return self.find_element_by_locator(CreateRecipesLocators.RECIPE_CARD)
    
    @allure.step('Проверка отображение названия рецепта в карточке')
    def check_name_recipe_in_card(self):
        text_element = self.get_text_element(CreateRecipesLocators.NAME_RECIPE_IN_CARD)
        return text_element

