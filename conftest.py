import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import oth.data as data
from oth.locators import BurgersAuthLocators as BAL



@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.get(data.URL)
    yield chrome
    chrome.quit()

@pytest.fixture
def auth(driver):
    driver.find_element(*BAL.Main).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.Email))

    driver.find_element(*BAL.Email).send_keys(data.email)
    driver.find_element(*BAL.Password).send_keys(data.password)

    driver.find_element(*BAL.LogBut).click()



