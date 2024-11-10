import pyautogui
import time

print("Наведите курсор на нужный элемент в течение 5 секунд...")
time.sleep(5)  # Даем время навести курсор

# Получаем текущие координаты и цвет пикселя под курсором
x, y = pyautogui.position()  # координаты
color = pyautogui.pixel(x, y)  # цвет в формате RGB

print(f"Координаты: ({x}, {y})")
print(f"Цвет пикселя: {color}")
