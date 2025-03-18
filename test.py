import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Firefox()
    browser.get("https://nexign.com/ru")
    yield browser
    browser.quit()


def test_navigation_with_clicks(browser):
    wait = WebDriverWait(browser, 10) 
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Продукты и решения']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Инструменты для ИТ-команд']"))).click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Nexign Nord"))).click()
