import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.base_page import BasePage
import allure
from url import Url
from locators.base_locators import BaseLocators


class MainPage(BasePage):
    @allure.step('Перейти в конструктор')
    def go_to_constructor(self):
        self.open_page(Url.url_feed)
        super().go_to_constructor()

    @allure.step('Перейти в ленту заказов')
    def go_to_feed(self):
        self.open_page(Url.url_page)
        super().go_to_feed()

    @allure.step('Открыть модальное окно ингредиента')
    def open_ingredient_modal(self):
        self.click(BaseLocators.FLUOR_BUN)
        self.wait_for_element(BaseLocators.MODAL)

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.click(BaseLocators.BTN_MODAL_CLOSE)

    @allure.step('Добавить булку в конструктор')
    def add_bun(self):
        self.drag_and_drop(BaseLocators.BUN, BaseLocators.BURGER_CONSTR)

    @allure.step('Добавить соус в конструктор')
    def add_sauce(self):
        self.drag_and_drop(BaseLocators.SOUCE, BaseLocators.BURGER_CONSTR)

    @allure.step('Получить счётчик соуса')
    def get_sauce_counter(self):
        return self.get_text(BaseLocators.COUNT_SPICY_X)