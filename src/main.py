import sys
import requests
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Погода")
        self.setWindowIcon(QIcon('src/image/weather.png'))

        self.ui.city_inp_le.setPlaceholderText("Введите город")
        self.ui.city_inp_le.editingFinished.connect(lambda: self.show_weather())

    def show_weather(self):
        city = self.ui.city_inp_le.text()
        url = "http://api.weatherapi.com/v1/current.json?key=d193b5efdd7a4a5f889150054242302&q="+city
        weather_data = requests.get(url).json()

        temp_c = round(weather_data['current']['temp_c'])
        temp_f = round(weather_data['current']['temp_f'])
        wind_mph = round(weather_data['current']['wind_mph'])
        wind_direction = weather_data['current']['wind_dir']

        match wind_direction:
            case "N":
                wind_direction = "🠣 С"
            case "NNE":
                wind_direction = "⭩ ССВ"
            case "NE":
                wind_direction = "⭩ СВ"
            case "ENE":
                wind_direction = "⭩ ВСВ"
            case "E":
                wind_direction = "🠠 В"
            case "ESE":
                wind_direction = "⭦ ВЮВ"
            case "SE":
                wind_direction = "⭦ ЮВ"
            case "SSE":
                wind_direction = "⭦ ЮЮВ"
            case "S":
                wind_direction = "🠡 Ю"
            case "SSW":
                wind_direction = "⭧ ЮЮЗ"
            case "SW":
                wind_direction = "⭧ ЮЗ"
            case "WSW":
                wind_direction = "⭧ ЗЮЗ"
            case "W":
                wind_direction = "🠢 З"
            case "WNW":
                wind_direction = "⭨ ЗСЗ"
            case "NW":
                wind_direction = "⭨ СЗ"
            case "WWN":
                wind_direction = "⭨ ССЗ"

        self.ui.temp_c_out_lb.setText(str(temp_c))
        self.ui.temp_f_out_lb.setText(str(temp_f))
        self.ui.wind_vel_out_lb.setText(str(wind_mph))
        self.ui.wind_rumb_out_lb.setText(wind_direction)


app = QtWidgets.QApplication([])
application = Main()
application.show()

sys.exit(app.exec_())
