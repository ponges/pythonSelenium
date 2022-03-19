from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/Users/nicolasbrown/Desktop/automation/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://login.salesforce.com/')
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("Nicolas")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Password ")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").clear()
driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
driver.find_element(By.NAME, 'cancel').click()
driver.find_element(By.XPATH,"//form[@name='login']").text
print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] label:nth-child(3)").text)