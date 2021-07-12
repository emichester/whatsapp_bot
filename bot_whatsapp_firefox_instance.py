#!/usr/bin/env python3
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
# secure imports
import configparser
# import utilities
from utilities.buttons import find_contact
from utilities.text_boxes import search_contact, type_chat_message

def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver

def send_message(driver, contact, message):
    """
    Args:
        contact : str : name of contact or group
        message : str
    """
    TIME_WAIT = 3
    search_contact(driver, contact)
    sleep(TIME_WAIT)
    type_chat_message(driver, message)

def close_father_webdriver(driver):
    driver.close() # better just press ENTER at the main bash

def main():
    config = configparser.ConfigParser()
    config.read("config/session/session.ini")
    session_id =  config['SESSION']['session_id']
    executor_url = config['SESSION']['executor_url']
    driver = create_driver_session(session_id, executor_url)

    from messages import messages

    base_url = 'https://web.whatsapp.com/'
    driver.get(base_url)
    sleep(10)
    
    for contact,message in messages.items():
        send_message(driver, contact, message)
        sleep(1)
    
    driver.get('https://www.duckduckgo.com')

if __name__ == "__main__":
    main()