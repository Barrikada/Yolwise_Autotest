import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Input language (default ru)")
    parser.addoption('--env', action='store', help='Input environment')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_argument("ignore-certificate-errors")
    options.add_argument("start-maximized")
    options.page_load_strategy = 'eager'
    print(f"\nStart browser for test with language: {language}")

    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser..")
    browser.quit()
