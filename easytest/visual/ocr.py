import pytesseract
import cv2
import allure
from typing import Optional, Tuple

class OCR:
    @staticmethod
    def extract_text_from_image(image_path: str) -> str:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError("Изображение для OCR не найдено.")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # Бинаризация для улучшения контраста
        
        text = pytesseract.image_to_string(binary, lang="eng")
        allure.attach(text, name="Extracted Text", attachment_type=allure.attachment_type.TEXT)
        with open(image_path, "rb") as file:
            allure.attach(file.read(), name="Исходное изображение для OCR", attachment_type=allure.attachment_type.PNG)
        
        return text

    @staticmethod
    def find_text_position(screen_path: str, search_text: str) -> Optional[Tuple[int, int]]:
        img = cv2.imread(screen_path)
        
        if img is None:
            raise FileNotFoundError("Изображение для OCR не найдено")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
        for i, text in enumerate(data['text']):
            if search_text.lower() in text.lower():
                x = data['left'][i]
                y = data['top'][i]
                w = data['width'][i]
                h = data['height'][i]
                center_x = x + w // 2
                center_y = y + h // 2
                with open(screen_path, "rb") as file:
                    allure.attach(file.read(), name="Screen with Text", attachment_type=allure.attachment_type.JPG)
                return center_x, center_y
        return None

