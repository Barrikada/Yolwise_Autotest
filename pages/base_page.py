import os
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def element_to_be_clickable(self, how, what, timeout=20):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def presence_of_element_located(self, how, what, timeout=60):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def take_screenshot(self, screenshot_name="screenshot"):
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(screenshots_dir, f"{screenshot_name}_{timestamp}.png")
        self.browser.save_screenshot(file_path)
        print(f"Screenshot saved at {file_path}")
