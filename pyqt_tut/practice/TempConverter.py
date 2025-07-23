import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class Window(qtw.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temperature Converter")
        self.resize(400, 300)
        self.in_label = qtw.QLabel("Celsius")
        self.out_label = qtw.QLabel("Farenheit")
        self.input = qtw.QLineEdit("0")
        self.out = qtw.QLabel("0")
        self.cel_2_faren = qtw.QRadioButton("Celsius -> Farenheit")
        self.faren_2_cel = qtw.QRadioButton("Farenheit -> Celsius")
        self.convert = qtw.QPushButton("Convert")
        self.central_wid = qtw.QWidget()
    
        self.initUI()


    def initUI(self) -> None:
        
        self.setFont(QFont("Calibri", pointSize=11))
        self.setCentralWidget(self.central_wid)
        master_layout = qtw.QVBoxLayout()
        row0 = qtw.QHBoxLayout()
        row1 = qtw.QHBoxLayout()
        row2 = qtw.QHBoxLayout()
        row3 = qtw.QHBoxLayout()

        self.cel_2_faren.setChecked(True)
        self.cel_2_faren.toggled.connect(self.set_conversion)
        self.faren_2_cel.toggled.connect(self.set_conversion)
        row0.addWidget(self.cel_2_faren, alignment=Qt.AlignmentFlag.AlignCenter)
        row0.addWidget(self.faren_2_cel, alignment=Qt.AlignmentFlag.AlignCenter)

        row1.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignCenter)
        row1.addWidget(self.in_label, alignment=Qt.AlignmentFlag.AlignCenter)

        row2.addWidget(self.out, alignment=Qt.AlignmentFlag.AlignCenter)
        row2.addWidget(self.out_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.cel_to_faren()

        row3.addWidget(self.convert, alignment=Qt.AlignmentFlag.AlignCenter)
        self.convert.clicked.connect(self.cel_to_faren)

        master_layout.addLayout(row0)
        master_layout.addLayout(row1)
        master_layout.addLayout(row2)
        master_layout.addLayout(row3)

        self.central_wid.setLayout(master_layout)

    def cel_to_faren(self) -> None:
        cel: float = float(self.input.text())
        faren = (cel * 1.8) + 32
        faren = round(faren, 2)
        self.out.setText(str(faren))

    def faren_to_cel(self) -> None:
        faren: float = float(self.input.text())
        cel = (faren - 32) / 1.8
        cel = round(cel, 2)
        self.out.setText(str(cel))

    def set_conversion(self) -> None:
        button: qtw.QRadioButton = self.sender()

        if button.text() == "Celsius -> Farenheit":
            self.convert.clicked.connect(self.cel_to_faren)
            self.in_label.setText("Celsius")
            self.out_label.setText("Farenheit")
            self.cel_to_faren()
        else:
            self.convert.clicked.connect(self.faren_to_cel)
            self.in_label.setText("Farenheit")
            self.out_label.setText("Celsius")
            self.faren_to_cel()

def main() -> None:
    app = qtw.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()