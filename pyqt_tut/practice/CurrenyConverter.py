import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from enum import Enum


# TODO: Change from and to currencies on clicking swap button


class Currency(Enum):

    USD: str = "USD"
    INR: str = "INR"
    AUD: str = "AUD"
    CAD: str = "CAD"
    JPY: str = "JPY"
    EUR: str = "EUR"
    EGP: str = "EGP"


class Window(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.rates = {
            Currency.USD.value: {
                Currency.INR.value: 85.22697,
                Currency.AUD.value: 1.54736,
                Currency.CAD.value: 1.38054,
                Currency.JPY.value: 143.33017,
                Currency.USD.value: 1,
            },
            Currency.INR.value: {
                Currency.USD.value: 0.01173,
                Currency.AUD.value: 0.01815,
                Currency.JPY.value: 1.68125,
                Currency.CAD.value: 0.0162,
                Currency.INR.value: 1
            },
            Currency.AUD.value: {
                Currency.AUD.value: 1,
                Currency.INR.value: 55.09797,
                Currency.USD.value: 0.64651,
                Currency.JPY.value: 92.65801,
                Currency.CAD.value: 0.89262
            },
            Currency.JPY.value: {
                Currency.INR.value: 0.59464,
                Currency.USD.value: 0.28891,
                Currency.JPY.value: 1,
                Currency.AUD.value: 0.01079,
                Currency.CAD.value: 0.00963
            },
            Currency.CAD.value: {
                Currency.INR.value: 61.72584,
                Currency.USD.value: 0.72409,
                Currency.JPY.value: 103.80408,
                Currency.AUD.value: 1.12061,
                Currency.CAD.value: 1
            }
        }
        

        self.font = QFont("Calibri", 12)
        self.combo_from = qtw.QComboBox(self)
        self.label_from = qtw.QLabel("From: ", self)
        self.combo_to = qtw.QComboBox(self)
        self.label_to = qtw.QLabel("To: ", self)
        self.input_from = qtw.QLineEdit(self)
        self.input_to = qtw.QLineEdit(self)
        self.input_label_from = qtw.QLabel(Currency.USD.value)
        self.input_label_to = qtw.QLabel(Currency.INR.value)
        self.swap = qtw.QPushButton("<->",)
        # self.convert_button = qtw.QPushButton("Convert", self)
        self.main_widget = qtw.QWidget()

        self.initUI()

    def initUI(self) -> None:

        self.resize(450, 250)
        self.setMaximumSize(450, 250)
        self.setWindowTitle("Currency Converter")
        self.setWindowIcon(QIcon(r"D:\Python Programs\pyqt_tut\practice\currency.png"))
        self.setFont(self.font)
        self.setCentralWidget(self.main_widget)

        self.combo_from.addItems(self.rates.keys())
        self.combo_to.addItems(self.rates.get(self.combo_from.currentText(), {}).keys())

        # self.convert_button.setMaximumSize(100, 30)
        # self.convert_button.clicked.connect(self.convert)

        self.input_from.setMaximumSize(150, 25)
        self.input_to.setMaximumSize(150, 25)
        self.swap.setMaximumSize(50, 50)
        self.swap.clicked.connect(self.swap_to_from)
        self.input_from.textChanged.connect(self.convert_from)
        self.input_to.textChanged.connect(self.convert_to)
        self.combo_from.currentTextChanged.connect(self.change_from_label)
        self.combo_to.currentTextChanged.connect(self.change_to_label)
        
        
        row1 = qtw.QHBoxLayout()
        row1.addWidget(self.label_from, alignment=Qt.AlignRight)
        row1.addWidget(self.combo_from, alignment=Qt.AlignLeft)
        row1.addWidget(self.label_to, alignment=Qt.AlignRight)
        row1.addWidget(self.combo_to, alignment=Qt.AlignLeft)

        row2 = qtw.QHBoxLayout()
        row2.addWidget(self.input_from, alignment=Qt.AlignRight)
        row2.addWidget(self.input_label_from, alignment=Qt.AlignLeft)
        row2.addWidget(self.swap, alignment=Qt.AlignCenter)
        row2.addWidget(self.input_to, alignment=Qt.AlignRight)
        row2.addWidget(self.input_label_to, alignment=Qt.AlignLeft)

        mainLayout = qtw.QVBoxLayout()
        mainLayout.addLayout(row1)
        mainLayout.addLayout(row2)

        # mainLayout.addWidget(self.convert_button, alignment=Qt.AlignCenter)

        self.main_widget.setLayout(mainLayout)

    # def convert(self) -> None:
    #     conversion_rate = self.rates.get(self.combo_from.currentText(), 0).get(self.combo_to.currentText(), 0)
    #     curr = float(self.input_from.text()) * conversion_rate
    #     self.input_to.setText(str(round(curr, 3)))
    
    def convert_from(self) -> None:
        if self.input_from.hasFocus():
            conversion_rate = self.rates.get(self.combo_from.currentText(), 0).get(self.combo_to.currentText(), 0)
            curr_from = self.input_from.text()
            curr = float(curr_from if curr_from else 0) * conversion_rate
            self.input_to.setText(str(round(curr, 3)))
    
    def convert_to(self) -> None:
        if self.input_to.hasFocus():
            conversion_rate = self.rates.get(self.combo_to.currentText(),0).get(self.combo_from.currentText(), 0)
            curr_to = self.input_to.text()
            curr = float(curr_to if curr_to else 0) * conversion_rate
            self.input_from.setText(str(round(curr, 3)))

    def swap_to_from(self) -> None:
        pass

    def change_from_label(self) -> None:
        self.input_label_from.setText(self.combo_from.currentText())

    def change_to_label(self) -> None:
        self.input_label_to.setText(self.combo_to.currentText())
        

def main() -> None:

    app = qtw.QApplication([])
    win = Window()

    win.show()
    app.exec()

if __name__ == '__main__':

    main()