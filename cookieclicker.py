from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
import time

service = Service(executable_path="/Users/chetan/Desktop/Education/Learnings/Selenium/chromedriver")
chrome = webdriver.Chrome(service=service)  

cookieID = 'bigCookie'
cookie_count_id = 'cookies'
prod_price_prefix = 'productPrice'
prod_prefix = 'product'

chrome.get("http://orteil.dashnet.org/cookieclicker/")

WebDriverWait(chrome, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

lang = chrome.find_element(By.XPATH, "//*[contains(text(), 'English')]")
lang.click()


WebDriverWait(chrome, 5).until(
    EC.presence_of_element_located((By.ID, cookieID))
)
cookie = chrome.find_element(By.ID, cookieID)

while True:
    cookie.click()
    cookie_count = int(chrome.find_element(By.ID, cookie_count_id).text.split(" ")[0])

    for i in range(4, -1, -1):
        # get product price edding with 'i' and click on it if cookie_count is >= the price
        prod_price = chrome.find_element(By.ID, prod_price_prefix + str(i)).text
        prod_price = prod_price.replace(",", "")
        if not prod_price.isdigit():
            continue

        prod_price = int(prod_price)
        if cookie_count >= prod_price:
            prod = chrome.find_element(By.ID, prod_prefix + str(i))
            prod.click()
            print("Clicked on product " + str(i))