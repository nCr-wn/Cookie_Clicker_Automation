from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()

driver = webdriver.Chrome(service=service)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

def formating(store_item):
     for i in store_item:
        x = i.text.split('\n')
        x = x[0].split(' - ')
        x.pop(0)
        x = x[0].split(',')
        return int(float(''.join(x)))


def formating_money(money):
    for i in money:
        x = i.text.split(',')
        return int(float(''.join(x)))

cookie_button = driver.find_element(By.CSS_SELECTOR, '#cookie')
money = driver.find_elements(By.CSS_SELECTOR, '#money')
    
play = True
while play:
    time.sleep(0.25)
    cookie_button.click()
    
    if formating_money(money) >= formating(driver.find_elements(By.CSS_SELECTOR, '#buyTime\ machine')):
        driver.find_element(By.CSS_SELECTOR, '#buyTime\ machine').click()
        time.sleep(0.5)
    elif formating_money(money) >= formating(driver.find_elements(By.CSS_SELECTOR, '#buyPortal')):
        driver.find_element(By.CSS_SELECTOR, '#buyPortal').click()
        time.sleep(0.5)
    elif formating_money(money) >= formating(driver.find_elements(By.CSS_SELECTOR, '#buyAlchemy\ lab')):
        driver.find_element(By.CSS_SELECTOR, '#buyAlchemy\ lab').click()
        time.sleep(0.5)
    elif formating_money(money) >= formating(driver.find_elements(By.CSS_SELECTOR, '#buyShipment')):
        driver.find_element(By.CSS_SELECTOR, '#buyShipment').click()
        time.sleep(0.5)
    elif formating_money(money) >= formating(driver.find_elements(By.CSS_SELECTOR, '#buyMine')):
        driver.find_element(By.CSS_SELECTOR, '#buyMine').click()
        time.sleep(0.5)
    elif formating_money(money) >= formating(driver.find_elements(By.CSS_SELECTOR, '#buyFactory')):
        driver.find_element(By.CSS_SELECTOR, '#buyFactory').click()
        time.sleep(0.5)
    elif formating_money(money) >= formating(driver.find_elements(By.CSS_SELECTOR, '#buyGrandma')):
        driver.find_element(By.CSS_SELECTOR, '#buyGrandma').click()
        time.sleep(0.5)
    elif formating_money(money) >= formating(driver.find_elements(By.CSS_SELECTOR, '#buyCursor')):
        driver.find_element(By.CSS_SELECTOR, '#buyCursor').click()
        time.sleep(0.5)
    
