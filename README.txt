'''
* Selenium is a library for webscrapping websites with dynamic contents such as social media sites like Instagram, Youtube, facebook, twitter etc.
* Selenium helps us to control our browsers: 
    - launching browsers and opening pages
    - filling out forms
    - etc
* It is used for testing.
https://pypi.org/project/selenium/

* Selenium requires a driver to interface with the chosen browser. 
Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. 
Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.
Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

* WebDriver is an open source tool for automated testing of webapps across many browsers. 
It provides capabilities for navigating to web pages, user input, JavaScript execution, and more.  
* WebDriver drives a browser natively, as a user would, either locally or 
on a remote machine using the Selenium server, marks a leap forward in terms of browser automation.

* Lets create our virtual environment and activate it:
    # python -m venv pyscripting-selenium
    # .\pyscripting-selenium\Scripts\activate

STEP 1: Installing Selenium:
    # pip install selenium
    # pip list
    selenium         4.1.2

STEP 2: Installing webdrivers either: gatewaydriver(for chrome) or chromedriver (for chrome).
    https://www.selenium.dev/documentation/webdriver/
    The browser version need to work with the webdriver you install. check about page of your browser.
    For my chrome: (...) -> Help --> About: Mine is 'Version 98.0.4758.102 (Official Build) (64-bit)'.
    Checking chrome support by reading latest documentation: https://chromedriver.chromium.org/downloads
    The readme of latest stable supports chrome 98. so I shoule be ok to install https://chromedriver.storage.googleapis.com/98.0.4758.102/notes.txt
    You can see chrome drivers supported and compatibility from: https://www.selenium.dev/downloads/

    download the zip, extract and install it.

Ref:
- https://www.selenium.dev/
- https://www.selenium.dev/documentation/

- Web Scraping Instagram with Selenium Python | by Arry M. Lani Anhar | Analytics Vidhya | Medium
https://medium.com/analytics-vidhya/web-scraping-instagram-with-selenium-python-b8e77af32ad4

- 4 Web Scraping Projects That Will Help Automate Your Life
https://medium.com/geekculture/4-web-scraping-projects-that-will-help-automate-your-life-6c6d43aefeb5

- Web Scraping Cheat Sheet (2021), Python for Web Scraping
https://medium.com/geekculture/web-scraping-cheat-sheet-2021-python-for-web-scraping-cad1540ce21c
'''