from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    browser.execute_script("window.scrollBy(0, 100);")
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    button1 = browser.find_element_by_tag_name("button")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
