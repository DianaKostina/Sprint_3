#вход через кнопку в форме регистрации, //a[contains(text(),'Войти')]
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Auto
from helper import wait_and_click_element
class TestRegistrationForm:
    def test_registration_form(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, *Auto.REGISTER)
        browser.find_element(*Auto.TO_COME_IN).click()
        browser.find_element(*Auto.COME_LOGIN).send_keys('Di.Kosti@yandex.ru')
        browser.find_element(*Auto.COME_PASSWORD).send_keys('123456')
        wait_and_click_element(browser, *Auto.TO_COME_IN)