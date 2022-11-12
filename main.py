from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(r"C:\Users\aleja\Downloads\selenium-java-4.5.3\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")
box = driver.find_element(by=By.ID, value="twotabsearchtextbox")
submit_button = driver.find_element(by=By.ID, value="nav-search-submit-button")
box.send_keys("HP Pavilion azul")
submit_button.click()
item = driver.find_element(by=By.CLASS_NAME, value="s-image")
item.click()

cantidadbot = driver.find_element(by=By.CLASS_NAME, value="a-button-inner")
cantidadbot.click()
cantidad = driver.find_element(by=By.ID, value="quantity_1")
cantidad.click()
agregar = driver.find_element(by=By.ID, value="add-to-cart-button")
agregar.click()
time.sleep(15)
cerrar = driver.find_element(by=By.ID, value="attach-close_sideSheet-link")
cerrar.click()
seeItem = driver.find_element(by=By.ID, value="nav-cart-count-container")
seeItem.click()
time.sleep(20)
driver.close()