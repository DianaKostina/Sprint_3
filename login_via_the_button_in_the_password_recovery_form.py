#вход через кнопку в форме восстановления пароля.
from locators import Auto
from helper import wait_and_click_element
class TestRecoveryForm:
    def test_recovery_form(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, *Auto.RESTORE_PASSWORD)
        browser.find_element(*Auto.TO_COME_IN).click()
        browser.find_element(*Auto.COME_LOGIN).send_keys('Di.Kosti@yandex.ru')
        browser.find_element(*Auto.COME_PASSWORD).send_keys('123456')
        wait_and_click_element(browser, *Auto.TO_COME_IN)
