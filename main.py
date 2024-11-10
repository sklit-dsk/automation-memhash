import pyautogui
import keyboard
import time
import tkinter as tk
from datetime import datetime
import pygetwindow as gw
import os

# Координаты ползунка и кнопки на экране
x_energy_bar = 1737
y_energy_bar = 351
x_status = 1701
y_status = 372
x_button = 1721
y_button = 469
energy_bar_position = (x_energy_bar, y_energy_bar)
status_position = (x_status, y_status)
button_position = (x_button, y_button)

# RGB цвета для проверки
full_energy_color = (214, 227, 194)
status_color = (228, 120, 102)

# Время ожидания
wait_time = 1800

# Название другого окна, которое должно стать поверх всех
target_window_title = "TelegramDesktop"  # Замените на название окна

# Переменная для паузы
paused = False

def countdown(timer_window, seconds, label):
    def update_timer():
        nonlocal seconds
        if seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer_text = f"Осталось {mins:02}:{secs:02}"
            label.config(text=timer_text)

            if seconds == 15:
                timer_window.attributes("-topmost", True)
                target_window = gw.getWindowsWithTitle(target_window_title)
                if target_window:
                    target_window[0].activate()
                    target_window[0].top = True

            # Планируем обновление через 1 секунду
            timer_window.after(1000, update_timer)
            seconds -= 1
        else:
            label.config(text="Нажатие кнопки!")
            timer_window.after(1000, timer_window.destroy)

    update_timer()  # Запускаем таймер

def check_energy_level():
    current_color = pyautogui.pixel(*energy_bar_position)
    return current_color == full_energy_color

def check_status():
    current_color = pyautogui.pixel(*status_position)
    return current_color == status_color

def toggle_pause():
    global paused
    paused = not paused
    state = "пауза" if paused else "работа"
    print(f"Переключение: {state}")

# Назначаем клавишу ` для паузы
# keyboard.add_hotkey('`', toggle_pause)

print("Нажмите ` для паузы и возобновления")

while True:
    if not paused:
        if check_status():
            print("Low energy!!")
            pyautogui.click(button_position)
            print("Low energy, нажата кнопка Стоп")

            # Создаем окно таймера
            timer_window = tk.Tk()
            timer_window.title("Таймер до нажатия кнопки")
            timer_window.geometry("300x100")

            # Получаем размеры экрана
            screen_width = timer_window.winfo_screenwidth()
            screen_height = timer_window.winfo_screenheight()

            # Вычисляем координаты для правого нижнего угла
            x = screen_width - 320  # Ширина окна + отступ
            y = screen_height - 150  # Высота окна + отступ
            timer_window.geometry(f"300x100+{x}+{y}")

            # Метка для отображения времени
            label = tk.Label(timer_window, text="", font=("Arial", 20))
            label.pack(expand=True)

            # Запускаем таймер в основном потоке с использованием after
            countdown(timer_window, wait_time, label)

            # Запуск окна
            timer_window.mainloop()

            # Нажимаем кнопку снова по завершении таймера
            pyautogui.click(button_position)
            print("Энергия накоплена, нажата кнопка Старт")
            time.sleep(5)
    else:
        print("Программа на паузе")

    time.sleep(1)  # Проверка каждые 1 секунду
