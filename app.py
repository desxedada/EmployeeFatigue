import sys
import os

from PySide6.QtCore import Slot, Signal, QObject
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# Main Window Class
class LoginWindow(QObject):
    def __init__(self):
        QObject.__init__(self)

    # Static Info
    staticUser = "wanderson"
    staticPass = "123456"

    # Signals To Send Data
    signalUser = Signal(str)
    signalPass = Signal(str)
    signalLogin = Signal(bool)

    # Function To Check Login
    @Slot(str, str)
    def checkLogin(self, getUser, getPass):
        if(self.staticUser.lower() == getUser.lower() and self.staticPass == getPass):
            # Send User And Pass
            self.signalUser.emit("Username: " + getUser)
            self.signalPass.emit("Password: " + getPass)

            # Send Login Signal
            self.signalLogin.emit(True)
            print("Login passed!")
        else:
            self.signalLogin.emit(False)
            print("Login error!")


# INSTANCE CLASS
if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = LoginWindow()
    engine.rootContext().setContextProperty("backend", main)

    # Load QML File
    engine.load(os.path.join(os.path.dirname(__file__), "qml/loginDialog.qml"))

    # Check Exit App
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())