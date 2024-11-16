import logging
import pytest
from easytest.config.config import Config
from easytest.core.driver import Driver

@pytest.fixture(scope="session")
def config():
    """
    Предоставляет объект Config для тестов.
    """
    return Config()

@pytest.fixture(scope="session")
def driver(config):
    drv = None
    try:
        desired_capabilities = config.get_desired_capabilities()
        print("Инициализируем драйвер с параметрами:", desired_capabilities)  # Отладка

        drv = Driver(desired_capabilities)  # Инициализация драйвера
        yield drv.driver  # Передача драйвера в тесты
    finally:
        if drv is not None:  # Убедимся, что драйвер был инициализирован
            logging.info("Закрываем приложение...")
            drv.driver.quit()  # Закрытие сессии драйвера
        else:
            logging.error("Драйвер не был инициализирован. Пропускаем закрытие.")