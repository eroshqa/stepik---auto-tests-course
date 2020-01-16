from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    z = str(int(x) + int(y))
    #element = browser.find_element_by_id("dropdown").click()
   # browser.find_element_by_css_selector("[value='" + z + "']").click()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла