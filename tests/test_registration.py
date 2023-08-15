from selenium import webdriver
from helper import wait_and_click_element
from helper import registration, come_in
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import Auto
fake = Faker()
class TestRegistration:
    def test_not_correct_pass(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        registration(browser, 'dia@mail.ru', '1234', 'Диана')
        error_message = browser.find_element(*Auto.NOT_CORRECT_PASSWORD)
        assert error_message.is_displayed(), "Error message is not displayed"

    def test_name_is_empty(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, *Auto.REGISTER)
        registration(browser, 'dia@mail.ru', '123456', '')
        wait_and_click_element(browser, *Auto.REGISTER)
        name_is_empty = browser.find_element(*Auto.REGISTER)
        assert name_is_empty.is_displayed(), "Пустое поле Имя"

    def test_successful_registration(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        email = fake.email()
        name = fake.name()
        print(email)
        password = fake.password(length=7)
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, *Auto.REGISTER)
        registration(browser, email, password, name)
        wait_and_click_element(browser, *Auto.REGISTER)
        WebDriverWait(browser, 10000).until(EC.presence_of_element_located((By.XPATH, "//form//fieldset[1]//input")))
        wait_and_click_element(browser, *Auto.TO_COME_IN)
        come_in(browser, email, password)
        wait_and_click_element(browser, *Auto.TO_COME_IN)
        wait_and_click_element(browser, *Auto.PERSONAL_ACCOUNT)
        wait_and_click_element(browser, By.XPATH, "//input[@value='" + email + "']")
        successful_registration = browser.find_element(By.XPATH, "//input[@value='" + email + "']")
        assert successful_registration.is_displayed(), "Поле логин соотвествует введенному значению"


