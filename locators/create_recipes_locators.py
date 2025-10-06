from selenium.webdriver.common.by import By


class CreateRecipesLocators:
    
    NAME_RECIPE = (By.CLASS_NAME, 'styles_inputField__3eqTj')
    SELECT_TAG = (By.XPATH, '//button[contains(@class, "styles_checkbox__1WBUC")]')
    INGREDIENT_FIELD = (By.CLASS_NAME, 'styles_ingredientsInput__1zzql')
    DROPDOWN_WITH_INGREDIENTS = (By.XPATH, '//div[@class="styles_container__3ukwm"]/div[text()="облепиха"]')
    WEIGHT_FIELD = (By.CSS_SELECTOR, 'input.styles_inputField__3eqTj.styles_ingredientsAmountValue__2matT')
    ADD_INGREDIENT_BUTTON = (By.XPATH, '//div[@class="styles_ingredientAdd__3fc32" and text()="Добавить ингредиент"]')
    COOKING_TIME_FIELD = (By.XPATH, '//div[contains(@class, "styles_input__2Dg_j") and '
    'contains(@class, "styles_ingredientsTimeInput__3oqdd")]//input[@type="text"]')
    DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, 'textarea.styles_textareaField__1wfhC')
    FILE_INPUT = (By.CSS_SELECTOR, 'input.styles_fileInput__3HjP3[type="file"]')
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'styles_single-card__info__2_cny')]")
    NAME_RECIPE_IN_CARD = (By.CSS_SELECTOR, "h1.styles_single-card__title__2QMPq")
    