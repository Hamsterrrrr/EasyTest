from easytest.core.actions import Actions
from easytest.core.utils import find_element


def test_find_and_click_element(driver):
    locator = "easytest/templates/icons/friends.png"
    test_name = "test_click_element"

    screen_path = "current_screen.png"
    driver.get_screenshot_as_file(screen_path)

    Actions.click_element(driver, locator, test_name=test_name, screen_path=screen_path)
