import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon

icon = "./Resources/Icons/minecraft_icon.png"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MineGUI")
        self.setGeometry(100, 0, 500, 500)
        self.setWindowIcon(QIcon(icon))
        label = QLabel("Hello", self)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
