from selenium.webdriver.common.by import By
import time

def test_add_to_baket_button_is_avaliable(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    assert True, " Button isn't avaliable "

