
import allure
from pages.base_page import BasePage
from locators.create_account_locators import CreateAccountLocators
from helpers import GenerateUserData
from urls import URLs


class CreateAccount(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    

    @allure.step('Ввод имени')
    def enter_first_name(self):
        return self.enter_text(CreateAccountLocators.FIRST_NAME, GenerateUserData.first_name)
    

    @allure.step('Ввод фамилии')
    def enter_last_name(self):
        return self.enter_text(CreateAccountLocators.LAST_NAME, GenerateUserData.last_name)
    
    
    @allure.step('Ввод логина')
    def enter_username(self):
        return self.enter_text(CreateAccountLocators.USERNAME, GenerateUserData.user_name)
    
    
    @allure.step('Ввод email')
    def enter_email(self):
        return self.enter_text(CreateAccountLocators.EMAIL, GenerateUserData.email)
    

    @allure.step('Ввод пароля')
    def enter_password(self):
        return self.enter_text(CreateAccountLocators.PASSWORD, GenerateUserData.password)
    
    @allure.step('Клик по кнопке "Создать аккаунт" после заполнения данных пользователя')
    def click_to_create_account_button(self):
        return self.click_to_element(CreateAccountLocators.CREATE_ACCOUNT_BUTTON)
    


    
