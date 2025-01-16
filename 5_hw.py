from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://saucedemo.com/")

# поиск элемента
icon = driver.find_element(By.CSS_SELECTOR, '#password')
user = driver.find_element(By.CSS_SELECTOR, '#user-name')
button = driver.find_element(By.CSS_SELECTOR, '#login-button')
if icon is None and user is None and button is None:
    print('Элементы не найден')

else:
    print('Элементы найдены')
