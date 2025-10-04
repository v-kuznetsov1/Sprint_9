import allure 
from pages.create_account_page import CreateAccount
from pages.signin_page import SigninPage
from urls import URLs


class TestCreateAccount:

    @allure.title('Проверка создания пользователя')
    def test_create_account(self, driver):

        signin_page = SigninPage(driver)
        create_account = CreateAccount(driver)

        signin_page.navigate_cite()
        signin_page.click_to_create_account_button()
        
        with allure.step('Создание аккаунта'):
            create_account.enter_first_name()
            create_account.enter_last_name()
            create_account.enter_username()
            create_account.enter_email()
            create_account.enter_password()
            create_account.click_to_create_account_button()

        with allure.step('Проверка редиректа на страницу /signin'):
            assert signin_page.get_expecter_url(URLs.SIGNIN_URL) == True, f'переход на {URLs.SIGNIN_URL} не произошел'


        with allure.step('Проверка отображения формы для авторизации'):
            assert 'email' in signin_page.get_attribute_email()
            assert 'password' in signin_page.get_attribute_password()
        
