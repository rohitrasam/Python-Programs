import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QWidget

class MainWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(1000, 500, 500, 500)    # Set the xy position on the screen and the height and width
        self.lineEdit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self) -> None:
        self.lineEdit.setGeometry(10, 30, 200, 40)
        self.lineEdit.setStyleSheet("font-size: 25px;" \
                                    "font-family: Calibri;")
        self.button.setGeometry(210, 30, 100, 40)
        self.button.setStyleSheet("font-size: 25px;" \
                                    "font-family: Calibri;")
        self.lineEdit.setPlaceholderText("Enter text...")
        self.button.clicked.connect(self.submit)

    def submit(self) -> None:
        text = self.lineEdit.text()
        print(text)


def main() -> None:
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()