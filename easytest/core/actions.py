import logging
import time
from typing import Tuple, Union
import allure
from easytest.core.utils import take_screen, find_element
from selenium.webdriver.remote.webelement import WebElement
from easytest.visual.comparison import ImageComparator


class Actions:
    def __init__(self, driver):
        self.driver = driver
        
        
    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_to_disappear(self, template_path: str, timeout: int = 30, screen_path: str = "current_screen.png"):
        start_time = time.time()
        with allure.step(f"Ожидание исчезновения элемента: {template_path}"):
            while time.time() - start_time < timeout:
                # Сохраняем скриншот текущего экрана
                self.driver.get_screenshot_as_file(screen_path)

                # Проверяем, присутствует ли изображение
                position = ImageComparator.find_template_on_screen(screen_path, template_path)
                if position is None:
                    logging.info(f"Элемент {template_path} исчез с экрана.")
                    return True  # Изображение исчезло воля

                logging.info(f"Элемент {template_path} все еще присутствует на экране, ждем...")
                time.sleep(1)
            raise TimeoutError(f"Элемент {template_path} не исчез за {timeout} секунд.")
        
    @allure.step("Ожидание появления элемента")
    def wait_for_element_to_appear(self, template_path: str, timeout: int = 30, screen_path: str = "current_screen.png"):
        start_time = time.time()
        with allure.step(f"Ожидание появления элемента: {template_path}"):
            while time.time() - start_time < timeout:
                self.driver.get_screenshot_as_file(screen_path)
                position = ImageComparator.find_template_on_screen(screen_path, template_path)
                if position:
                    logging.info(f"Элемент {template_path} появился на экране.")
                    return True  # Элемент появился на экране
                
                logging.info(f"Элемент {template_path} все еще не присутствует на экране, ждем...")
                time.sleep(1)
            raise TimeoutError(f"Элемент {template_path} не появился за {timeout} секунд.")
    
    def scroll(self, direction='up', duration=800, steps=1):
        with allure.step(f"Прокрутка экрана в направлении: {direction}, длительность: {duration}, шаги: {steps}"):
            size = self.driver.get_window_size()
            start_x = size['width'] // 2
            start_y = size['height'] // 2
            directions = {
                'up': (start_x, size['height'] - 100),
                'down': (start_x, 100),
                'left': (size['width'] - 100, start_y),
                'right': (100, start_y)
            }

            if direction not in directions:
                raise ValueError("Неверное направление. Используйте 'up', 'down', 'left' или 'right'.")

            end_x, end_y = directions[direction]
            for _ in range(steps):
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    @allure.step("Клик по элементу")
    def click_element(self, locator, test_name, take_screenshot=True, screen_path="current_screen.png"):
        try:
            # Скриншот перед поиском элемента
            take_screen(self.driver, test_name, 'init', take_screenshot)

            # Поиск элемента
            element = find_element(self.driver, locator, screen_path=screen_path)

            if isinstance(element, tuple):  # Если найдены координаты
                take_screen(self.driver, test_name, 'before_tap', take_screenshot)
                with allure.step(f"Клик по координатам {element}"):
                    self.driver.tap([element])  # Выполняем клик по координатам
                    logging.info(f"Клик выполнен по координатам: {element}")
                take_screen(self.driver, test_name, 'after_tap', take_screenshot)
            elif element:  # Если найден WebElement
                take_screen(self.driver, test_name, 'before_click', take_screenshot)
                with allure.step(f"Клик по WebElement {locator}"):
                    element.click()  # Выполняем клик по WebElement
                    logging.info(f"Клик выполнен по элементу: {locator}")
                take_screen(self.driver, test_name, 'after_click', take_screenshot)
            else:  # Элемент не найден
                take_screen(self.driver, test_name, 'element_not_found', take_screenshot)
                raise ValueError(f"Элемент с локатором {locator} не найден.")

        except Exception as ex:
            logging.error(f"Ошибка в click_element: {ex}")
            take_screen(self.driver, test_name, 'error', take_screenshot)
            raise

    def input_text(self, locator, input_text, test_name, take_screenshot=True):
        with allure.step(f"Ввод текста в элемент {locator}"):
            try:
                take_screen(self.driver, test_name, 'init', take_screenshot)
                element = find_element(self.driver, locator)
                if element:
                    take_screen(self.driver, test_name, 'before_input', take_screenshot)
                    element.send_keys(input_text)
                    take_screen(self.driver, test_name, 'after_input', take_screenshot)
                else:
                    take_screen(self.driver, test_name, 'element_not_found', take_screenshot)
            except Exception as ex:
                logging.error(f"Ошибка в input_text: {ex}")
                take_screen(self.driver, test_name, 'error', take_screenshot)

    def get_text_from_element(self, locator, test_name):
        with allure.step(f"Получение текста из элемента с локатором {locator}"):
            element = find_element(self.driver, locator)
            if element:
                text = element.text
                logging.info(f"Текст элемента: {text}")
                return text
            else:
                logging.warning(f"Элемент не найден: {locator}")
                return None
