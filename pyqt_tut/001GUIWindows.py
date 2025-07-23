import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt5 Tutorial for CERN")
        self.setGeometry(1000, 500, 500, 500)    # Set the xy position on the screen and the height and width
        self.setWindowIcon(QIcon(rf"D:\PixelArt\orb.png"))

def main() -> None:
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()