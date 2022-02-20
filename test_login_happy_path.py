from selenium import webdriver
from selenium.webdriver.common.by import By                          
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Open Browser
driver = webdriver.Firefox()  
driver.implicitly_wait(5)                          
driver.get("https://www.hudl.com/login")                

#Log In
driver.find_element(By.ID,'email').send_keys('<valid email>')                                                            #Use connection library to database Users table        
driver.find_element(By.ID,'password').send_keys('<valid password>')                                                                         #Passwords likely encrypted and salted; automation environment DMZ'd from network?    
driver.find_element(By.ID,'logIn').click()

#Verification
expected_result = 'EP'
actual_result = driver.find_element(By.XPATH,"//h5[@class='uni-avatar__initials uni-avatar__initials--user']").text                     #Not most reliable; used relative xpath but css selector or name may be better
assert expected_result == actual_result, f'Error. Expected text {expected_result}, but actual text: {actual_result}'

#Log Out; don't believe this is logging out. Elements in user Profile dropdown are in a div so Select class does not work either.
menu = driver.find_element(By.CSS_SELECTOR,".hui-globaluseritem__display-name > span:nth-child(1)")
hidden_log_out = driver.find_element(By.CSS_SELECTOR,".hui-globaladditionalitems--not-phone > a:nth-child(2) > span:nth-child(1)")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_log_out)
actions.perform()

#Close Session
#driver.delete_all_cookies() #Not necessary per this post? https://stackoverflow.com/questions/50456783/python-selenium-clear-the-cache-and-cookies-in-my-chrome-webdriver
driver.quit()





