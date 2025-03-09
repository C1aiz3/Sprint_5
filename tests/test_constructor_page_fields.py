from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from oth.locators import BurgersComponents as BC


class TestConstructorPageFields:

    def test_bread_button_constructor_page(self, auth, driver):

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BC.BreadText))

        assert driver.find_element(*BC.BreadText).text == 'Булки'

    def test_sauce_button_constructor_page(self, auth, driver):

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BC.Sauce))

        driver.find_element(*BC.Sauce).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BC.SauceText))

        assert driver.find_element(*BC.SauceText).text == 'Соусы'

    def test_topping_button_constructor_page(self, auth, driver):

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BC.Topping))

        driver.find_element(*BC.Topping).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(BC.ToppingText))

        assert driver.find_element(*BC.ToppingText).text == 'Начинки'
