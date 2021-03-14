#! python3
# play the 2048 game using an up, right, down, left strategy

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://play2048.co/")

htmlElem = driver.find_element_by_tag_name("html")
gameOver = driver.find_elements_by_class_name("game-message game-over")

while len(gameOver) < 1:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)

driver.quit()