from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options  # Импортируем класс Options для Android

class Driver:
    def __init__(self, desired_capabilities):
        self.server_url = desired_capabilities["server_url"]

        # Создаем объект UiAutomator2Options
        options = UiAutomator2Options()
        for key, value in desired_capabilities["capabilities"].items():
            options.set_capability(key, value)

        # Инициализируем драйвер Appium с использованием options
        self.driver = webdriver.Remote(
            command_executor=self.server_url,
            options=options
        )
