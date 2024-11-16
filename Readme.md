# **EasyTest Framework**

**EasyTest Framework** — это мощный инструмент для автоматизированного тестирования мобильных приложений, включающий в себя:

- **Appium** для управления мобильными устройствами.
- **Pytest** для организации структуры тестов.
- **Allure** для создания подробных отчетов о тестировании.
- **Шаблоны изображений** для поиска элементов на экране и взаимодействия с ними через координаты.

---

## **Ключевые особенности**

1. **Поддержка локаторов и изображений**:
   - Поиск элементов с помощью стандартных локаторов (`id`, `xpath`, `class`, `css`).
   - Поиск элементов по шаблонам изображений (например, `load.png`).

2. **Модуль действий (Actions)**:
   - Взаимодействие с элементами: клики, ввод текста и прокрутка.
   - Использование как координат, так и стандартных локаторов.

3. **Интеграция с Allure**:
   - Детализированные шаги тестов с прикреплением скриншотов.

4. **Шаблоны изображений**:
   - Использование OpenCV для поиска элементов на экране.

5. **Простая настройка конфигурации**:
   - Все параметры тестирования настраиваются через JSON.

---

## **Установка**

1. Убедитесь, что установлен **Python 3.7+**.
2. Установите фреймворк:
   ```bash
   pip install easytest-framework
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Настройте файл `driver_config.json`:
   ```json
   {
       "android": {
           "local": {
               "stage": {
                   "platformName": "Android",
                   "deviceName": "emulator-5554",
                   "appPackage": "com.example.app",
                   "appActivity": "com.example.app.MainActivity",
                   "automationName": "UiAutomator2",
                   "noReset": true,
                   "newCommandTimeout": 600,
                   "APPIUM_SERVER_URL": "http://127.0.0.1:4723/wd/hub"
               }
           }
       }
   }
   ```
5. Запустите сервер Appium:
   ```bash
   appium
   ```

---

## **Использование**

### **Функции**

1. **`click_element`**
   - Выполняет клик по элементу с использованием координат или локаторов.
   - Пример:
     ```python
     from easytest.core.actions import Actions

     def test_click_element(driver):
         actions = Actions(driver)
         
         # Клик с использованием локатора
         locator = "id=com.example:id/button"
         actions.click_element(locator, test_name="test_button_click")

         # Клик с использованием шаблона изображения
         image_template = "templates/icons/button.png"
         actions.click_element(image_template, test_name="test_image_click", take_screenshot=True)
     ```

2. **`wait_for_element_to_appear`**
   - Ожидает появления элемента (шаблона изображения) на экране.
   - Пример:
     ```python
     load_template = "templates/icons/load.png"
     actions.wait_for_element_to_appear(load_template, timeout=10)
     ```

3. **`wait_for_element_to_disappear`**
   - Ожидает исчезновения элемента (шаблона изображения) с экрана.
   - Пример:
     ```python
     load_template = "templates/icons/load.png"
     actions.wait_for_element_to_disappear(load_template, timeout=30)
     ```

4. **`scroll`**
   - Прокручивает экран в указанном направлении.
   - Пример:
     ```python
     actions.scroll(direction='up', duration=800, steps=1)
     ```

5. **`input_text`**
   - Вводит текст в элемент.
   - Пример:
     ```python
     locator = "id=com.example:id/input_field"
     actions.input_text(locator, "Hello, World!", test_name="test_input_text")
     ```

6. **`get_text_from_element`**
   - Получает текст из элемента.
   - Пример:
     ```python
     locator = "id=com.example:id/text_view"
     text = actions.get_text_from_element(locator, test_name="test_get_text")
     print(f"Текст элемента: {text}")
     ```

---

## **Пример теста**

```python
from easytest.core.actions import Actions

def test_find_and_click_element(driver):
    actions = Actions(driver)

    # Ожидание завершения загрузки
    load_template = "templates/icons/load.png"
    actions.wait_for_element_to_appear(load_template, timeout=10)
    actions.wait_for_element_to_disappear(load_template, timeout=30)

    # Клик по элементу с использованием шаблона изображения
    friends_template = "templates/icons/friends.png"
    actions.click_element(friends_template, test_name="test_friends_icon", take_screenshot=True)
```

---

## **Команды**

- **Запуск тестов**:
  ```bash
  pytest --alluredir=./allure-results
  ```
- **Просмотр отчетов Allure**:
  ```bash
  allure serve ./allure-results
  ```

---

## **Лицензия**

Этот проект распространяется под **лицензией MIT**.
