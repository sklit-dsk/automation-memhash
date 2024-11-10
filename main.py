import pyautogui
import keyboard
import time

x_energy_bar = 1737
y_energy_bar = 351
x_status = 1712
y_status = 486
x_button = 1740
y_button = 573

wait_time = 2400

# Координаты ползунка и кнопки на экране
energy_bar_position = (x_energy_bar, y_energy_bar)  # замените x и y на координаты ползунка
status_position = (x_status, y_status)
button_position = (x_button, y_button)  # замените a и b на координаты кнопки "Старт-стоп"

# RGB цвет полностью накопленной энергии (укажите цвет, который отображается при полном уровне)
full_energy_color = (214, 227, 194)  # замените r, g, b на реальные значения RGB
status_color = (228, 120, 102) 

# Переменная для отслеживания состояния паузы
paused = False

def countdown(seconds):
    while seconds > 0:
        print(f"Осталось {seconds} секунд до нажатия на кнопку...", end="\r")
        time.sleep(1)
        seconds -= 1
    print()  # Перевод строки после завершения отсчета

def check_energy_level():
    # Получаем цвет пикселя на позиции ползунка энергии
    current_color = pyautogui.pixel(*energy_bar_position)
    # Проверяем, совпадает ли цвет с ожидаемым цветом полностью накопленной энергии
    return current_color == full_energy_color

def check_status():
    # Получаем цвет пикселя на позиции статуса
    current_color = pyautogui.pixel(*status_position)
    # Проверяем, совпадает ли цвет с ожидаемым цветом статуса
    return current_color == status_color

# Обработчик для переключения состояния паузы
def toggle_pause():
    global paused
    paused = not paused
    state = "пауза" if paused else "работа"
    print(f"Переключение: {state}")

# Назначаем клавишу  для переключения паузы
# keyboard.add_hotkey('', toggle_pause)

print("Нажмите  для паузы и возобновления")

while True:
    if not paused:
        if check_status():
            print("Low energy!!")
            pyautogui.click(button_position)
            print("Low energy, нажата кнопка Стоп")
            # Ожидание, чтобы дать время энергии снова накапливаться
            # Отсчет времени до следующего нажатия
            countdown(wait_time)
            # Нажимаем кнопку снова
            pyautogui.click(button_position)
            print("Энергия накоплена, нажата кнопка Старт")
        # if check_energy_level():
        #     # Нажимаем на кнопку "Старт-стоп"
        #     pyautogui.click(button_position)
        #     print("Полная энергия, нажата кнопка Старт-стоп")
        #     # Ожидание, чтобы дать время энергии снова накапливаться
        #     time.sleep(600)
    else:
        print("Программа на паузе")

    time.sleep(1)  # Проверка каждые 1 секунду