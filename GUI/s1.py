import pyautogui
import time


def move_mouse(x, y):
    pyautogui.moveTo(x, y)


def click_left_button():
    pyautogui.click(button='left')


def main():
    while True:
        if pyautogui.rightClick():
            # 获取鼠标当前位置
            x, y = pyautogui.position()

            # 移动鼠标指针到目标位置
            move_mouse(x, y)

            # 激活鼠标右键同时按下鼠标左键
            click_left_button()

        time.sleep(0.1)  # 控制循环速度


if __name__ == '__main__':
    main()