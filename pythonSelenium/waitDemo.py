#Implicit Wait
#Explicit Wait
#pause using time class

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

list = []
list2 = []
validateText = "Option3"
s = Service('/Users/nicolasbrown/Desktop/automation/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    button.click()
print(list)

#driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
#driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(4)

promoCode = "rahulshettyacademy"
wait = WebDriverWait(driver, 5)

veggies = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for veg in veggies:
    list2.append(veg.text)
print (list2)
assert list[0] == list2[0] == "Cucumber - 1 Kg"
assert list[1] == list2[1] == "Raspberry - 1/4 Kg"
assert list[2] == list2[2] == "Strawberry - 1/4 Kg"

beforeDiscountAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text 
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode"))).send_keys(promoCode)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum +int(amount.text)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount

afterDiscountAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text 
assert float(afterDiscountAmount) < int(beforeDiscountAmount) 


