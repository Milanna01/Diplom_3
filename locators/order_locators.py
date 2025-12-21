import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.common.by import By

# Теперь импортируем BaseLocators
from locators.base_locators import BaseLocators

class OrderFeedLocators(BaseLocators):
    # Счётчики
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")

    # Раздел "В работе"
    ORDERS_IN_PROGRESS = (By.XPATH, "(//li[@class='text text_type_digits-default mb-2'])")

    # Модальное окно заказа
    ID_ORDER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]")
    BTN_CLOSE_MODAL = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    ORDER_OVERLAIN_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")

    # Кнопка заказа
    BTN_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")