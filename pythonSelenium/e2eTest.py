from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



s = Service('/Users/nicolasbrown/Desktop/automation/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.LINK_TEXT, "Shop").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        #add item to cart
        product.find_element(By.XPATH, "div[2]/button").click()   
driver.find_element(By.CLASS_NAME, "nav-link.btn.btn-primary").click()
driver.find_element(By.XPATH, "//h4/a").text == productName 
driver.find_element(By.CLASS_NAME, "btn-success").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
termsCheckBox = driver.find_element(By.XPATH, "//*[@id='checkbox2']")
driver.execute_script("arguments[0].click();", termsCheckBox)
driver.find_element(By.CLASS_NAME, "btn-success").click()
successMessage = driver.find_element(By.XPATH, "//*[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in successMessage
driver.get_screenshot_as_file("screen.png")