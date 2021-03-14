#! python3
# play the 2048 game using an up, right, down, left strategy

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://play2048.co/")

htmlElem = driver.find_element_by_tag_name("html")

def play():
    gameOver = []
    while len(gameOver) < 1:    # keep pressing keys until game over message
        gameOver = driver.find_elements_by_class_name("game-message.game-over")
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)

count = 0
while count < 100:
    play()
    count += 1
    retryElem = driver.find_element_by_class_name("retry-button")
    retryElem.click()

bestScore = driver.find_elements_by_class_name("best-container")  # find high score
print(f"Computer played {count} games and managed a high score of {bestScore[0].text}")