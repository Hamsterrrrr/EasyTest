from easytest.core.actions import Actions
import time


def test_find_and_click_element(driver):
    actions = Actions(driver)

    # Ожидание появления изображения загрузки
    load_template = "easytest/templates/icons/load.png"
    actions.wait_for_element_to_appear(load_template, timeout=30)

    # Ожидание исчезновения изображения загрузки
    actions.wait_for_element_to_disappear(load_template, timeout=3000)

    # Локатор для шаблона изображения
    locator = "easytest/templates/icons/friends.png"

    # Клик по элементу или координатам
    actions.click_element(locator, test_name="test_friends_icon", take_screenshot=True)

