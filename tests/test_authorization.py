import allure 
from pages.signin_page import SigninPage
from pages.recipes_page import RecipesPage
from urls import URLs
from data import TestData


class TestAuthorizationUser:

    @allure.title('Проверка возможности авторизации')
    def test_authorization_user(self, driver):
        
        signin_page = SigninPage(driver)
        recipes_page = RecipesPage(driver)

        with allure.step('Авторизация пользователя'):
            signin_page.navigate_cite()
            signin_page.click_login_button()
            signin_page.enter_email(TestData.user_login)
            signin_page.enter_password(TestData.user_password)
            signin_page.click_authorization_button()

        
        with allure.step('Проверка перехода на главную страницу после авторизации'):
            assert recipes_page.check_current_after_authorization(URLs.RECIPES_URL), f'Переход на {URLs.RECIPES_URL} не произошел'


        with allure.step('Проверка наличия кнопки "Выйти" на странице /recipes'):
            assert recipes_page.check_logout_button(), 'Кнопка "ВЫйти" не обнаружена на странице'
        
