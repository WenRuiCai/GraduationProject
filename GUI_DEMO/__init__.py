from PyQt5.QtWidgets import QPushButton, QWidget,QLineEdit, QApplication
import sys, time


def main():
    application = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Sample')
    w.show()
    #time.sleep(3)
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()