'''
* Lets test scrolling in the browsers using Selenium
* we will scroll to bottom of the page.

'''

from selenium import webdriver

driver = webdriver.Chrome()

#implicity wait time
driver.implicitly_wait(5)

#url launch
driver.get("https://www.tutorialspoint.com/index.htm")

#scroll to bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

