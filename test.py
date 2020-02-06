import sys
import time
from ui_new import Ui_MainWindow
from Algorithm import qtoutput

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
from PyQt5.QtGui import QFont
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from mythread import myThread
from matplotlib.figure import Figure
from const import exitFlag,data

global exitFlag
class ApplicationWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.verticalLayout.addWidget(dynamic_canvas)
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(dynamic_canvas, self))
        # self.textEdit.setFont(Qfont(14))#("Consolas", 14)
        self.textEdit.setFont(QFont("Consolas", 14))

        self.pushButton.clicked.connect(self.MeasureThread)
        self.pushButton_2.clicked.connect(self.output)
        self.pushButton_3.clicked.connect(self.opensetting)

        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self._timer = dynamic_canvas.new_timer(
            100, [(self._update_canvas, (), {})])

    def output(self):
        str = "{:.2f}"
        str = str.format(qtoutput())
        self.textEdit.setText(str)
        # self.textEdit.setText(str(qtoutput()))
    def opensetting(self):
        print("槽函数触发成功")
        pass

    def MeasureThread(self):
        print("123")
        self.pushButton.setEnabled(False)
        thread1 = myThread(1, "Thread-1", 1)
        # thread2 = myThread(2, "Thread-2", 1)
        self._timer.start()
        thread1.start()
        print(exitFlag[0])

    def _update_canvas(self):
        global exitFlag
        if exitFlag[0]==1:
            self._timer.stop()
            self.pushButton.setEnabled(True)
        self._dynamic_ax.clear()
        global data
        self._dynamic_ax.plot(range(1600), data[...,0])#data[...,1]
        self._dynamic_ax.set_xlim(0, 1600)
        self._dynamic_ax.set_ylim(0.0008, 0.00145)
        self._dynamic_ax.figure.canvas.draw()


# if __name__ == "__main__":
#     qapp = QtWidgets.QApplication(sys.argv)
#     app = ApplicationWindow()
#     app.show()
#     qapp.exec_()
