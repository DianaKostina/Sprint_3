
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage
from locators import Auto
from helper import wait_and_click_element
class TestToppingSection:
    def test_topping_section(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *MainPage.SING_IN)
        browser.find_element(*Auto.COME_LOGIN).send_keys('Di.Kosti@yandex.ru')
        browser.find_element(*Auto.COME_PASSWORD).send_keys('123456')
        browser.find_element(*Auto.TO_COME_IN).click()
        wait_and_click_element(browser, *MainPage.TOPPING)
