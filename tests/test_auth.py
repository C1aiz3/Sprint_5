from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from oth.locators import BurgersAuthLocators as BAL
import oth.data as data

class TestAuthPage:

    def test_login_button_main_page(self, driver):

        driver.find_element(*BAL.Main).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogBut))

        driver.find_element(*BAL.Email).send_keys(data.email)
        driver.find_element(*BAL.Password).send_keys(data.password)
        driver.find_element(*BAL.LogBut).click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((BAL.Order), 'Оформить заказ'))

        assert driver.find_element(*BAL.Order).text == 'Оформить заказ'

    def test_login_button_personal_account_page(self, driver):

        driver.find_element(*BAL.LogPerAcc).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogBut))

        driver.find_element(*BAL.Email).send_keys(data.email)
        driver.find_element(*BAL.Password).send_keys(data.password)
        driver.find_element(*BAL.LogBut).click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((BAL.Order), 'Оформить заказ'))

        assert driver.find_element(*BAL.Order).text == 'Оформить заказ'

    def test_login_button_registration_page(self, driver):

        driver.get(f'{data.URL}register')

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogRegPage))

        driver.find_element(*BAL.LogRegPage).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogBut))

        driver.find_element(*BAL.Email).send_keys(data.email)
        driver.find_element(*BAL.Password).send_keys(data.password)
        driver.find_element(*BAL.LogBut).click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((BAL.Order), 'Оформить заказ'))

        assert driver.find_element(*BAL.Order).text == 'Оформить заказ'

    def test_login_button_pass_recovery_page(self, driver):

        driver.get(f'{data.URL}forgot-password')

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogRegPage))

        driver.find_element(*BAL.LogRegPage).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogBut))

        driver.find_element(*BAL.Email).send_keys(data.email)
        driver.find_element(*BAL.Password).send_keys(data.password)
        driver.find_element(*BAL.LogBut).click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((BAL.Order), 'Оформить заказ'))

        assert driver.find_element(*BAL.Order).text == 'Оформить заказ'

