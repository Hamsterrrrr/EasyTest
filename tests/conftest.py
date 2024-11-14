import pytest
from easytest.core.driver import Driver
from easytest.core.actions import Actions

@pytest.fixture(scope="session")
def driver():
    drv = Driver()
    driver = drv.start_driver()
    yield driver
    drv.stop_driver()

@pytest.fixture
def actions(driver):
    return Actions(driver)
