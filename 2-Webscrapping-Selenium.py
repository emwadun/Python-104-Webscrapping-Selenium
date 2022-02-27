'''
Lets now fill up some forms.

'''
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys #--> we need this if we need to have keystrokes like clicking buttons etc

driver = webdriver.Chrome() 
driver.implicitly_wait(10) # --> This gives 10 seconds before we confirm the page is loaded. helps while clicking accept all cookies.

url = 'https://dashboard.heroku.com/apps'

driver.get(url)

#Lets click on 'Accept all cookies popup on the page'.
#You can get xpath by:
# -> click right-click on button -> inspect -> click on arrow button on right side menu -> click on button on left -> it will highlight the section ->
# rightclick -> copy -> copy xpath

driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()


#since we have two fields to fill, email address and password. Also we need xpath for login button. 
# Get their xpaths and we use them.

'''
//*[@id="email"]
//*[@id="password"]
//*[@id="login"]/form/button
'''

#For safety of our email and password in code, lets use variables otherwise you can specify the strings in send_keys directly but that is not safe.
email = input("Enter email: ")
password = input("Enter password: ")

driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="login"]/form/button').click()

#Here we log in now successfully!


#Lets click on 'Later' popup that we dont need to show after login regarding MFA


driver.find_element_by_xpath('//*[@id="mfa-later"]/button').click()