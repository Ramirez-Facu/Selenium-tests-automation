import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

#Definimos el driver para que se ejecute una vez para toda la sesion
@pytest.fixture(scope="session")
def driver():
    service = Service(executable_path="./drivers/msedgedriver.exe")
    driver =webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()
