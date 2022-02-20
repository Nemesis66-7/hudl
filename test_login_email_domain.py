from selenium import webdriver
from selenium.webdriver.common.by import By                          
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#initialize emails array
emails = ["local-part@[IPv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334]","local-part@doesnotexist.tld"] #https://en.wikipedia.org/wiki/Email_address; violate RFC rules on domain

#Keeping each iteration to a session may be better; interested in hudl's practices on this
for email in emails:
    #Open Browser
    driver = webdriver.Firefox()  
    driver.implicitly_wait(5)                          
    driver.get("https://www.hudl.com/login")            

    #Provide password
    driver.find_element(By.ID,'password').send_keys('P@ssw0rd')
    driver.find_element(By.ID,'email').send_keys(email)                  
    driver.find_element(By.ID,'logIn').click()

    #Verification
    try:
        driver.find_element(By.LINK_TEXT,"Need help?")
    except NoSuchElementException:
        print(email, "Not Handled - \"Need help?\" link does not exist")

    #Close Session
    driver.quit()                                                                                    








