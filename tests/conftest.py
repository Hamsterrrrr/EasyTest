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
    """
    Инициализирует драйвер Appium и завершает сессию после тестов.
    """
    desired_capabilities = config.get_desired_capabilities()
    print("Инициализируем драйвер с параметрами:", desired_capabilities)  # Отладка

    drv = Driver(desired_capabilities)
    yield drv.driver
    drv.driver.quit()
