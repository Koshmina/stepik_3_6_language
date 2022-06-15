import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ar or ca or cs or da or de or en-gb or el or es or fi or fr or it or ko or nl or pl or pt or pt-br or"
                          " ro or ru or sk or uk or zh-hans")


@pytest.fixture(scope="function")
def browser(request):
    try:
        user_language = request.config.getoption("language")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        yield browser
    finally:
        browser.quit()
