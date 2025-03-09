from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from oth.locators import BurgersAuthLocators as BAL
from oth.locators import BurgersPerAccButton as BPAB


class TestPersonalAccountButton:

    def test_personal_account_button(self, driver, auth):

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogPerAcc))

        driver.find_element(*BAL.LogPerAcc).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BPAB.PerAccName))

        assert driver.find_element(*BPAB.PerAccName).get_attribute('value') == "Pavel"


