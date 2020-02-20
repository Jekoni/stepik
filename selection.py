from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
  
	
    browser = webdriver.Chrome()
    browser.get(link)
    first_element = browser.find_element_by_id("num1")
    first_element_text = int(first_element.text)
    second_element = browser.find_element_by_id("num2")
    second_element_text = int(second_element.text)
    sum = first_element_text + second_element_text
    sum_str = "[value='" + str(sum) + "']"
    sum_str2 = str(sum)
    print(sum_str)
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(sum_str).click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	#return str(math.log(abs(12*math.sin(int(x)))))
    
   
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()