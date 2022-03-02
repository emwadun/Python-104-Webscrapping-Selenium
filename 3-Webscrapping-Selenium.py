'''
- Let's log into instagram automatically
- Search Mikel artetas instagram account
- Download the posts or photos.
- Close the browser
'''

from selenium import webdriver
from selenium.webdriver.common.keys  import Keys 
import time
import os
import wget
import requests


driver = webdriver.Chrome()

driver.get('https://www.instagram.com')
driver.implicitly_wait(10)

#lets click on the button to accept all cookies
driver.find_element_by_xpath('/html/body/div[4]/div/div/button[2]').click()

#Click on the login button
#driver.implicitly_wait(5)
#driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()

#Lets supply Instagram username and password for automation. We dont want to hardcode the values for security reasons.
username = input("Enter username: ")
password = input("Enter password: ")

driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

#lets dismiss the message to save the password that shows up on the screen. It did not work
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

#also lets dismiss message to turn on instagram notifications
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()


#Now lets search a 'mikelarteta' Instagram account
driver.implicitly_wait(10)
searchword = 'mikelarteta'
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(searchword)

#now lets click on the first result
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()


#lets download the first image / post. This will save in a list.
images = driver.find_elements_by_class_name("_bz0w")

images_href = []
for img in images:
    href = img.find_element_by_tag_name("a").get_attribute("href")
    images_href.append(href)

print(images_href)



#Lets scroll down the page -- WORKING
#scrolldown = driver.execute_script(
#    "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#match = False
#while(match == False):
#    last_count = scrolldown
#    time.sleep(3)
#    scrolldown = driver.execute_script(
#        "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#    if last_count == scrolldown:
#        match = True

#Lets scroll down 3 times
#n_scrolls = 3
#for j in range(0, n_scrolls):
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#    time.sleep(5)

#lets get the links for the posts/images - WORKING
#posts = []
#links = driver.find_elements_by_tag_name('a')
#for link in links:
#    post = link.get_attribute('href')
#    if '/p' in post:
#     posts.append(post)

#print(posts)


#Lets save images to our computer, we need to create a directory
keyword = 'Arteta'
path = os.getcwd()
path = os.path.join(path, keyword + "_pics")

#os.mkdir(path)
#print(path)

#download images
counter = 0
for image in images_href:
    save_as = os.path.join(path, keyword + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

driver.implicitly_wait(20)
driver.close()
