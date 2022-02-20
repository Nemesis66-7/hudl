from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #https://selenium-python.readthedocs.io/waits.html
from selenium.webdriver.common.by import By                          
from selenium.webdriver.common.keys import Keys
import time

#Open Browser
driver = webdriver.Firefox()  
driver.implicitly_wait(5)                          
driver.get("https://www.hudl.com/login")                

#Log In
driver.find_element(By.ID,'email').send_keys('<valid email>')                                                               
driver.find_element(By.ID,'password').send_keys('<valid password>')  

driver.find_element(By.CSS_SELECTOR,'.checkbox-container').click()                                                                           
driver.find_element(By.ID,'logIn').click()

#Log Out
WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.CLASS_NAME,"hui-globaluseritem__display-name")) #By.XPATH,"//div[@class='hui-globaluseritem__display-name']"
)
driver.find_element(By.CLASS_NAME,"hui-globaluseritem__display-name").click() 

time.sleep(3)
WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.XPATH,"//a[@href='/logout']/span"))
)
driver.find_element(By.XPATH,"//a[@href='/logout']/span").click() 

#Log In
driver.find_element(By.CSS_SELECTOR,"a.mainnav__btn:nth-child(3)").click()

#Verification
expected_result = 'Evan.Pederson.1201@gmail.com'

time.sleep(3)
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.ID,'email'))
)
actual_result = driver.find_element(By.ID,'email').get_attribute('value')                  
assert expected_result.lower() == actual_result, f'Error. Expected text {expected_result}, but actual text: {actual_result}'

#Close Session
driver.quit()





