import allure
from pages.base_page import BasePage
from locators.signin_locatorts import SigninPageLocarots
from urls import URLs


class SigninPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    @allure.step('Переход на сайт')
    def navigate_cite(self):
        return self.navigate(URLs.BASE_URL)
    
    @allure.step('Нажатие на кнопку "Создать аккаунт"')
    def click_to_create_account_button(self):
        return self.click_to_element(SigninPageLocarots.CREATE_ACCOUNT_BUTTON)
    

    @allure.step('Проверка ожидаемого url')
    def get_expecter_url(self, url):
        return self.check_current_url(url)
    

    @allure.step('Проверка наличия поля для ввода email')
    def get_attribute_email(self):
        return self.get_attribute_element(SigninPageLocarots.EMAIL, 'name')
    
    
    @allure.step('Проверка наличия поля для ввода пароля')
    def get_attribute_password(self):
        return self.get_attribute_element(SigninPageLocarots.PASSWORD, 'name')
    
    
    @allure.step('Клик по кнопке войти для перехода на страницу /signin')
    def click_login_button(self):
        return self.click_to_element(SigninPageLocarots.LOGIN_BUTTON)
    
    @allure.step('Ввод электронной почты')
    def enter_email(self, email):
        return self.enter_text(SigninPageLocarots.EMAIL, email)
    

    @allure.step('Ввод пароля')
    def enter_password(self, password):
        return self.enter_text(SigninPageLocarots.PASSWORD, password)
    

    @allure.step('Клик по кнопке войти для авторизации пользователя')
    def click_authorization_button(self):
        return self.click_to_element(SigninPageLocarots.AUTHORIZATION_BUTTON)
    
  