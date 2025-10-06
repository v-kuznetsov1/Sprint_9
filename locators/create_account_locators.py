
from selenium.webdriver.common.by import By

class CreateAccountLocators:

    FIRST_NAME = (By.NAME, 'first_name')
    LAST_NAME = (By.NAME, 'last_name')
    USERNAME = (By.NAME, 'username')
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Создать аккаунт"]')

    
    