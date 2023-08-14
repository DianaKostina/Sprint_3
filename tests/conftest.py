import pytest
from selenium import webdriver
from faker import Faker
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.fixture
def fake_data():
    return Faker()