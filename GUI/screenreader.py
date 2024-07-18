import pyautogui
import cv2
import numpy as np
import time

# 获取屏幕尺寸
screen_width, screen_height = pyautogui.size()
#screen_size = (1920, 1080)
#cv2.namedWindow("Screen Capture", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Screen Capture", screen_size // 2, screen_size // 2)
def fetch_screen():
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()

    # 将截图转换为OpenCV图像格式
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    return image

