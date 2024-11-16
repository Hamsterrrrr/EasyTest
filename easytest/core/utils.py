import os
import shutil
import subprocess
import time
from typing import Union, Tuple, Optional
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import logging
import allure
from easytest.visual.comparison import ImageComparator


def find_element(
    driver, 
    locator: Union[str, Tuple[int, int]], 
    screen_path: str = None, 
    timeout: int = 10
) -> Union[Tuple[int, int], WebElement, None]:

    with allure.step(f"Поиск элемента: {locator}"):
        if isinstance(locator, str) and locator.endswith(".png"):
            if screen_path is None:
                raise ValueError("Для поиска по шаблону необходимо указать screen_path.")

            position = ImageComparator.find_template_on_screen(screen_path, locator)
            if position:
                logging.info(f"Элемент найден по шаблону {locator} на координатах {position}.")
                return position
            else:
                logging.error(f"Элемент по шаблону '{locator}' не найден.")
                return None

        # Поиск через стандартные локаторы
        try:
            locators = {
                "id=": By.ID,
                "class=": By.CLASS_NAME,
                "xpath=": By.XPATH,
                "name=": By.NAME,
                "css=": By.CSS_SELECTOR
            }
            for prefix, by in locators.items():
                if isinstance(locator, str) and locator.startswith(prefix):
                    value = locator[len(prefix):]
                    break
            else:
                raise ValueError(f"Неизвестный формат локатора: {locator}")

            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.presence_of_element_located((by, value)))
            logging.info(f"Элемент найден с локатором: {locator}")
            return element
        except Exception as ex:
            logging.error(f"Не удалось найти элемент {locator}: {str(ex)}")
            return None

        
def take_screen(driver, test_name, suffix="screenshot", take_screenshot=True):
    if take_screenshot:
        with allure.step(f"Создание скриншота: {test_name}_{suffix}"):
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{test_name}_{suffix}_{timestamp}.png"
            screenshot_path = os.path.join("screen_video", screenshot_name)
            
            if not os.path.exists("screen_video"):
                os.makedirs("screen_video")
            
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
