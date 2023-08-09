from selenium import webdriver
from locators import Auto
from helper import wait_and_click_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestNotCorrectPassword:
    def test_not_correct_pass(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, *Auto.REGISTER)
        browser.find_element(*Auto.NAME).send_keys('Диана')
        browser.find_element(*Auto.LOGIN).send_keys('Di.Kosti@yandex.ru')
        browser.find_element(*Auto.PASSWORD).send_keys('1234')
        wait_and_click_element(browser, *Auto.REGISTER)
        browser.find_element(*Auto.NOT_CORRECT_PASSWORD).click()
