from selenium.webdriver.common.by import By


class OrderLocators:
    # Счётчики (специфичные для страницы заказов)
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")

    # Раздел "В работе"
    ORDERS_IN_PROGRESS = (By.XPATH, "(//li[@class='text text_type_digits-default mb-2'])")

    # Модальное окно заказа в BaseLocators так как может использоваться на разных страницах
    # ID_ORDER удален отсюда, он будет в BaseLocators