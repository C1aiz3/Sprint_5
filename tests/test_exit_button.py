from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from oth.locators import BurgersExitButton as BEB
from oth.locators import BurgersAuthLocators as BAL

class TestExitButton:

    def test_exit_button_from_personal_account(self, auth, driver):

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogPerAcc))

        driver.find_element(*BAL.LogPerAcc).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BEB.ExitPerAcc))

        driver.find_element(*BEB.ExitPerAcc).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogBut))

        assert driver.find_element(*BAL.LogBut).text == 'Войти'