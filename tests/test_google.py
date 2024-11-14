import pytest
from easytest.core.actions import Actions
from easytest.core.driver import Driver
from easytest.core.utils import find_element

@pytest.fixture
def driver():
    drv = Driver()
    driver = drv.start_driver()
    yield driver
    drv.stop_driver()

def test_google_search(driver):
    actions = Actions(driver)
    search_box_locator = ("id", "com.google.android.googlequicksearchbox:id/search_box")
    search_input_locator = ("id", "com.google.android.googlequicksearchbox:id/search_box_text_input")
    search_result_locator = ("id", "com.google.android.googlequicksearchbox:id/googleapp_search_box_text")

    # Кликнуть на поисковую строку
    actions.click_element(search_box_locator, "Open Search Box")

    # Ввести запрос в поисковую строку
    actions.input_text(search_input_locator, "OpenAI", "Enter Search Query")

    # Проверка наличия результатов
    assert find_element(driver, search_result_locator), "Search results should appear"

