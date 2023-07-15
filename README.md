# EasyTest

EasyTest is a Python library designed to simplify the process of writing automated tests for web and mobile applications. It provides a set of easy-to-use functions for common testing tasks such as finding elements, clicking elements, inputting text, and taking screenshots.

Whether you're testing a website with Selenium WebDriver or a mobile application with Appium, EasyTest can help you write your tests faster and with less code. It's compatible with both Selenium and Appium, making it a versatile tool for any tester's toolkit.

The library also integrates with Allure, a flexible and lightweight tool for generating test reports in multiple languages, to provide detailed and informative test reports. This makes understanding test results and debugging any issues that arise during testing easier.

With EasyTest, you can focus more on designing your tests rather than the low-level details of interacting with your application. It's a great way to make your testing process more efficient and effective.

EasyTest - это библиотека Python, разработанная для упрощения процесса написания автоматизированных тестов для веб- и мобильных приложений. Она предоставляет набор простых в использовании функций для общих задач тестирования, таких как поиск элементов, клик по элементам, ввод текста и создание скриншотов.

Будь то тестирование веб-сайта с помощью Selenium WebDriver или мобильного приложения с помощью Appium, EasyTest может помочь вам быстрее и с меньшим количеством кода написать ваши тесты. Она совместима как с Selenium, так и с Appium, что делает ее универсальным инструментом для любого набора инструментов тестировщика.

Библиотека также интегрируется с Allure, гибким и легким инструментом для создания тестовых отчетов на нескольких языках, чтобы предоставить подробные и информативные отчеты о тестировании. Это облегчает понимание результатов тестов и отладку любых проблем, возникающих во время тестирования.

С EasyTest вы можете сосредоточиться больше на проектировании ваших тестов, а не на низкоуровневых деталях взаимодействия с вашим приложением. Это отличный способ сделать ваш процесс тестирования более эффективным и эффективным.

Usage

Here's a simple example of how you can use EasyTest to write a test for a web application:

python

from easytest import click_element, input_text, find_element
from selenium import webdriver

driver = webdriver.Firefox()

### Find an element
element = find_element(driver, ("id", "myElement"))

### Click an element
click_element(driver, ("id", "myButton"))

### Input text
input_text(driver, ("id", "myInput"), "Hello, World!")

## Functions

### `find_element(driver, locator) -> WebElement`

This function is used to find an element on the page. It takes two arguments:

- `driver`: The WebDriver instance.
- `locator`: A tuple containing the method to locate the element and the value. The method can be one of the following: "id", "class_name", "xpath", "name", "css", "tag_name", "link_text", "partial_link_text".

This function returns a WebElement if the element is found, or None if it's not.

### `click_element(driver, locator, take_screenshot=True)`

This function is used to click an element on the page. It takes three arguments:

- `driver`: The WebDriver instance.
- `locator`: A tuple containing the method to locate the element and the value.
- `take_screenshot` (optional): A boolean indicating whether to take a screenshot before and after clicking the element. Default is True.

### `input_text(driver, locator, input_text, take_screenshot=True)`

This function is used to input text into an element on the page. It takes four arguments:

- `driver`: The WebDriver instance.
- `locator`: A tuple containing the method to locate the element and the value.
- `input_text`: The text to input into the element.
- `take_screenshot` (optional): A boolean indicating whether to take a screenshot before and after inputting the text. Default is True.

### `scroll(driver, direction='up', duration=800, steps=1)`

This function is used to scroll the page. It takes four arguments:

- `driver`: The WebDriver instance.
- `direction` (optional): The direction to scroll. Can be "up", "down", "left", or "right". Default is "up".
- `duration` (optional): The duration of the scroll in milliseconds. Default is 800.
- `steps` (optional): The number of times to perform the scroll. Default is 1.

### `take_screen(driver, test_name)`

This function is used to take a screenshot of the page. It takes two arguments:

- `driver`: The WebDriver instance.
- `test_name`: The name of the test. This is used to name the screenshot file.


## Example
```python
from easytest import find_element, click_element, input_text, scroll, take_screen

# Create a WebDriver instance
driver = ...

# Use the functions from easytest
element = find_element(driver, ("id", "my-element"))
click_element(driver, ("id", "my-button"))
input_text(driver, ("id", "my-input"), "Hello, world!")
scroll(driver, direction='down')
take_screen(driver, "my_test")
```