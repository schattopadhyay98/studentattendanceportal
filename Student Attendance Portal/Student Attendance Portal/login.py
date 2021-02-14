import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from mainwindow import *


class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Student Attendance Portal Admin Login')
		self.resize(500, 120)

		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('username')
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('password')
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)

		button_login = QPushButton('Login')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		self.setLayout(layout)

	def check_password(self):
		msg = QMessageBox()

		if self.lineEdit_username.text() == 'admin' and self.lineEdit_password.text() == 'admin':
			msg.setText('Success')
			msg.exec_()
			print("Correct Password Entered")
			mixer.init()
			mixer.music.load('assets/text_to_speech/correctpassword.mp3')
			mixer.music.play()
			time.sleep(1)
			app.quit()
			os.system('python mainwindow.py')

		else:
			msg.setText('Incorrect Password')
			print("Incorrect Password Entered")
			mixer.init()
			mixer.music.load('assets/text_to_speech/wrongpassword.mp3')
			mixer.music.play()
			time.sleep(5)
			app.quit()




if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = LoginForm()
	form.show()

	sys.exit(app.exec_())