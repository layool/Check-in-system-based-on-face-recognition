from regisder_run import Regisder
from logon_run import Log
from PyQt5.Qt import *
from PyQt5.QtWidgets import *


if __name__=='__main__':
    import sys
    app =QApplication(sys.argv)
    login_pane = Log()

    def showregister():
        print("展示注册")
        register_run = Regisder(login_pane)
        register_run.move(0, login_pane.height())
        register_run.show()
        animation = QPropertyAnimation(register_run)
        animation.setTargetObject(register_run)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(300, login_pane.height()))
        animation.setEndValue(QPoint(300, 65))
        animation.setDuration(500)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
        animation.setEasingCurve(QEasingCurve.OutBounce)

    login_pane.show_log_signal.connect(showregister)
    login_pane.show()
    sys.exit(app.exec_())