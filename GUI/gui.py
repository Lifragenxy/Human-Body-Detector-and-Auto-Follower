import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class ShooterGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口图标
        self.setWindowIcon(QIcon("icon.jpg"))

        # 设置窗口标题
        self.setWindowTitle("100% Shooter")

        # 设置主窗口大小和位置
        self.setGeometry(100, 100, 1200, 900)

        # 锁定窗口大小
        self.setFixedSize(self.size())

        # 设置主题色为黑色
        self.setStyleSheet("background-color: black; color: white;")
        # 创建垂直布局容器
        central_widget = QWidget()
        vbox = QVBoxLayout(central_widget)

        # 创建一个纯文本标签
        self.text_label = QLabel(
            "Don't use this software for any strange purpose!!!")
        self.text_label.setFont(QFont("SimHei", 16))
        self.text_label.setStyleSheet("color: red;")
        vbox.addWidget(self.text_label)


        # 创建一个 QLabel 用于显示图片
        self.label = QLabel()
        self.label.setPixmap(QPixmap("background.jpg"))
        self.label.setScaledContents(True)


        # 将 label 添加到布局容器中
        vbox.addWidget(self.label)

        # 创建启动和退出按钮
        start_button = QPushButton("Launch")
        start_button.setFont(QFont("SimHei", 24, QFont.Bold))
        start_button.clicked.connect(self.start_program)

        exit_button = QPushButton("Exit")
        exit_button.setFont(QFont("SimHei", 24, QFont.Bold))
        exit_button.clicked.connect(self.exit_program)

        # 创建一个纯文本标签
        self.text_label = QLabel("Find project in Github: https://github.com/Lifragenxy/Human-Body-Detector-and-Auto-Follower")
        self.text_label.setFont(QFont("SimHei", 16))
        vbox.addWidget(self.text_label)

        # 将按钮添加到布局容器
        vbox.addWidget(start_button)
        vbox.addWidget(exit_button)

        # 设置居中布局
        vbox.setAlignment(Qt.AlignCenter)

        # 设置中心窗口小部件
        self.setCentralWidget(central_widget)

    def start_program(self):
        # 在这里添加启动程序的代码
        print("启动程序")

    def exit_program(self):
        # 在这里添加退出程序的代码
        print("退出程序")
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = ShooterGUI()
    gui.show()
    sys.exit(app.exec_())