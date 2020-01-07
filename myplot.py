#-*-coding:utf-8-*-
import random
from ui_new import Ui_MainWindow
import time
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton,QGridLayout
from mythread import myThread
from const import exitFlag,SIGNAL,data
#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)

class MainDialogImgBW(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0,0)

        self.pushButton.clicked.connect(self.MeasureThread)

        self.F = MyFigure(width=3, height=2, dpi=100)
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F,0,1)
        t = np.arange(0.0, 5.0, 0.01)
        s = np.cos(2 * np.pi * t)
        self.F.axes.plot(t, s)
        self.F.axes.cla()
        #self.F.axes.plot(random.randint(0,9),random.randint(0,9), 'o')

        # self.F.draw()

    def MeasureThread(self):
        self.pushButton.setEnabled(False)
        thread1 = myThread(1, "Thread-1", 1)
        thread2 = myThread(2, "Thread-2", 1)
        # 开启新线程

        # thread1.start()
        # thread1.join()
        # thread2.start()
        # while True:
        #     time.sleep(1)
        #     if exitFlag:
        #         break
        #     else:
        #         if SIGNAL:
        #             # QApplication.processEvents()
        #             self.F.axes.cla()
        #             self.F.axes.plot(data[..., 0], data[..., 1], 'o')
        #             print(data)
        #             #self.pushButton.setEnabled(True)
        #             SIGNAL = 0

        print("退出主线程")