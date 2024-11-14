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
    with allure.step(f"Поиск элемента с локатором {locator}"):
        try:
            locators = {
                "id=": By.ID,
                "class=": By.CLASS_NAME,
                "xpath=": By.XPATH,
                "name=": By.NAME,
                "css=": By.CSS_SELECTOR
            }
            for prefix, by in locators.items():
                if locator.startswith(prefix):
                    value = locator[len(prefix):]
                    break
            else:
                logging.error(f"Неизвестный формат локатора: {locator}")
                return None

            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((by, value)))
            return element
        except Exception as ex:
            logging.error(f"Элемент с локатором {locator} не найден: {str(ex)}")
            return None

import allure
import time
import logging
import os

def take_screen(driver, test_name, suffix="screenshot", take_screenshot=True):
    if take_screenshot:
        with allure.step(f"Создание скриншота: {test_name}_{suffix}"):
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{test_name}_{suffix}_{timestamp}.png"
            screenshot_path = os.path.join("screen_video", screenshot_name)
            try:
                driver.get_screenshot_as_file(screenshot_path)
                logging.info(f"Скриншот сохранен: {screenshot_path}")
                with open(screenshot_path, "rb") as file:
                    allure.attach(file.read(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
            except Exception as ex:
                logging.error(f"Не удалось создать скриншот {screenshot_path}: {ex}")


def report_data():
    with allure.step("Запуск Allure сервера"):
        try:
            logging.info("Запуск сервера Allure...")
            subprocess.Popen(["allure", "serve", "./allure-results"])
        except Exception as ex:
            logging.error(f"Ошибка при запуске Allure: {ex}")

def restart_screen_video():
    with allure.step("Перезапуск папки для скриншотов"):
        folder = "screen_video"
        try:
            if os.path.exists(folder):
                shutil.rmtree(folder)
                logging.info(f"Папка {folder} удалена.")
            os.makedirs(folder)
            logging.info(f"Папка {folder} создана заново.")
        except Exception as ex:
            logging.error(f"Ошибка при перезапуске папки {folder}: {ex}")
