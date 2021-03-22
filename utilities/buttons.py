from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from utilities.xpaths import find_contact_to_click_xpath

def find_contact(driver):
    contact_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, find_contact_to_click_xpath.format(contact))))
    contact_button.click()