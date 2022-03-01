'''
Now since selenium has been installed and webdriver has been installed lets test all is fine.

'''

from selenium import webdriver

 
#linux default path /usr/local/bin you can specify the path in chrome() if it is not located automatically.
driver = webdriver.Chrome() 

# When we run this python file now chrome is launched. with message "Chrome is being controlled by automated test software"
# That is nice!!! out setup of Selenium and webdriver is OK.

url = 'http://google.ie'

driver.get(url) #--> This open google page . Awesome!!!
