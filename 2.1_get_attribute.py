from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    people_radio = browser.find_element_by_tag_name("img")
    x = people_radio.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    button1 = browser.find_element_by_tag_name("button")
    button1.click()
finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла