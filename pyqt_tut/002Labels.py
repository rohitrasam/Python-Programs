import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(1000, 500, 500, 500)    # Set the xy position on the screen and the height and width

        label = QLabel("Hey Bro", self)
        label.setFont(QFont("Calibri", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: dodgerblue;"
                            "background-color: azure;"
                            "font-weight: bold;"
                            "font-style: italic;")
        
        # label.setAlignment(Qt.AlignmentFlag.AlignTop)
        # label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        # label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        # label.setAlignment(Qt.AlignmentFlag.AlignRight)
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

def main() -> None:
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()