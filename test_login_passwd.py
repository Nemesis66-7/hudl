from selenium import webdriver
from selenium.webdriver.common.by import By                          
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#initialize passwords array
passwords = ["invalidPasswd","' or 1=1--"] #https://pentestmonkey.net/category/cheat-sheet/sql-injection

#Open Browser
driver = webdriver.Firefox()  
driver.implicitly_wait(5)                          
driver.get("https://www.hudl.com/login")                

#Provide Email
driver.find_element(By.ID,'email').send_keys('Evan.Pederson.1201@gmail.com')

#Iterate through passwords
for passwd in passwords:
    driver.find_element(By.ID,'password').send_keys(passwd)                  
    driver.find_element(By.ID,'logIn').click()

    #Verification
    try:
        driver.find_element(By.LINK_TEXT,"Need help?")
    except NoSuchElementException:
        print(passwd, "Not Handled - \"Need help?\" link does not exist")

    #Clean-up
    driver.find_element(By.ID,'password').clear()
    driver.delete_all_cookies()

#Close Session
driver.quit()





