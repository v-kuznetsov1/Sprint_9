from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from pages.signin_page import SigninPage
from data import TestData
from urls import URLs
import config
import pytest


@pytest.fixture
def driver():
    
    if config.remote_driver:
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")
        options.set_capability("selenoid:options", {"enableVNC": True})
        options.set_capability("selenoid:options", {"enableVideo": False})

        driver = webdriver.Remote(command_executor='http://selenoid:4444/wd/hub', options=options)

    else: 
        driver = webdriver.Chrome()

    yield driver

    driver.quit()



@pytest.fixture
def login_user(driver):
    
    signin_page = SigninPage(driver)
            
    signin_page.navigate_cite()
    signin_page.click_login_button()
    signin_page.enter_email(TestData.user_login)
    signin_page.enter_password(TestData.user_password)
    signin_page.click_authorization_button()








