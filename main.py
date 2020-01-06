from PyQt5 import QtGui,QtWidgets,QtCore
# from ui_new import Ui_MainWindow
#from slot import UI_slot
from myplot import MainDialogImgBW
import sys



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow = MainDialogImgBW()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())