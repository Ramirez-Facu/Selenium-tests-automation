from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_fail(driver):
    login_page = LoginPage(driver)
    login_page.login("user", "password")

    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"
def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user","secret_sauce")
    
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"