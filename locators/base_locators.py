from selenium.webdriver.common.by import By


class BaseLocators:
    # Навигация (общие для всех страниц)
    BTN_CONSTRR = (By.XPATH, "//p[text()='Конструктор']")
    BTN_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    
    # Лента заказов (заголовок может быть на нескольких страницах)
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Модальные окна (общие для всех страниц)
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    BTN_MODAL_CLOSE = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    ID_ORDER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]")
    
    # Авторизация (общие для всех страниц с авторизацией)
    BTN_LOGIN_ACC = (By.XPATH, "//button[contains(., 'Войти в аккаунт')]")
    FIELD_EMAIL = (By.XPATH, "//input[@type='text']")
    FIELD_PASSWORD = (By.XPATH, "//input[@type='password']")
    BTN_LOGIN = (By.XPATH, "//button[contains(., 'Войти')]")