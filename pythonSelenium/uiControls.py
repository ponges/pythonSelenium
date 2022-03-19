from dis import dis
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/Users/nicolasbrown/Desktop/automation/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://rahulshettyacademy.com/AutomationPractice/') 

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements(By.NAME, "radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

displayedText = driver.find_element(By.ID, "displayed-text")
assert displayedText.is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not displayedText.is_displayed()
