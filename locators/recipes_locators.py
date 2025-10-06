from selenium.webdriver.common.by import By

class RecipesLocators:

    LOGOUT_BUTTON = (By.XPATH, '//a[text()="Выход"]')
    CREATE_RECIPES_BUTTON = (By.XPATH, '//a[@href="/recipes/create"]')