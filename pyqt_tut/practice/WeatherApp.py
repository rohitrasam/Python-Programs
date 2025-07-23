import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import requests
import json

"""
TODO: Select city and country
TODO: Search city and country by name
"""

API_KEY = "f3233804c9134949050402bca751ffa9"
UNITS = "metric"
URL = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units={}"

class WeatherApp(qtw.QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.resize(750, 500)
        self.setMaximumSize(750, 500)
        self.input_city = qtw.QLineEdit(self)
        self.submit = qtw.QPushButton("Submit", self)
        self.central_widget = qtw.QWidget()
        self.country_label = qtw.QLabel("Country:")
        self.city_label = qtw.QLabel("City:")
        self.lat_label = qtw.QLabel("Lat:")
        self.long_label = qtw.QLabel("Long:")
        self.temp_label = qtw.QLabel("Temp:")
        self.min_temp_label = qtw.QLabel("Min Temp:")
        self.max_temp_label = qtw.QLabel("Max Temp:")
        self.weather_label = qtw.QLabel("Weather:")
        self.country_output = qtw.QLabel("-")
        self.city_output = qtw.QLabel("-")
        self.lat_output = qtw.QLabel("-")
        self.long_output = qtw.QLabel("-")
        self.temp_output = qtw.QLabel("-")
        self.min_temp_output = qtw.QLabel("-")
        self.max_temp_output = qtw.QLabel("-")
        self.weather_output = qtw.QLabel("-")
        self.error_dialog = qtw.QDialog()

        self.initUI()
    
    def initUI(self) -> None:
        self.setWindowTitle("Weather App")
        self.setCentralWidget(self.central_widget)
        # self.setCentralWidget(self)
        self.setFont(QFont("Calibri", 12))

        self.submit.clicked.connect(self.handle_submit)

        row1 = qtw.QHBoxLayout()
        row1.addWidget(self.input_city)
        row1.addWidget(self.submit)

        row2 = qtw.QGridLayout()
        row2.addWidget(self.country_label, 0, 0, Qt.AlignHCenter)
        row2.addWidget(self.country_output, 0, 1, Qt.AlignmentFlag.AlignLeft)
        row2.addWidget(self.city_label, 1, 0, Qt.AlignHCenter)
        row2.addWidget(self.city_output, 1, 1, Qt.AlignmentFlag.AlignLeft)
        row2.addWidget(self.lat_label, 2, 0, Qt.AlignHCenter)
        row2.addWidget(self.lat_output, 2, 1, Qt.AlignmentFlag.AlignLeft)
        row2.addWidget(self.long_label, 3, 0, Qt.AlignHCenter)
        row2.addWidget(self.long_output, 3, 1, Qt.AlignmentFlag.AlignLeft)
        
        row2.addWidget(self.temp_label, 4, 0, Qt.AlignHCenter)
        row2.addWidget(self.temp_output, 4, 1, Qt.AlignmentFlag.AlignLeft)
        row2.addWidget(self.min_temp_label, 5, 0, Qt.AlignHCenter)
        row2.addWidget(self.min_temp_output, 5, 1, Qt.AlignmentFlag.AlignLeft)
        row2.addWidget(self.max_temp_label, 6, 0, Qt.AlignHCenter)
        row2.addWidget(self.max_temp_output, 6, 1, Qt.AlignmentFlag.AlignLeft)

        row2.addWidget(self.weather_label, 7, 0, Qt.AlignHCenter)
        row2.addWidget(self.weather_output, 7, 1, Qt.AlignmentFlag.AlignLeft)

        main_layout = qtw.QVBoxLayout()

        main_layout.addLayout(row1)
        main_layout.addLayout(row2)

        # self.setLayout(main_layout)
        self.central_widget.setLayout(main_layout)
    
    def handle_submit(self) -> None:
        city = self.input_city.text()
        res: dict = self.get_info(city)
        if res.get("cod") == 200:
            self.populate(res)
        else:
            qtw.QMessageBox().warning(self, f"Error: {res.get("cod")}", f"{res.get("message")}")
           
    def populate(self, info: dict) -> None:
        self.country_output.setText(info["sys"]["country"])
        self.city_output.setText(info["name"])
        self.lat_output.setText(str(info["coord"]["lat"]))
        self.long_output.setText(str(info["coord"]["lon"]))
        self.temp_output.setText(str(info["main"]["temp"])+" C")
        self.min_temp_output.setText(str(info["main"]["temp_min"])+" C")
        self.max_temp_output.setText(str(info["main"]["temp_max"])+" C")
        weather = info["weather"][0]["main"] + ", " + info["weather"][0]["description"]
        self.weather_output.setText(weather)

    def get_info(self, city: str) -> dict:

        res = requests.get(URL.format(city, API_KEY, UNITS))
        res = json.loads(res.text)
        
        return res


def main() -> None:
    app = qtw.QApplication([])
    win = WeatherApp()
    win.show()
    app.exec()

if __name__ == '__main__':

    main()



