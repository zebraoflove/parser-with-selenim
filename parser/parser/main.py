import time
import csv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
url = "https://www.nseindia.com/"
driver = webdriver.Chrome()
driver.get(url)
actions = ActionChains(driver)
market_data = driver.find_element(By.ID, 'link_2')
actions.move_to_element(market_data)
actions.perform()
preopen_market = driver.find_element(By.LINK_TEXT, 'Pre-Open Market')
actions.click(preopen_market)
actions.perform()
driver.implicitly_wait(3)
items = len(driver.find_elements(By.CLASS_NAME, 'symbol-word-break'))
names = driver.find_elements(By.CLASS_NAME, 'symbol-word-break')
prices = driver.find_elements(By.CSS_SELECTOR, 'tr > td.bold.text-right')
items2 = len(driver.find_elements(By.CSS_SELECTOR, 'tr > td.bold.text-right'))
with open('prices.csv', 'w') as f: 
    writer = csv.writer(f, delimiter = " ", lineterminator = "\r")
    for item in range(items):
        name = names[item].text
        price = prices[item].text
        add = (name + ';' + price)
        writer.writerow(add)
time.sleep(3)
home = driver.find_element(By.ID, 'link_0')
actions.click(home)
actions.perform()
actions.scroll_by_amount(0, 1100)
actions.perform()
time.sleep(1)
board_meetings = driver.find_element(By.ID, 'board-meetings2')
actions.click(board_meetings)
actions.perform()
time.sleep(1)
corporate_actions = driver.find_element(By.ID, 'corporate-actions2')
actions.click(corporate_actions)
actions.perform()
time.sleep(1)
driver.close()
