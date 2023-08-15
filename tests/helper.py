
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Auto
def wait_and_click_element(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        element.click()
    except Exception as e:
        print("shit happen: {e}", + value)

def registration(browser, email='di@mail.ru', password= '123456', name= 'Диана'):
    wait_and_click_element(browser, *Auto.REGISTER)
    browser.find_element(*Auto.NAME).send_keys(name)
    browser.find_element(*Auto.LOGIN).send_keys(email)
    browser.find_element(*Auto.PASSWORD).send_keys(password)
    wait_and_click_element(browser, *Auto.REGISTER)
def come_in(browser, email = 'Di.Kosti@yandex.ru', password = '123456'):
    browser.find_element(*Auto.COME_LOGIN).send_keys(email)
    browser.find_element(*Auto.COME_PASSWORD).send_keys(password)