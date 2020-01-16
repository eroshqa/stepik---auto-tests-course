from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    button1 = browser.find_element_by_tag_name("button")
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)

    button2 = browser.find_element_by_tag_name("button")
    button2.click()
finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла