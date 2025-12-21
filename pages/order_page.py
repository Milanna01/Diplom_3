import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.base_page import BasePage
import allure
from locators.order_locators import OrderFeedLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()

    @allure.step('Добавить ингредиенты в конструктор')
    def add_ingredients(self):
        self.drag_and_drop(self.locators.BUN, self.locators.BURGER_CONSTR)
        self.drag_and_drop(self.locators.SOUCE, self.locators.BURGER_CONSTR)

    @allure.step('Оформить заказ')
    def place_order(self):
        self.click(self.locators.BTN_ORDER)

    @allure.step('Закрыть модальное окно заказа')
    def close_order_modal(self):
        self.click(self.locators.BTN_CLOSE_MODAL)
        self.wait_for_element_not_visible(self.locators.ORDER_OVERLAIN_MODAL)

    @allure.step('Получить номера заказов в работе')
    def get_orders_in_progress(self):
        return self.get_text(self.locators.ORDERS_IN_PROGRESS)

    @allure.step('Получить общий счётчик заказов')
    def get_total_count(self):
        return self.get_text(self.locators.TOTAL_ORDERS_COUNT)

    @allure.step('Получить счётчик заказов за сегодня')
    def get_today_count(self):
        return self.get_text(self.locators.TODAY_ORDERS_COUNT)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.get_text(self.locators.ID_ORDER)