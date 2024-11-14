from appium import webdriver
from appium.options.android import UiAutomator2Options
from easytest.config.config import Config  # Предполагается, что Config находится в config.py
import logging

class Driver:
    def __init__(self):
        self.driver = None

    def start_driver(self):
        # Загружаем конфигурацию
        config = Config()  # Заданы platform="android", environment="local", mode="stage" по умолчанию
        desired_caps = config.get_desired_capabilities()

        if not desired_caps:
            raise ValueError("Не удалось загрузить настройки из конфигурации. Проверьте JSON файл.")

        logging.info(f"Запуск драйвера с параметрами: {desired_caps}")

        # Устанавливаем параметры для UiAutomator2
        options = UiAutomator2Options()
        for key, value in desired_caps.items():
            options.set_capability(key, value)

        # Инициализируем Appium драйвер с UiAutomator2Options
        self.driver = webdriver.Remote(desired_caps["APPIUM_SERVER_URL"], options=options)

        return self.driver

    def stop_driver(self):
        if self.driver:
            self.driver.quit()



