from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

validateText = "Option3"
s = Service('/Users/nicolasbrown/Desktop/automation/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://rahulshettyacademy.com/AutomationPractice/') 

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateText)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText 
alert.accept()
#alert.dismiss()