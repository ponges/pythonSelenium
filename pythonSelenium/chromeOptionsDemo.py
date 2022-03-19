from turtle import title
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
s = Service('/Users/nicolasbrown/Desktop/automation/drivers/chromedriver')
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get('https://rahulshettyacademy.com/angularpractice/')

print(driver.title)