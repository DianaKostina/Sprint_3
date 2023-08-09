#соусы
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Auto, MainPage
from helper import wait_and_click_element
class TestSaucesSection:
    def test_sauces_section(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *MainPage.SING_IN)
        browser.find_element(*Auto.COME_LOGIN).send_keys('Di.Kosti@yandex.ru')
        browser.find_element(*Auto.COME_PASSWORD).send_keys('123456')
        wait_and_click_element(browser, *Auto.TO_COME_IN)
        wait_and_click_element(browser, *MainPage.SAUCES)
