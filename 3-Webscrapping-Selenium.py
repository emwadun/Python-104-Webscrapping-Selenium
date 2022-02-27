'''
- Lets log into instagram
'''

from email.mime import image
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys 

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')
driver.implicitly_wait(10)

driver.find_element_by_xpath('/html/body/div[4]/div/div/button[2]').click()

#Lets supply Instagram username and password for automation. We dont want to hardcode the values for security reasons.
username = input("Enter username: ")
password = input("Enter password: ")

driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

#lets dismiss the message to save the password that shows up on the screen. It did not work
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

#also lets dismiss message to turn on instagram notifications
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()


#Now lets search a hash tag #pythonprogramming
driver.implicitly_wait(10)

keyword = '#pythonprogramming'
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(keyword)

#now lets click on the first trending results
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()

#Lets scroll to select the images we have and list them
driver.execute_script("window.scrollTo(0,4000);")
images =  driver.find_element_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images

