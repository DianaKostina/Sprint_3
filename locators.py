from selenium.webdriver.common.by import By
class Auto:
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    AUTH_FORM = (By.XPATH, "//h2[contains(text(),'Вход')]")
    REGISTER = (By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]")
    RESTORE_PASSWORD = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    TO_COME_IN = (By.XPATH, "//*[contains(text(),'Войти')]")
    LOGIN = (By.XPATH, "//form//fieldset[2]//input")
    PASSWORD = (By.XPATH, "//form//fieldset[3]//input")
    COME_PASSWORD = (By.XPATH, "//form//fieldset[2]//input")
    COME_LOGIN = (By.XPATH, "//form//fieldset[1]//input")
    NAME = (By.XPATH, "//form//fieldset[1]//input")
    NOT_CORRECT_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    EXIT = (By.XPATH, "//button[contains(text(),'Выход')]")
class MainPage:
    BUNS = (By.XPATH, "//span[contains(text(),'Булки')]")
    BUNS_C = (By.XPATH, "//*[contains(@class, 'current')]//*[contains(text(), 'Булки')]")
    SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]")
    SAUCES_C = (By.XPATH, "//*[contains(@class, 'current')]//*[contains(text(), 'Соусы')]")
    TOPPING = (By.XPATH, "//span[contains(text(),'Начинки')]")
    TOPPING_C = (By.XPATH, "//*[contains(@class, 'current')]//*[contains(text(), 'Начинки')]")
    SING_IN = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    STELLARBURGER = (By.XPATH, "//nav//div//a[contains(@class, 'active')]")



