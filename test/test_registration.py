from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from oth.locators import BurgersRegLocators as BRL
import oth.data as data


class TestRegistration:

    def test_reg_page_fill_fields(self, driver):
        driver.get(f'{data.URL}register')
        driver.find_element(*BRL.Name).send_keys(data.name)
        driver.find_element(*BRL.Email).send_keys(data.email)
        driver.find_element(*BRL.Password).send_keys(data.password)

        assert len(driver.find_element(*BRL.Name).get_attribute('value')) > 0
        assert driver.find_element(*BRL.Email).get_attribute('value') == data.email
        assert len(driver.find_element(*BRL.Password).get_attribute('value')) >= 6

    def test_incorrect_password(self, driver):
        driver.get(f'{data.URL}register')
        driver.find_element(*BRL.Name).send_keys(data.name)
        driver.find_element(*BRL.Email).send_keys(data.email)
        driver.find_element(*BRL.Password).send_keys('123')

        driver.find_element(*BRL.RegBut).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((BRL.IncorPass)))

        assert driver.find_element(*BRL.IncorPass).text == 'Некорректный пароль'