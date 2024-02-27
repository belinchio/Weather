from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 175)
        MainWindow.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
                                 "border-radius: 5;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-radius: 5;")
        self.centralwidget.setObjectName("centralwidget")
        self.city_lb = QtWidgets.QLabel(self.centralwidget)
        self.city_lb.setGeometry(QtCore.QRect(0, 0, 200, 35))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.city_lb.setFont(font)
        self.city_lb.setStyleSheet("background-color: #12c7a3;\n"
                                   "color: #3f4d4a;\n"
                                   "border: 1px solid #118c74;\n"
                                   "border-radius: 5;")
        self.city_lb.setObjectName("city_lb")
        self.temp_c_lb = QtWidgets.QLabel(self.centralwidget)
        self.temp_c_lb.setGeometry(QtCore.QRect(0, 35, 200, 35))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.temp_c_lb.setFont(font)
        self.temp_c_lb.setStyleSheet("background-color: #12c7a3;\n"
                                     "color: #3f4d4a;\n"
                                     "border: 1px solid #118c74;\n"
                                     "border-radius: 5;")
        self.temp_c_lb.setObjectName("temp_c_lb")
        self.temp_f_lb = QtWidgets.QLabel(self.centralwidget)
        self.temp_f_lb.setGeometry(QtCore.QRect(0, 70, 200, 35))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.temp_f_lb.setFont(font)
        self.temp_f_lb.setStyleSheet("background-color: #12c7a3;\n"
                                     "color: #3f4d4a;\n"
                                     "border: 1px solid #118c74;\n"
                                     "border-radius: 5;")
        self.temp_f_lb.setObjectName("temp_f_lb")
        self.wind_vel_lb = QtWidgets.QLabel(self.centralwidget)
        self.wind_vel_lb.setGeometry(QtCore.QRect(0, 105, 200, 35))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.wind_vel_lb.setFont(font)
        self.wind_vel_lb.setStyleSheet("background-color: #12c7a3;\n"
                                       "color: #3f4d4a;\n"
                                       "border: 1px solid #118c74;\n"
                                       "border-radius: 5;")
        self.wind_vel_lb.setObjectName("wind_vel_lb")
        self.wind_rumb_lb = QtWidgets.QLabel(self.centralwidget)
        self.wind_rumb_lb.setGeometry(QtCore.QRect(0, 140, 200, 35))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.wind_rumb_lb.setFont(font)
        self.wind_rumb_lb.setStyleSheet("background-color: #12c7a3;\n"
                                        "color: #3f4d4a;\n"
                                        "border: 1px solid #118c74;\n"
                                        "border-radius: 5;")
        self.wind_rumb_lb.setObjectName("wind_rumb_lb")
        self.temp_c_out_lb = QtWidgets.QLabel(self.centralwidget)
        self.temp_c_out_lb.setGeometry(QtCore.QRect(200, 35, 200, 35))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.temp_c_out_lb.setFont(font)
        self.temp_c_out_lb.setStyleSheet("background-color: #12c7a3;\n"
                                         "color: #3f4d4a;\n"
                                         "border: 1px solid #118c74;\n"
                                         "border-radius: 5;")
        self.temp_c_out_lb.setText("")
        self.temp_c_out_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_c_out_lb.setObjectName("temp_c_out_lb")
        self.temp_f_out_lb = QtWidgets.QLabel(self.centralwidget)
        self.temp_f_out_lb.setGeometry(QtCore.QRect(200, 70, 200, 35))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.temp_f_out_lb.setFont(font)
        self.temp_f_out_lb.setStyleSheet("background-color: #12c7a3;\n"
                                         "color: #3f4d4a;\n"
                                         "border: 1px solid #118c74;\n"
                                         "border-radius: 5;")
        self.temp_f_out_lb.setText("")
        self.temp_f_out_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_f_out_lb.setObjectName("temp_f_out_lb")
        self.wind_vel_out_lb = QtWidgets.QLabel(self.centralwidget)
        self.wind_vel_out_lb.setGeometry(QtCore.QRect(200, 105, 200, 35))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.wind_vel_out_lb.setFont(font)
        self.wind_vel_out_lb.setStyleSheet("background-color: #12c7a3;\n"
                                           "color: #3f4d4a;\n"
                                           "border: 1px solid #118c74;\n"
                                           "border-radius: 5;\n"
                                           "")
        self.wind_vel_out_lb.setText("")
        self.wind_vel_out_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.wind_vel_out_lb.setObjectName("wind_vel_out_lb")
        self.wind_rumb_out_lb = QtWidgets.QLabel(self.centralwidget)
        self.wind_rumb_out_lb.setGeometry(QtCore.QRect(200, 140, 200, 35))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.wind_rumb_out_lb.setFont(font)
        self.wind_rumb_out_lb.setStyleSheet("background-color: #12c7a3;\n"
                                            "color: #3f4d4a;\n"
                                            "border: 1px solid #118c74;\n"
                                            "border-radius: 5;")
        self.wind_rumb_out_lb.setText("")
        self.wind_rumb_out_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.wind_rumb_out_lb.setObjectName("wind_rumb_out_lb")
        self.city_inp_le = QtWidgets.QLineEdit(self.centralwidget)
        self.city_inp_le.setGeometry(QtCore.QRect(200, 0, 200, 35))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.city_inp_le.setFont(font)
        self.city_inp_le.setStyleSheet("background-color: #12c7a3;\n"
                                       "color: #3f4d4a;\n"
                                       "border: 1px solid #118c74;\n"
                                       "border-radius: 5;")
        self.city_inp_le.setAlignment(QtCore.Qt.AlignCenter)
        self.city_inp_le.setObjectName("city_inp_le")
        self.temp_c_lb.raise_()
        self.wind_vel_out_lb.raise_()
        self.city_lb.raise_()
        self.temp_f_lb.raise_()
        self.wind_vel_lb.raise_()
        self.wind_rumb_lb.raise_()
        self.temp_c_out_lb.raise_()
        self.temp_f_out_lb.raise_()
        self.wind_rumb_out_lb.raise_()
        self.city_inp_le.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.city_lb.setText(_translate("MainWindow", "Город: "))
        self.temp_c_lb.setText(_translate("MainWindow", "Температура °C: "))
        self.temp_f_lb.setText(_translate("MainWindow", "Температура ℉: "))
        self.wind_vel_lb.setText(_translate("MainWindow", "Скорость ветра, м/с: "))
        self.wind_rumb_lb.setText(_translate("MainWindow", "Направление ветра:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
