import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
time.sleep(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")