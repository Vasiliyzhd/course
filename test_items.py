from selenium.webdriver.common.by import By
import time


def test_basket_exist(browser):
    assert bool(browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").get_attribute("type")) == True
    time.sleep(5)