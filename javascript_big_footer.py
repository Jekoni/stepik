from selenium import webdriver
import time
import math


try: 

    def calc(x):
	    return str(math.log(abs(12*math.sin(int(x)))))
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link) 
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 100);")	
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
	
   


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()