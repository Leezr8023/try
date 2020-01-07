from PyQt5 import QtGui,QtWidgets,QtCore
# from ui_new import Ui_MainWindow
#from slot import UI_slot
#
from test import ApplicationWindow
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow = ApplicationWindow()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())