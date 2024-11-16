import cv2
import allure
from typing import Tuple, Optional
import numpy as np

class ImageComparator:
    @staticmethod
    def find_template_on_screen(screen_path: str, template_path: str, threshold: float = 0.8, scale_steps: int = 5) -> Optional[Tuple[int, int]]:
        screen = cv2.imread(screen_path)
        template = cv2.imread(template_path)

        if screen is None or template is None:
            raise FileNotFoundError("Экран или шаблонное изображение не найдено.")

        for scale in np.linspace(0.5, 1.5, scale_steps):
            resized_template = cv2.resize(template, (0, 0), fx=scale, fy=scale)
            result = cv2.matchTemplate(screen, resized_template, cv2.TM_CCOEFF_NORMED)
            
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            if max_val >= threshold:
                center_x = max_loc[0] + resized_template.shape[1] // 2
                center_y = max_loc[1] + resized_template.shape[0] // 2

                screen_copy = screen.copy()
                cv2.rectangle(
                    screen_copy,
                    max_loc,
                    (max_loc[0] + resized_template.shape[1], max_loc[1] + resized_template.shape[0]),
                    (0, 255, 0), 2
                )
                annotated_path = "annotated_screen.png"
                cv2.imwrite(annotated_path, screen_copy)
                with open(annotated_path, "rb") as file:
                    allure.attach(file.read(), name="Screen with Template Location", attachment_type=allure.attachment_type.PNG)

                return center_x, center_y

        return None


