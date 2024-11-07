from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_LINK = (By.CSS_SELECTOR, "input[placeholder='E-posta']")
    PASSWORD_LINK = (By.CSS_SELECTOR, "input[placeholder='Şifre']")
    AUTHORIZATION_BUTTON = (By.CSS_SELECTOR, "[data-qa='sign_in']")


"""Пока не добавляю data-qa, буду заниматься этим позже. Поэтому локаторы могут выглядеть не очень красиво"""


class AviaSearchLocators:
    DEPARTURE_CITY_INPUT = (By.CSS_SELECTOR, "input[type='text'][placeholder='From']")
    ARRIVAL_CITY_INPUT = (By.CSS_SELECTOR, "input[type='text'][placeholder='To']")
    DEPARTURE_AUTOCOMPLIT_FIRST = (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[1]/div/div/div[1]/div[1]/div["
                                             "1]/div[1]/div/div[2]/div/div/div[1]/div/div[2]")
    ARRIVAL_AUTOCOMPLIT_FIRST = (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[1]/div/div/div[1]/div[1]/div["
                                           "1]/div[3]/div/div[2]/div/div/div[1]/div/div[2]")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]")
    SORT_AVIA = (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]")
    NO_RESULTS_AVIA = (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div/div/div/div[1]")
