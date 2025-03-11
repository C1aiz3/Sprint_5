from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from oth.locators import BurgersAuthLocators as BAL
from oth.locators import BurgerConstructorButton as BCB


class TestConstructorButton:

    def test_constructor_button_from_personal_account(self, auth, driver):

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogPerAcc))

        driver.find_element(*BAL.LogPerAcc).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BCB.Constructor))

        driver.find_element(*BCB.Constructor).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.Order))

        assert driver.find_element(*BCB.CookingText).text == 'Соберите бургер'


    def test_logo_button_constructor_page(self, auth, driver):

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.LogPerAcc))

        driver.find_element(*BAL.LogPerAcc).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BCB.LogoButton))

        driver.find_element(*BCB.LogoButton).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BAL.Order))

        assert driver.find_element(*BCB.CookingText).text == 'Соберите бургер'