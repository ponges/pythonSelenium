from curses import window
from tkinter import SCROLL
from xml.dom.minidom import Document
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

validateText = "Option3"
s = Service('/Users/nicolasbrown/Desktop/automation/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.NAME, "name").send_keys("hello")
print(driver.find_element(By.NAME, "name").text)
print(driver.find_element(By.NAME, "name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))  
shopbutton = driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
driver.execute_script("arguments[0].click();", shopbutton)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
