from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.XPATH, "//input[@id='helpsearch']")
search.clear()
search.send_keys('cancel order')

sleep(3)

driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()

assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

driver.quit()