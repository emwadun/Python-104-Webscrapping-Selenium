'''
Now since selenium has been installed and webdriver has been installed lets test all is fine.

'''

from selenium import webdriver

#linux default path /usr/local/bin
driver = webdriver.Chrome() 

# When we run this python file now chrome is launched. with message "Chrome is being controlled by automated test software"
# That is nice!!! out setup of Selenium and webdriver is OK.

url = 'https://www.google.ie'

driver.get(url) #--> This open google page 