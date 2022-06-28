import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: any language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(f'http://selenium1py.pythonanywhere.com/{str(language)}/catalogue/coders-at-work_207/')
    yield browser
    print("\nquit browser..")
    browser.quit()
