from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from lxml import etree

from utilities.xpaths import search_box_xpath, chat_box_xpath
from utilities.classes import search_box_class, chat_box_class
from utilities.ids import sidebar_id, main_chat_id

def search_contact(driver, contact):
    #@ find id
    divs = driver.find_elements_by_tag_name('div')
    for div in divs:
        sidebar = div.find_element_by_id(sidebar_id)
        break
    ## find class
    # search = main.find_element()
    search = WebDriverWait(sidebar, 5).until(EC.presence_of_element_located((\
        By.CSS_SELECTOR,"[class$='%s']"%search_box_class)))
    search.clear()
    search.send_keys(contact)
    search.send_keys(Keys.ENTER)
def type_chat_message(driver, message):
    ## find id
    divs = driver.find_elements_by_tag_name('div')
    for div in divs:
        main = div.find_element_by_id(main_chat_id)
        break
    ## find class
    typebox = WebDriverWait(main, 5).until(EC.presence_of_element_located((\
        By.CSS_SELECTOR,"[class$='%s']"%chat_box_class)))
    typebox.send_keys(message)
    typebox.send_keys(Keys.ENTER)