from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(r"C:\Users\aleja\Downloads\selenium-java-4.5.3\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")