import sys
import time
from ui_new import Ui_MainWindow
import numpy as np

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from mythread import myThread
from matplotlib.figure import Figure
import random
from const import exitFlag,data


class ApplicationWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self._main = QtWidgets.QWidget()
        # self.setCentralWidget(self._main)
        # layout = QtWidgets.QVBoxLayout(self._main)
        # layout = QtWidgets.QVBoxLayout(self.centralwidget)
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.verticalLayout.addWidget(dynamic_canvas)
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(dynamic_canvas, self))

        self.pushButton.clicked.connect(self.MeasureThread)


        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self._timer = dynamic_canvas.new_timer(
            100, [(self._update_canvas, (), {})])
        # self._timer.start()
        print("uidone")

    def MeasureThread(self):
        print("123")
        self.pushButton.setEnabled(False)
        thread1 = myThread(1, "Thread-1", 1)
        thread2 = myThread(2, "Thread-2", 1)
        self._timer.start()
        # 开启新线程

        thread1.start()
        # thread1.join()
        # thread2.start()
    def _update_canvas(self):
        if exitFlag:  #exitFlag # 画200个点就停止，根据实际情况确定终止条件
            self._timer.stop()

        self._dynamic_ax.clear()
        # t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.

        # data[self.n] = random.randint(0,self.n)
        self._dynamic_ax.plot(data[...,0], data[...,1])
        self._dynamic_ax.set_xlim(0, 400)
        self._dynamic_ax.set_ylim(0, 400)
        self._dynamic_ax.figure.canvas.draw()


if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec_()
