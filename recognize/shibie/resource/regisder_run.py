import sys
import csv
import already
import regisder
from PyQt5 import QtWidgets
from PyQt5.Qt import *
from PyQt5.QtWidgets import *

path = "data/load/name.csv"
class Regisder(QtWidgets.QMainWindow,regisder.Ui_MainWindow):
    exit_signal = pyqtSignal()
    register_signal = pyqtSignal(str, str,str,str,str)

    def __init__(self, parent=None, *args, **kwargs):
        super(Regisder,self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
    '''def tuichu(self):
        #self.exit_signal.emit()
        #QCloseEvent.accept()'''
    def reset(self):
        print("重置")
        self.xm.clear()
        self.xb.clear()
        self.sfzh.clear()
        self.rzny_1.clear()
        self.lxdh_1.clear()

    def queren(self):
        print("确认")
        #already.undx()
        xm_txt = self.xm.text()
        print(xm_txt)
        xb_txt = self.xb.text()
        print(xb_txt)
        sfzh_txt = self.sfzh.text()
        print(sfzh_txt)
        rzny_txt = self.rzny_1.text()
        print(rzny_txt)
        lxdh_txt = self.lxdh_1.text()
        print(lxdh_txt)
        with open(path, 'a+', newline="") as f:
            csv_write = csv.writer(f)
            csv_head = [xm_txt, xb_txt, sfzh_txt, rzny_txt, lxdh_txt]
            csv_write.writerow(csv_head)
        self.register_signal.emit(xm_txt, xb_txt,sfzh_txt,rzny_txt,lxdh_txt)

    def enableregisder(self):
        print("判定")
        #already.undx()
        xm_txt=self.xm.text()
        xb_txt=self.xb.text()
        sfzh_txt=self.sfzh.text()
        rzny_txt=self.rzny_1.text()
        lxdh_txt=self.lxdh_1.text()
        if len(xm_txt) > 0 and len(xb_txt) > 0 and len(sfzh_txt) > 0 and len(rzny_txt) > 0 and len(lxdh_txt) > 0:
            self.qr.setEnabled(True)
        else:
            self.qr.setEnabled(False)

    def shanku(self):
        already.removeku()


if __name__=='__main__':
    app =QApplication(sys.argv)
    mainWindow = Regisder()
    ui = regisder.Ui_MainWindow()
    #mainWindow.exit_signal.connect(lambda: print("退出"))
    #mainWindow.register_signal.connect(lambda a, b,c,d,e: print(a, b,c,d,e))
    mainWindow.show()
    t=app.exec()
    print(t)
    #sys.exit(t)
