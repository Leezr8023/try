from ui_set import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
import sys
from const import START_POSITION,FINISH_ONCE,SECEND_START,\
    SECEND_FINISH,STEP,point_num,delay,y_range,single_num

global START_POSITION
global FINISH_ONCE
global SECEND_START
global SECEND_FINISH
global STEP
global point_num
global delay
global y_range
global single_num
# global
# global



class subapp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.update)
    def update(self):
        START_POSITION = self.doubleSpinBox_2.value()
        FINISH_ONCE = self.doubleSpinBox.value()
        SECEND_START = self.doubleSpinBox_3.value()
        SECEND_FINISH = self.doubleSpinBox_4.value()
        STEP = self.doubleSpinBox_7.value()
        point_num = self.spinBox.value()
        delay = self.doubleSpinBox_8.value()
        y_range[0] = self.doubleSpinBox_5.value()
        y_range[1] = self.doubleSpinBox_6.value()
        single_num = self.spinBox_3.value()



if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = subapp()
    app.show()
    qapp.exec_()