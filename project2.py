from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
driver = webdriver.Chrome()
driver.get(link)

num = driver.find_element_by_id('input_value')
driver.execute_script("return arguments[0].scrollIntoView(true);", num)
input1 = driver.find_element_by_id('answer')
input1.send_keys(calc(num.text))

robotCheckbox = driver.find_element_by_id('robotCheckbox')
driver.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
robotCheckbox.click()

robotsRule = driver.find_element_by_id('robotsRule')
driver.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
robotsRule.click()

button = driver.find_element_by_tag_name("button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
