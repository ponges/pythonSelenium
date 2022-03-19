from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service('/Users/nicolasbrown/Desktop/automation/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://the-internet.herokuapp.com/iframe')
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)