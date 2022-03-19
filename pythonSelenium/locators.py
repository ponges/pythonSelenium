from select import select
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/Users/nicolasbrown/Desktop/automation/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://rahulshettyacademy.com/angularpractice/')

#driver.find_element_by_name('name').send_keys('Nicolás')
driver.find_element(By.NAME, 'name').send_keys('Nicolás')
#driver.find_element_by_css_selector("input[name='email']").send_keys("ponges@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("ponges@gmail.com")
#driver.find_element_by_id('exampleCheck1').click()
driver.find_element(By.ID, "exampleCheck1").click()

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

#driver.find_element(by=By.XPATH, value="//input[@type='submit']") .click
driver.find_element(By.XPATH, "//input[@type='submit']").click()
succesText = driver.find_element(By.CLASS_NAME, "alert-success").text
print (succesText)
assert "Success! The Form has been submitted successfully!." in succesText
