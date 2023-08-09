from selenium.webdriver.common.by import By
from locators import Auto
from helper import wait_and_click_element
class TestNameFieldIsEmpty:
    def test_name_is_empty(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, *Auto.REGISTER)
        browser.find_element(*Auto.COME_LOGIN).send_keys('Di.Kosti@yandex.ru')
        browser.find_element(*Auto.COME_PASSWORD).send_keys('123456')
        wait_and_click_element(browser, *Auto.REGISTER)
        browser.find_element(*Auto.REGISTER)