
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage
from locators import Auto
from helper import wait_and_click_element, come_in
class TestSection:
    def test_topping_section(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *MainPage.SING_IN)
        come_in(browser, 'Di.Kosti@yandex.ru', '123456')
        browser.find_element(*Auto.TO_COME_IN).click()
        wait_and_click_element(browser, *MainPage.TOPPING)
        browser.find_element(*MainPage.TOPPING_C)
        topping = browser.find_element(*MainPage.TOPPING_C)
        assert topping.is_displayed(), 'Выбран раздел начинки'
    def test_sauces_section(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *MainPage.SING_IN)
        come_in(browser, 'Di.Kosti@yandex.ru', '123456')
        wait_and_click_element(browser, *Auto.TO_COME_IN)
        wait_and_click_element(browser, *MainPage.SAUCES)
        browser.find_element(*MainPage.SAUCES_C)
        sauces = browser.find_element(*MainPage.SAUCES_C)
        assert sauces.is_displayed(), 'Выбран раздел соусы'


    def test_buns(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *MainPage.SING_IN)
        come_in(browser, 'Di.Kosti@yandex.ru', '123456')
        wait_and_click_element(browser, *Auto.TO_COME_IN)
        wait_and_click_element(browser, *MainPage.SAUCES)
        wait_and_click_element(browser, *MainPage.BUNS)
        browser.find_element(*MainPage.BUNS_C)
        sauces = browser.find_element(*MainPage.BUNS_C)
        assert sauces.is_displayed(), 'Выбран раздел булки'


    def test_stellar_burger(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *MainPage.SING_IN)
        browser.find_element(*Auto.COME_LOGIN).send_keys('Di.Kosti@yandex.ru')
        browser.find_element(*Auto.COME_PASSWORD).send_keys('123456')
        browser.find_element(*Auto.TO_COME_IN).click()
        wait_and_click_element(browser, *MainPage.STELLARBURGER)
        browser.find_element(*MainPage.SAUCES)
        sauces = browser.find_element(*MainPage.SAUCES)
        assert sauces.is_displayed(), 'Выбран раздел соусы, на странице есть стеллар бургер'

    def test_go_to_constructor(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *MainPage.SING_IN)
        browser.find_element(*Auto.COME_LOGIN).send_keys('Di.Kosti@yandex.ru')
        browser.find_element(*Auto.COME_PASSWORD).send_keys('123456')
        browser.find_element(*Auto.TO_COME_IN).click()
        browser.find_element(*MainPage.CONSTRUCTOR).click()
        browser.find_element(*MainPage.SAUCES)
        sauces = browser.find_element(*MainPage.SAUCES)
        assert sauces.is_displayed(), 'Выбран раздел соусы, на странице есть конструктор'