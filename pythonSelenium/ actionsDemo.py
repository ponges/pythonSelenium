from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


s = Service('/Users/nicolasbrown/Desktop/automation/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://rahulshettyacademy.com/AutomationPractice')
action = ActionChains(driver)
menu = driver.find_element(By.ID, "mousehover")

action.move_to_element(menu).perform()
childMenu = driver.find_element(By.LINK_TEXT, "Top")
action.move_to_element(childMenu).click().perform()

driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')
action.double_click(driver.find_element(By.ID, "double-click" )).perform()
alert = driver.switch_to.alert
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept()