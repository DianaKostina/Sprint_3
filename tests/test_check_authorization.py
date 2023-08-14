from locators import Auto, MainPage
from helper import wait_and_click_element, come_in
class TestEntrance:
    def test_registration_form(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, *Auto.REGISTER)
        browser.find_element(*Auto.TO_COME_IN).click()
        come_in(browser, 'Di.Kosti@yandex.ru', '123456')
        wait_and_click_element(browser, *Auto.TO_COME_IN)
        wait_and_click_element(browser, *MainPage.SAUCES)
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_recovery_form(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, *Auto.RESTORE_PASSWORD)
        browser.find_element(*Auto.TO_COME_IN).click()
        come_in(browser, 'Di.Kosti@yandex.ru', '123456')
        wait_and_click_element(browser, *Auto.TO_COME_IN)
        wait_and_click_element(browser, *MainPage.SAUCES)
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_log_main_page(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *MainPage.SING_IN)
        come_in(browser, 'Di.Kosti@yandex.ru', '123456')
        wait_and_click_element(browser, *Auto.TO_COME_IN)
        wait_and_click_element(browser, *MainPage.SAUCES)
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_your_account(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, *Auto.REGISTER)
        browser.find_element(*Auto.TO_COME_IN).click()
        come_in(browser, 'Di.Kosti@yandex.ru', '123456')
        wait_and_click_element(browser, *Auto.TO_COME_IN)
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, *Auto.EXIT)
        wait_and_click_element(browser, *Auto.TO_COME_IN)
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login'



