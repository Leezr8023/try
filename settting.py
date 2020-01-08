from ui_set import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
import numpy as np
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
        self.doubleSpinBox.setDecimals(6)
        self.doubleSpinBox_2.setDecimals(6)
        self.doubleSpinBox_3.setDecimals(6)
        self.doubleSpinBox_4.setDecimals(6)
        self.doubleSpinBox_5.setDecimals(6)
        self.doubleSpinBox_6.setDecimals(6)
        self.doubleSpinBox_7.setDecimals(6)

        self.doubleSpinBox_2.setValue(0)
        self.doubleSpinBox.setValue(0.1)
        self.doubleSpinBox_3.setValue(10)
        self.doubleSpinBox_4.setValue(10.1)
        self.doubleSpinBox_7.setValue(0.001)
        self.doubleSpinBox_8.setValue(1)
        self.spinBox_3.setValue(6)
        self.doubleSpinBox_5.setValue(0.001)
        self.doubleSpinBox_6.setValue(0.0015)
        self.spinBox.setRange(100,1000)
        self.spinBox.setSingleStep(100)
        self.spinBox.setValue(400)
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

        np.savetxt('setting.txt',[START_POSITION,FINISH_ONCE,SECEND_START,
    SECEND_FINISH,STEP,point_num,delay,y_range[0],y_range[1],single_num],
                   fmt='%f',delimiter='\n')

        self.close()



if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = subapp()
    app.show()
    qapp.exec_()