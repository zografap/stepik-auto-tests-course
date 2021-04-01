from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome(executable_path=r"c://chromedriver//chromedriver.exe")
    browser.get(link)
    button = browser.find_elements_by_id("book")
    print('button = browser.find_elements_by_id("book")')

    if (WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))== True):
        button[0].click()
        print('button[0].click()')

    x =int( browser.find_element_by_xpath('//*[@id="input_value"]').text)
    print(x)

    result =calc(x)
    print(result)

    input1 = browser.find_element_by_class_name('form-control')
    input1.send_keys(result)
    print("input1")

    button1 = browser.find_element_by_css_selector("#solve")
    button1.click()
    print("button1.click()")
      

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(30)
    browser.quit()


