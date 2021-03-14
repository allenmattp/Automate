#! python3
# emailLogin.py - sign into gmail and then send an email of active clipboard
# pyinputplus doesn't seem to like working in IDE so runs best with a .bat

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyinputplus as pyip
import pyperclip


def nextElem(currentElem):
    # tabs to next element
    currentElem.send_keys(Keys.TAB)
    newElem = driver.switch_to.active_element
    return newElem

driver = webdriver.Firefox()
htmlElem = driver.find_element_by_tag_name("html")

# prompt for username/password to sign into Gmail
driver.get("https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/")
userElem = driver.find_element_by_name("identifier")
username = pyip.inputStr("Enter your username:\n")
userElem.send_keys(username)
userElem.send_keys(Keys.ENTER)

try:
    # give page enough time to load password field
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
finally:
    passwordElem = driver.find_element_by_name("password")
    password = pyip.inputPassword("Input your password:\n")
    passwordElem.send_keys(password)
    passwordElem.send_keys(Keys.ENTER)

try:
    # allow site to load before clicking compose
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div"))
    )
finally:
    composeElem = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")
    composeElem.click()

try:
    # wait for new message box to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "to"))
    )
finally:
    toElem = driver.find_element_by_name("to")
    toEmail = pyip.inputEmail("Enter recipient's email:\n")
    toElem.send_keys(toEmail)

    subjectElem = driver.find_element_by_name("subjectbox")
    subject = pyip.inputStr("Enter subject:\n")
    subjectElem.send_keys(subject)

    textboxElem = nextElem(subjectElem)
    message = pyperclip.paste() # will send whatever is currently on clipboard
    textboxElem.send_keys(message)

    sendElem = nextElem(textboxElem)
    sendElem.send_keys(Keys.ENTER)


# driver.quit()