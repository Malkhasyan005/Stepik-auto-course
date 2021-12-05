from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

ind = input()
link = f"http://suninjuly.github.io/selects{ind}.html"
driver = webdriver.Chrome()
driver.get(link)

select = Select(driver.find_element_by_tag_name("select"))
num1 = driver.find_element_by_id('num1').text
num2 = driver.find_element_by_id('num2').text
num = int(num1) + int(num2)
select.select_by_value(f"{num}")
driver.find_element_by_class_name('btn-default').click()
time.sleep(4)
