from pages.login_page import LoginPage

def test_login_fail(driver):
    login_page = LoginPage(driver)
    login_page.login("user", "password")

    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"
    