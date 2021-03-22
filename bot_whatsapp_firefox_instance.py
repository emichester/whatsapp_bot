"""
https://tarunlalwani.com/post/reusing-existing-browser-session-selenium/
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
# secure imports
import configparser
from config.data import USER_DATA_PATH, CACHE_PATH

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

def main():
    config = configparser.ConfigParser()
    config.read("config/cache/session.ini")
    session_id =  config['SESSION']['session_id']
    executor_url = config['SESSION']['executor_url']
    driver = create_driver_session(session_id, executor_url)

# continuar por aquí ################################

contact = "CONSULTARRRR"
message = "Esto es un mensaje de prueba"

search_xpath = "/html/body/div/div/div/div[3]/div/div[1]/div/label/div/div[2]"
search = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
search.clear()
search.send_keys(contact)

contact_xpath = "/html/body/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]"
contact_button = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, contact_xpath)))
contact_button.click()

typebox_xpath = "/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
typebox = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, typebox_xpath)))
typebox.send_keys(message)
typebox.send_keys(Keys.ENTER)