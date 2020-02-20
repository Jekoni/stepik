from selenium import webdriver
import time
import os
import math 



try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    def calc(x):
	    return str(math.log(abs(12*math.sin(int(x)))))
    
	
    browser = webdriver.Chrome()
    browser.get(link)
  
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_id("input_value")
    x_input = browser.find_element_by_id("answer")
    x = x_element.text
    print(x)
    y = calc(x)
    x_input.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла