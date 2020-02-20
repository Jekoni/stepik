from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/math.html"
    def calc(x):
	    return str(math.log(abs(12*math.sin(int(x)))))
    
	
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x_input = browser.find_element_by_css_selector("#answer")
    x = x_element.text
    print(x)
    y = calc(x)
    x_input.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	#return str(math.log(abs(12*math.sin(int(x)))))
    
   
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()