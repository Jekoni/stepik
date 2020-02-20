from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    def calc(x):
	    return str(math.log(abs(12*math.sin(int(x)))))
    
	
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("treasure")
    print(x_element)
    x_element_attribute = x_element.get_attribute("valuex")
    x_input = browser.find_element_by_css_selector("#answer")
    print(x_element_attribute)
    y = calc(x_element_attribute)
    x_input.send_keys(y)
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	#return str(math.log(abs(12*math.sin(int(x)))))
    
   
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()