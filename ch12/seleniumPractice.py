from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyinputplus, time

browser = webdriver.Firefox()

# find the .cover-thumb element and then click on link
"""browser.get("https://inventwithpython.com")
try:
    elem = browser.find_element_by_class_name("cover-thumb")
    print(f"Found {elem.tag_name} element with that class name!")
except:
    print("Unable to find an element with that name.")

linkElem = browser.find_element_by_link_text("Read Online for Free")
print(type(linkElem))

linkElem.click()"""

# prompt for username/password and sign into Dakka
"""browser.get("https://www.dakkadakka.com/dakkaforum/user/login.page")
userElem = browser.find_element_by_name("username")
username = pyinputplus.inputStr("Enter your username:\n")
userElem.send_keys(username)

passwordElem = browser.find_element_by_name("password")
password = pyinputplus.inputPassword("Input your password:\n")
passwordElem.send_keys(password)
passwordElem.submit()"""

browser.get("https://nostarch.com")
htmlElem = browser.find_element_by_tag_name("html")
htmlElem.send_keys(Keys.END)
time.sleep(3)
htmlElem.send_keys(Keys.HOME)
time.sleep(3)

browser.quit()