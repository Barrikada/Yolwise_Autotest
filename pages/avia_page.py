from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import AviaSearchLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AviaPage(BasePage):
    def enter_departure_city(self):
        try:
            departure_input = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(AviaSearchLocators.DEPARTURE_CITY_INPUT)
            )
            departure_input.click()
        except TimeoutException:
            print("Не удалось кликнуть по полю города отправления")
            return False
        return True

    def select_departure_city_from_autocomplete(self):
        try:
            departure_auto_complete = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(AviaSearchLocators.DEPARTURE_AUTOCOMPLIT_FIRST)
            )
            departure_auto_complete.click()
        except TimeoutException:
            print("Не удалось выбрать первый город отправления из автокомплита")
            return False
        return True

    def enter_arrival_city(self):
        try:
            arrival_input = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(AviaSearchLocators.ARRIVAL_CITY_INPUT)
            )
            arrival_input.click()
            arrival_input.clear()
        except TimeoutException:
            print("Не удалось кликнуть по полю города прибытия")
            return False
        return True

    def select_arrival_city_from_autocomplete(self):
        try:
            arrival_auto_complete = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(AviaSearchLocators.ARRIVAL_AUTOCOMPLIT_FIRST)
            )
            arrival_auto_complete.click()
        except TimeoutException:
            print("Не удалось выбрать первый город прибытия из автокомплита")
            return False
        return True

    def click_search_button(self):
        try:
            search_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(AviaSearchLocators.SEARCH_BUTTON)
            )
            search_button.click()
        except TimeoutException:
            print("Не удалось нажать на кнопку поиска")
            return False
        return True

    def verify_search_results(self):
        try:
            sort_avia = WebDriverWait(self.browser, 20).until(
                EC.visibility_of_element_located(AviaSearchLocators.SORT_AVIA)
            )
            if "By price" in sort_avia.text:
                return "Результаты найдены и отсортированы по цене"
        except TimeoutException:
            try:
                no_results = WebDriverWait(self.browser, 20).until(
                    EC.visibility_of_element_located(AviaSearchLocators.NO_RESULTS_AVIA)
                )
                if "No results" in no_results.text:
                    return "Ничего не найдено"
            except TimeoutException:
                return "За 30 секунд авиабилетов не найдено."
