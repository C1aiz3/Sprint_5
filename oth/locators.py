from selenium.webdriver.common.by import By



class BurgersRegLocators:
    Name = By.XPATH, './/fieldset[1]//input' # Поле Имя на странице регистрации
    Email = By.XPATH, './/fieldset[2]//input' # Поле Email на странице регистрации
    Password = By.XPATH, './/fieldset[3]//input' # Поле Пароль на странице регистрации
    IncorPass = By.XPATH, './/p[@class="input__error text_type_main-default"]' # Ошибка при некорректном пароле
    RegBut = By.XPATH, './/form[@class="Auth_form__3qKeq mb-20"]/button' # Кнопка Зарегистрироваться

class BurgersAuthLocators:
    Main =  By.XPATH, './/main/section/div/button' # Кнопка Войти в аккаунт на главной
    Email = By.XPATH, './/input[@name="name"]' # Поле Email на странице авторизации
    Password = By.XPATH, './/input[@name="Пароль"]' # Поле Пароль на странице авторизации
    LogBut = By.XPATH, './/form/button' # Кнопка Войти на странице авторизации
    Order = By.XPATH, './/main/section/div/button' # Кнопка Оформить заказ на главной после авторизации
    LogPerAcc = By.XPATH, './/nav/a' # Кнопка Войти в личном кабинете
    LogRegPage = By.XPATH, './/a[@href="/login"]' # Кнопка Войти на странице регистрации

class BurgersPerAccButton:
    PerAccName = By.XPATH, './/input[@value="Pavel"]' # Поле Имя в личном кабинете

class BurgerConstructorButton:
    Constructor = By.XPATH, './/div[@class="App_App__aOmNj"]//li/a[@href="/"]' # Кнопка Конструктор
    CookingText = By.XPATH, './/main//h1' # Заголовок Соберите бургер на главной
    LogoButton = By.XPATH, './/div/a' # Кнопка на лого

class BurgersExitButton:
    ExitPerAcc = By.XPATH, './/li/button' # Кнопка Выход в личном кабинете


class BurgersComponents:
    Bread = By.XPATH, './/div[@style="display: flex;"]/div[1]' # Кнопка Булки в конструкторе(по факту не нужна)
    Sauce = By.XPATH, './/div[@style="display: flex;"]/div[2]' # Кнопка Соусы в конструкторе
    Topping = By.XPATH, './/div[@style="display: flex;"]/div[3]' # Кнопка Начинки в конструкторе
    BreadText = By.XPATH, './/section/div/h2[1]' # Заголовок раздела Булки в конструкторе
    SauceText = By.XPATH, './/section/div/h2[2]' # Заголовок раздела Соусы в конструкторе
    ToppingText = By.XPATH, './/section/div/h2[3]' # Заголовок раздела Начинки в конструкторе