from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from utilities.xpaths import search_box_xpath, chat_box_xpath

def search_contact(driver, contact):
    search = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
    search.clear()
    search.send_keys(contact)
    search.send_keys(Keys.ENTER)

def type_chat_message(driver, message):
    typebox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, chat_box_xpath)))
    typebox.send_keys(message)
    typebox.send_keys(Keys.ENTER)