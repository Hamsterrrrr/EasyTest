from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import os
import shutil
import time
import logging
import allure
import subprocess


def find_element(driver, locator) -> WebElement:
    try:
        if isinstance(locator, tuple):
            by, value = locator
        else:
            if locator.startswith("id="):
                by = By.ID
                value = locator[3:]
            elif locator.startswith("class="):
                by = By.CLASS_NAME
                value = locator[6:]
            elif locator.startswith("xpath="):
                by = By.XPATH
                value = locator[6:]
            elif locator.startswith("name="):
                by = By.NAME
                value = locator[5:]
            elif locator.startswith("css="):
                by = By.CSS_SELECTOR
                value = locator[4:]
            else:
                logging.error(f"Unknown format for locator {locator}")
                return None

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((by, value)))
        return element
    except Exception as _ex:
        logging.error(f"Element with locator {locator} not found: {str(_ex)}")
        return None



def take_screen(driver, test_name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = f"screen_video/{screenshot_name}"
    driver.get_screenshot_as_file(screenshot_path)
    
    with open(screenshot_path, "rb") as file:
        allure.attach(file.read(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
    
    
    
def report_data():
    logging.info("Starting Allure server...")
    subprocess.Popen(["allure", "serve", "./allure-results"])
        
    

def restart_screen_video():
    folder = "screen_video"
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)
