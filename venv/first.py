from sys import executable
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path=r"C:\Users\sirpah\OneDrive - Infinite Computer Solutions (India) Limited\Desktop\QA\QA Automation\SirpaAutomation\bins\chromedriver.exe" #r=takes input as raw text

service= Service(driver_path)

driver=webdriver.Chrome(service=service)


driver.get("https://www.saucedemo.com/")
print("Page title:",driver.title)

                                    #Login Page
driver.find_element(By.ID,'user-name').send_keys('standard_user')
driver.find_element(By.ID,'password').send_keys('secret_sauce')
#driver.implicitly_wait(5)
#driver.find_element(By.XPATH,'//*[@id="login-button"]').click()

#----EXPLICIT WAIT----
login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
)
login.click()


                                #homepage
firstItem= WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.ID,'item_4_title_link'))
)

firstItem.click()

                    #Printing text and price
paragraph= WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="inventory_item_container"]/div/div/div[2]/div[2]'))
)
text=paragraph.text
print("Paragraph:",text)

#------price---
price= WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="inventory_item_container"]/div/div/div[2]/div[3]'))
)
p=price.text
print("Price:",p)

time.sleep(2)




