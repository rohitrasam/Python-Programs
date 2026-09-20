import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(1000, 500, 500, 500)    # Set the xy position on the screen and the height and width
        # All radio buttons unless exclusively stated are a part of the same group
        self.radio1 = QRadioButton("COD", self)
        self.radio2 = QRadioButton("UPI", self)
        self.radio3 = QRadioButton("Net banking", self)
        self.radio4 = QRadioButton("Paytm Wallet", self)
        self.radio5 = QRadioButton("Gpay Wallet", self)

        self.walletGroup = QButtonGroup(self)

        self.initUI()
        
    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 60, 300, 50)
        self.radio3.setGeometry(0, 120, 300, 50)
        self.radio4.setGeometry(0, 180, 300, 50)
        self.radio5.setGeometry(0, 240, 300, 50)

        self.setStyleSheet("QRadioButton{"
                        "font-size: 40px;"
                        "font-family: Calibri;"
                        "padding: 10px;"
        "}")

        self.walletGroup.addButton(self.radio4)
        self.walletGroup.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_change)
        self.radio2.toggled.connect(self.radio_button_change)
        self.radio3.toggled.connect(self.radio_button_change)
        self.radio4.toggled.connect(self.radio_button_change)
        self.radio5.toggled.connect(self.radio_button_change)

    def radio_button_change(self) -> None:
        radio: QRadioButton = self.sender()   # returns the widget that sent the signal
        if radio.isChecked():
            print(f"{radio.text()} is selected!")


def main() -> None:
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()