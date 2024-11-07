import pytest
from pages.login_page import LoginPage
from pages.avia_page import AviaPage


def test_search_avia_today(browser):
    # URL страницы логина
    url = "https://yolwise.com/login"
    login_page = LoginPage(browser, url)
    login_page.open()

    # Вводим email и пароль
    login_page.enter_email("email")
    login_page.enter_password("password")

    # Нажимаем на кнопку авторизации
    login_page.click_authorization_button()

    # Проверка успешности авторизации — ожидаем, что кнопка поиска станет доступной
    assert login_page.is_search_button_present(), "Кнопка поиска не найдена"

    # Переход на страницу поиска авиабилетов
    avia_page = AviaPage(browser, url)
    avia_page.open()

    # Вводим город отправления и выбираем из автокомплита первый
    avia_page.enter_departure_city()
    avia_page.select_departure_city_from_autocomplete()

    # Вводим город прибытия и выбираем из автокомплита первый
    avia_page.enter_arrival_city()
    avia_page.select_arrival_city_from_autocomplete()

    # Нажимаем на кнопку поиска
    avia_page.click_search_button()

    # Проверка наличия результатов поиска:
    # - Если на странице отображен элемент "By price", считаем, что авиаперелеты найдены.
    # - Если виден элемент "No results", значит, ничего не найдено.
    # - В противном случае выводим сообщение, что идет поиск билетов.
    result_message = avia_page.verify_search_results()
    assert result_message in ["Результаты найдены и отсортированы по цене", "Ничего не найдено"], result_message
    print(result_message)

    # Делаем скриншот в конце теста, чтобы убедиться в результате
    avia_page.take_screenshot("search_avia_test")
