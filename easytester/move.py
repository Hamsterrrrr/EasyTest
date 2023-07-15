import logging
from utils import take_screen, find_element
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s)')

def scroll(driver, direction='up', duration=800, steps=1):
    size = driver.get_window_size()
    start_x = size['width'] // 2
    start_y = size['height'] // 2
    end_x = start_x
    end_y = start_y

    if direction == 'up':
        end_y = size['height'] - 100
    elif direction == 'down':
        end_y = 100
    elif direction == 'left':
        end_x = size['width'] - 100
    elif direction == 'right':
        end_x = 100
    else:
        raise ValueError("Invalid direction. Use 'up', 'down', 'left', or 'right'.")

    for _ in range(steps):
        driver.swipe(start_x, start_y, end_x, end_y, duration)
    
    
def click_element(driver, locator, test_name, take_screenshot=True):
    try:
        if take_screenshot:
            take_screen(driver, test_name)
        element = find_element(driver, locator)
        if element:
            if take_screenshot:
                take_screen(driver, test_name + "_before_click")
            element.click()
            if take_screenshot:
                take_screen(driver, test_name + "_after_click")
        else:
            if take_screenshot:
                take_screen(driver, test_name + "_element_not_found")
    except Exception as _ex:
        if take_screenshot:
            take_screen(driver, test_name + "_error")


def input_text(driver, locator, input_text, test_name, take_screenshot=True):
    try:
        if take_screenshot:
            take_screen(driver, test_name)
        element = find_element(driver, locator)
        if element:
            if take_screenshot:
                take_screen(driver, test_name + "_before_input")
            element.send_keys(input_text)
            if take_screenshot:
                take_screen(driver, test_name + "_after_input")
        else:
            if take_screenshot:
                take_screen(driver, test_name + "_element_not_found")
    except Exception as _ex:
        if take_screenshot:
            take_screen(driver, test_name + "_error")

        
def get_text_from_element(driver, locator, test_name):
    element = find_element(driver, locator)
    text = element.text
    logging.info(f"Text retrieved from element: {text}")
    return text