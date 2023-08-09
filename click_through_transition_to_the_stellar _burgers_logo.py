from locators import MainPage
from locators import Auto
from helper import wait_and_click_element
class TestStellarBurger:
    def test_stellar_burger(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *MainPage.SING_IN)
        browser.find_element(*Auto.COME_LOGIN).send_keys('Di.Kosti@yandex.ru')
        browser.find_element(*Auto.COME_PASSWORD).send_keys('123456')
        browser.find_element(*Auto.TO_COME_IN).click()
        wait_and_click_element(browser, *MainPage.STELLARBURGER)