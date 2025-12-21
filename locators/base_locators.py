from selenium.webdriver.common.by import By


class BaseLocators:
    # Навигация
    BTN_CONSTRR = (By.XPATH, "//p[text()='Конструктор']")
    BTN_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")

    # Ингредиенты
    FLUOR_BUN = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    BUN = (By.XPATH, "//img[contains(@alt, 'Флюоресцентная булка R2-D3')]")
    SOUCE = (By.XPATH, "//img[contains(@alt, 'Соус Spicy-X')]")
    BURGER_CONSTR = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")

    # Лента заказов
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

    # Модальные окна
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    BTN_MODAL_CLOSE = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    COUNT_SPICY_X = (By.XPATH, "//p[text()='Соус Spicy-X']/ancestor::a//p[contains(@class, 'counter_counter__num')]")

    # Авторизация
    BTN_LOGIN_ACC = (By.XPATH, "//button[contains(., 'Войти в аккаунт')]")
    FIELD_EMAIL = (By.XPATH, "//input[@type='text']")
    FIELD_PASSWORD = (By.XPATH, "//input[@type='password']")
    BTN_LOGIN = (By.XPATH, "//button[contains(., 'Войти')]")