import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions 
# Here you should set the path to your driver

driver_path = "./drivers/msedgedriver.exe"

# Set the options and the service
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")
options.add_argument("--silent")
service = Service(driver_path)

# Initialize the driver
driver = webdriver.Edge(service=service, options=options)

try:
    driver.get("https://www.google.com")
    search_box = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME ,"q")))
    #search_box = driver.find_element(By.Name ,"q")
    search_box.send_keys("Selenium automation")
    search_box.send_keys(Keys.RETURN)
    print(driver.title)

finally:
    driver.implicitly_wait(5)
    driver.quit()

#