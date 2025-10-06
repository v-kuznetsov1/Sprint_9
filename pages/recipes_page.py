import allure
from pages.base_page import BasePage
from locators.recipes_locators import RecipesLocators


class RecipesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Проверка перехода на страницу /recipes')
    def check_current_after_authorization(self, url):
        return self.check_current_url(url)
    
    @allure.step('Проверка наличия кнопки "Выйти на страницы /recipes')
    def check_logout_button(self):
        return self.get_text_element(RecipesLocators.LOGOUT_BUTTON)
    
    @allure.step('Клик по кнопке создания рецепта')
    def click_create_recipes_button(self):
        return self.click_to_element(RecipesLocators.CREATE_RECIPES_BUTTON)
    


    
    
    

