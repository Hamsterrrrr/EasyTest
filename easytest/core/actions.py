import logging
import allure
from easytest.core.utils import take_screen, find_element

class Actions:
    def __init__(self, driver):
        self.driver = driver

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

    def click_element(self, locator, test_name, take_screenshot=True):
        with allure.step(f"Клик по элементу с локатором {locator}"):
            try:
                take_screen(self.driver, test_name, 'init', take_screenshot)
                element = find_element(self.driver, locator)
                if element:
                    take_screen(self.driver, test_name, 'before_click', take_screenshot)
                    element.click()
                    take_screen(self.driver, test_name, 'after_click', take_screenshot)
                else:
                    take_screen(self.driver, test_name, 'element_not_found', take_screenshot)
            except Exception as ex:
                logging.error(f"Ошибка в click_element: {ex}")
                take_screen(self.driver, test_name, 'error', take_screenshot)

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
