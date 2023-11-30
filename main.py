from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="/Users/chetan/Desktop/Education/Learnings/Selenium/chromedriver")
driver = webdriver.Chrome(service=service)

# get the driver from www.google.com
driver.get("http://google.com")

# Waits for the gLFyf element
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)


input_ele = driver.find_element(By.CLASS_NAME, "gLFyf")
input_ele.clear()
input_ele.send_keys("Instagram" + Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Instagram")
link.click()

time.sleep(10)

driver.quit()
