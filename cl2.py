from PyQt5.QtCore import QObject, pyqtSignal


class DolarSignal(QObject):
    mySignal = pyqtSignal(int)