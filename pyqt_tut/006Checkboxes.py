import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(1000, 500, 500, 500)    # Set the xy position on the screen and the height and width
        self.checkbox = QCheckBox("Do you like Python?", self)
        self.initUI()

    def initUI(self) -> None:
        self.checkbox.setGeometry(10, 40, 500, 200)
        self.checkbox.setStyleSheet("font-size: 40px;"
                                    "font-family: Calibri;")
        self.checkbox.setChecked(False)

        # functionality
        self.checkbox.stateChanged.connect(self.on_check)

    def on_check(self, state: int) -> None:
        if state == Qt.CheckState.Checked:
            print("You like food!")
        else:
            print("You do not like food!")



def main() -> None:
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()