from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os
import math 

browser = webdriver.Chrome()
def calc(x):
	    return str(math.log(abs(12*math.sin(int(x)))))
		
browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )


button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id("input_value")
x_input = browser.find_element_by_id("answer")
x = x_element.text
print(x)
y = calc(x)
x_input.send_keys(y)
submit = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
submit.click()

time.sleep(5)
browser.quit()