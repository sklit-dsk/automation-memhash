import pyautogui
import keyboard
import time
import tkinter as tk
from threading import Thread

# Координаты ползунка и кнопки на экране
x_energy_bar = 1737
y_energy_bar = 351
x_status = 1712
y_status = 486
x_button = 1740
y_button = 573
energy_bar_position = (x_energy_bar, y_energy_bar)
status_position = (x_status, y_status)
button_position = (x_button, y_button)

# RGB цвета для проверки
full_energy_color = (214, 227, 194)
status_color = (228, 120, 102)

# Время ожидания
wait_time = 2400

# Переменная для паузы
paused = False

def countdown(seconds):
    # Создаем окно таймера
    timer_window = tk.Tk()
    timer_window.title("Таймер до нажатия кнопки")
    timer_window.geometry("300x100")

    # Получаем размеры экрана
    screen_width = timer_window.winfo_screenwidth()
    screen_height = timer_window.winfo_screenheight()

    # Вычисляем координаты для правого нижнего угла
    x = screen_width - 340  # Ширина окна + отступ
    y = screen_height - 200  # Высота окна + отступ
    timer_window.geometry(f"330x100+{x}+{y}")

    # Метка для отображения времени
    label = tk.Label(timer_window, text="", font=("Arial", 20))
    label.pack(expand=True)

    def update_timer():
        nonlocal seconds
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer_text = f"Осталось {mins:02}:{secs:02} до старта"
            label.config(text=timer_text)
            time.sleep(1)
            seconds -= 1
            timer_window.update_idletasks()  # Обновляем окно
        # Завершение отсчета
        label.config(text="Нажатие кнопки!")
        time.sleep(1)
        timer_window.destroy()  # Закрываем окно таймера

    # Запускаем таймер в отдельном потоке
    countdown_thread = Thread(target=update_timer)
    countdown_thread.start()
    timer_window.mainloop()

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
            
            # Запускаем таймер в отдельном окне
            countdown(wait_time)
            
            # Нажимаем кнопку снова по завершении таймера
            pyautogui.click(button_position)
            print("Энергия накоплена, нажата кнопка Старт")
    else:
        print("Программа на паузе")

    time.sleep(1)  # Проверка каждые 1 секунду
