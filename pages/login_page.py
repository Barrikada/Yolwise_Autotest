from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import LoginPageLocators, AviaSearchLocators


class LoginPage(BasePage):
    def enter_email(self, email):
        email_input = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_LINK)
        )
        email_input.clear()
        email_input.send_keys("demo@yolwise.com")

    def enter_password(self, password):
        password_input = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_LINK)
        )
        password_input.clear()
        password_input.send_keys("WmN-aqh-fbS-3na")

    def click_authorization_button(self):
        auth_button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.AUTHORIZATION_BUTTON)
        )
        auth_button.click()

    def is_search_button_present(self):
        return self.presence_of_element_located(*AviaSearchLocators.SEARCH_BUTTON)
