from PyQt5.QtCore import QObject, pyqtSignal


class RubSignal(QObject):
    mySignal = pyqtSignal(int)