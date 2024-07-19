import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QPushButton
from PyQt5.QtCore import Qt, QRect, QThread, pyqtSignal
#import roboflowAPI
import yoloAPI
import threading as thr
import pyautogui
import keyboard
import win32con, win32api

# Sample JSON data
'''
json_data = 
[
    {"title": "Rectangle 1", "x": 50, "y": 50, "width": 100, "height": 50, "color": "red", "class": "a", "confidence": 0.5},
    {"title": "Rectangle 2", "x": 200, "y": 100, "width": 150, "height": 75, "color": "green", "class": "a", "confidence": 0.5},
    {"title": "Rectangle 3", "x": 400, "y": 150, "width": 120, "height": 60, "color": "blue", "class": "a", "confidence": 0.5}
]
'''
global rects
# rects = [{'x': 50, 'y': 50, 'width': 100, 'height': 50, 'confidence': 0.48032453656196594, 'class': 'human', 'class_id': 3, 'detection_id': '12281778-50ed-496e-9e11-619a68ceae34'}, {'x': 1361.25, 'y': 397.5, 'width': 105.0, 'height': 277.5, 'confidence': 0.4474358856678009, 'class': '107', 'class_id': 0, 'detection_id': '786e9214-99d3-4030-8877-cb8ec6f696b1'}]

# Parse JSON data

#rects = json.loads(json_data)
#print(rects)
#rects = copy.deepcopy(roboflowAPI.fetch_results_by_path())
#print(rects)


global COLOR_INDEX
COLOR_INDEX = {"human": "red", "107": "red", "died": "blue", "114": "blue"}

global aimer_flag
aimer_flag = True


def move_mouse(x, y):
    cx, cy = pyautogui.position()
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, (x-cx), (y-cy))


class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rectangles Display')
        self.screen_width, self.screen_height = pyautogui.size()
        self.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.rects = []
        self.button_list = []
        #self.background_image = QPixmap("test.jpg")
        #self.image_width = self.background_image.width()
        #self.image_height = self.background_image.height()
        #self.setGeometry(0, 0, self.image_width, self.image_height)

        self.center()

        self.repaint()
        self.show()
        self.move(0, 0)
        self.raise_()


    # 主窗口居中
    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    # UI绘制
    def paint_it(self):
        # painter.drawPixmap(self.rect(), self.background_image)
        # rects = copy.deepcopy(roboflowAPI.fetch_results_by_path())
        # self.button_list = []
        order = 0

        for rect in self.rects:

            x, y, width, height, color = int(rect["x"]), int(rect["y"]), int(rect["width"]), int(rect["height"]), COLOR_INDEX[rect["class"]]
            x = x - width // 2
            y = y - height // 2

            #pen = QPen(QColor(color))
            #pen.setWidth(2)  # Set the pen width for the rectangle border


            self.button_list.append(QPushButton(self))

            self.button_list[order].setGeometry(x, y, width, height)
            self.button_list[order].setStyleSheet(""" QPushButton {
                border: 2px solid """ + color + """;
                background-color: rgba(0, 0, 0, 0);
                color: """ + color + """;
            }""")
            self.button_list[order].show()
            # painter.setPen(pen)
            # painter.setBrush(Qt.NoBrush)  # Ensure the rectangles are not filled
            # painter.drawRect(QRect(x, y, width, height))
            # painter.drawText(x + width // 2 - 10, y - 10, rect['class'] + ' ' + str(rect["confidence"]))
            order += 1

    # 删除旧框框
    def closing(self):
        for i in self.button_list:
            i.close()
        self.button_list = []

    def move_cursor(self, rects):
        if aimer_flag:
            if rects:
                history_value = self.screen_width + self.screen_height
                now_index = 0
                for rect in range(len(rects)):
                    distance = int(abs(self.screen_width//2 - rects[rect]['x']) + abs(self.screen_height//2 - rects[rect]['y']))
                    if distance < history_value:
                        history_value = distance
                        now_index = rect

                # now_x, now_y = pyautogui.position()
                move_mouse(int(rects[now_index]['x']), int(rects[now_index]['y']))


    # 窗口总重绘
    def redo(self, rects):
        self.rects = rects
        self.move_cursor(rects)
        self.closing()
        self.paint_it()




class FetchThread(QThread):
    # 获取识别框的线程

    # 将获取数据传回主窗口的信号
    data_fetched = pyqtSignal(list)

    def run(self) -> None:
        while True:
            # 调用yoloAPI跑模型，返回一个get_rects识别框JSON数据，结构如下
            """
            [                       <- 外层大列表，装的是每一个框的信息
            {'x': float,            <- 框框中心x绝对坐标（屏幕上）
             'y': float,            <- 框框中心y绝对坐标
             'width': float,        <- 框宽
             'height': float,       <- 框高
             'confidence': float,   <- 确认概率
             'class': str           <- 属于什么类型，例：human
            },
            ]
            """
            get_rects = yoloAPI.fetch_boxes_by_path()

            # 发射数据信号给主窗口，让主窗口重绘框框
            self.data_fetched.emit(get_rects)
            #time.sleep(1)

class CursorThread(QThread):
    def run(self) -> None:
        pass
        #while True:
        #    if keyboard.is_pressed('i'):
        #        # 获取鼠标当前位置
        #        if aimer_flag:
        #            aimer_flag = False
        #        else:
        #            aimer_flag = True
        #        while keyboard.is_pressed('i'):
        #            pass
        #        time.sleep(0.05)
#
def main():
    # 主窗口线程，隔离线程防止ai卡顿把主程序带崩
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()

    cursor_thread = CursorThread()
    cursor_thread.start()

    # 通过多创建获取框框信息线程来加快刷新速度
    #for i in range(10):
    fetch_thread = FetchThread()
    fetch_thread.data_fetched.connect(window.redo)
    fetch_thread.start()
    #time.sleep(0.05)
    sys.exit(app.exec_())



if __name__ == '__main__':
    gui_thread = thr.Thread(target=main)
    gui_thread.start()
    gui_thread.join()
