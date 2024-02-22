from pyautogui import screenshot
import time
from PIL import ImageGrab


def get_screenshot():
    time.sleep(5)
    shot = screenshot()
    shot.save("my_screenshot.png")


def get_screenshot_area():
    area = (0, 0, 1000, 1000)  # left, up, right, low
    time.sleep(5)
    shot = ImageGrab.grab(area)
    shot.save("my_screenshot_area.png")


# get_screenshot_area()
get_screenshot()
