from PyQt5 import QtGui
from login import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("Student Attendance Portal")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        self.text = QLabel("Welcome to the Portal.",self)
        self.text.move(135,50)
        self.enterButton = QPushButton("Entry Management",self)
        self.enterButton.move(80,80)
        self.enterButton.clicked.connect(self.enter)
        self.exitButton = QPushButton("Exit Management",self)
        self.exitButton.move(200,80)
        self.exitButton.clicked.connect(self.exit)

        # creating a label widget
        self.label_2 = QLabel(self)

        # moving position
        self.label_2.move(90, 150)

        # setting up the border and adding image to background
        self.label_2.setStyleSheet("background-image : url(logo.png);border: 2px solid blue")

        # setting label text
        #self.label_2.setText("with background image")
        self.label_2.resize(220, 140)

        self.show()

    def enter(self):
        mixer.init()
        mixer.music.load('assets/text_to_speech/entry.mp3')
        mixer.music.play()
        #time.sleep(1)
        os.system('python login.py')
    def exit(self):
        mixer.init()
        mixer.music.load('assets/text_to_speech/exit.mp3')
        mixer.music.play()
        #time.sleep(1)
        os.system('python login2.py')


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())



if __name__ == '__main__':
    main()
