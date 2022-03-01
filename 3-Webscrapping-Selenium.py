'''
- Lets log into instagram
- scroll down the window
- & download photos from arteta's instagram
'''

from selenium import webdriver
from selenium.webdriver.common.keys  import Keys 
import time
import os
import wget


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
n_scrolls = 3
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

#lets get the links for the posts/images - WORKING
#posts = []
#links = driver.find_elements_by_tag_name('a')
#for link in links:
#    post = link.get_attribute('href')
#    if '/p' in post:
#     posts.append(post)

#print(posts)


#target all the link elements on the page
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]
#narrow down all links to image links only
anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

print('Found ' + str(len(anchors)) + ' links to images')
anchors[:5]

#Lets get the links of the images so that we can download them
images = []

#follow each image link and extract only image at index=1
for a in anchors:
    driver.get(a)
    time.sleep(5)
    img = driver.find_elements_by_tag_name('img')
    img = [i.get_attribute('src') for i in img]
    images.append(img[1])


#Lets save images to our computer, we need to create a directory
keyword = 'Arteta'
path = os.getcwd()
path = os.path.join(path, keyword + "_pics")

os.mkdir(path)
print(path)

#download images
counter = 0
for image in images:
    save_as = os.path.join(path, keyword + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
