from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import URLs


class BasePage():

    def __init__(self, driver):
        self.driver = driver 


    def navigate(self, url):
        return self.driver.get(url)
    

    def find_element_by_locator(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    

    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()
        return element
    

    def enter_text(self, locator, enter_text):
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        field.send_keys(enter_text)
        return field
    

    def check_current_url(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))
    

    def get_attribute_element(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)
    

    def get_text_element(self, locator):
        text_element = self.driver.find_element(*locator)
        return text_element.text
    

    def upload_file(self, input_locator, file_path):
        input = self.driver.find_element(*input_locator)
        print(file_path)
        input.send_keys(file_path)