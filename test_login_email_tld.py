from selenium import webdriver
from selenium.webdriver.common.by import By                          
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#initialize emails array
emails = ["local-part@validSite.org","local-part@validSite.","local-part@validSite"] #https://en.wikipedia.org/wiki/Email_address; violate RFC rules on tld

#Open Browser
driver = webdriver.Firefox()  
driver.implicitly_wait(5)                          
driver.get("https://www.hudl.com/login")                

#Provide password
driver.find_element(By.ID,'password').send_keys('P@ssw0rd')

#Iterate through emails
for email in emails:
    driver.find_element(By.ID,'email').send_keys(email)                  
    driver.find_element(By.ID,'logIn').click()

    #Verification
    try:
        driver.find_element(By.XPATH,"//div[@class='login-error-container']")
    except NoSuchElementException:
        print(email, "Not Handled - Invalid Log In message does not exist")

    #Clean-up
    driver.find_element(By.ID,'email').clear()
    driver.delete_all_cookies()

#Close Session
driver.quit()





