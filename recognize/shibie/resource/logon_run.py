import sys
import logon
import getfaces
import recognized
from PyQt5 import QtWidgets
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
class Log(QtWidgets.QMainWindow,logon.Ui_MainWindow):

    show_log_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def showregister(self):
        self.show_log_signal.emit()
        #getfaces.intlx()
        #already.undx()
    def loadplane(self):
        recognized.rune()

    def showshibie(self):
        getfaces.intlx()

if __name__=='__main__':
    app =QApplication(sys.argv)
    mainWindow = Log()
    ui = logon.Ui_MainWindow()

    mainWindow.show()
    sys.exit(app.exec_())