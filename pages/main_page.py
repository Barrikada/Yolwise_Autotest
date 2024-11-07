from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from pages.locators import AviaSearchLocators


class AviaPage(BasePage):
    def enter_departure_city(self):
        """Вводим город отправления."""
        try:
            departure_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(AviaSearchLocators.DEPARTURE_CITY_INPUT)
            )
            departure_input.clear()  # Очищаем поле для ввода города отправления
        except TimeoutException:
            print("Не удалось найти поле для ввода города отправления")

    def select_departure_city_from_autocomplete(self):
        """Выбор первого города из автозаполнения для отправления."""
        try:
            departure_auto_complete = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(AviaSearchLocators.DEPARTURE_AUTOCOMPLIT_FIRST)
            )
            departure_auto_complete.click()
        except TimeoutException:
            print("Не удалось выбрать первый город отправления из автозаполнения")

    def enter_arrival_city(self):
        """Вводим город прибытия."""
        try:
            arrival_input = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(AviaSearchLocators.ARRIVAL_CITY_INPUT)
            )
            arrival_input.clear()  # Очищаем поле для ввода города прибытия
        except TimeoutException:
            print("Не удалось найти поле для ввода города прибытия")

    def select_arrival_city_from_autocomplete(self):
        """Выбор первого города из автозаполнения для прибытия."""
        try:
            arrival_auto_complete = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(AviaSearchLocators.ARRIVAL_AUTOCOMPLIT_FIRST)
            )
            arrival_auto_complete.click()
        except TimeoutException:
            print("Не удалось выбрать первый город прибытия из автозаполнения")

    def click_search_button(self):
        """Нажатие на кнопку поиска."""
        try:
            search_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(AviaSearchLocators.SEARCH_BUTTON)
            )
            search_button.click()
        except TimeoutException:
            print("Не удалось нажать на кнопку поиска")
