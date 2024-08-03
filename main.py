import pyautogui
import pyscreeze
import keyboard
import time
from PIL import Image

work = False

def get_position():
    start = time.time()
    position = pyautogui.position()
    screenshot = pyautogui.screenshot(region=[position[0], position[1], 10, 10]).getpixel((3, 3))
    print(position, screenshot)
    finish = time.time()
    print(f'Время работы: {str(finish-start)}')
    

def change_clicker():
    global work
    work = not work
    if work:
        print("\nВключен")
    else:
        print("\nВыключен")

def find_color(screen: Image):
    for i in range(0, 471, 25):
        for j in range(0, 121, 15):
            color = screen.getpixel((i, j))
            if color[0] in range(80, 180) and color[1] - color[2] > 70:
                pyautogui.click(i, j+430)

def clicker():
    start = time.time()
    find_color(pyautogui.screenshot(region=[0, 430, 471, 121]))
    finish = time.time()
    end_time = finish-start
    if end_time < 0.1:
        pyautogui.click(140, 763)
    print(f'Работа круга: {end_time}')

def main():
    keyboard.add_hotkey('`', change_clicker)
    keyboard.add_hotkey('=', get_position)
    try:
        while True:
            if work:
                clicker()

    except KeyboardInterrupt:
        print('\nВыход из программы')


if __name__ == '__main__':
    main()