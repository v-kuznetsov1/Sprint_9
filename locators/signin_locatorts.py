from selenium.webdriver.common.by import By

class SigninPageLocarots:

    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//a[text()="Создать аккаунт"]')
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//a[@href="/signin"]')
    AUTHORIZATION_BUTTON = (By.XPATH, '//button[text()="Войти"]')

    