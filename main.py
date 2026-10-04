from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton
)
import sys

import cl1
import cl2


class Some(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лаба 1 —  Основы проектирования графического интерфейса компьютерных систем")
        self.resize(500, 450)

        ## это чтобы были надпись сверху, куда будут показываться картинки
        self.label = QLabel("Выберите изображение")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumHeight(300)

        ## три фотки, три кнопки
        self.btn_interf = QPushButton("Интерферограмма")
        self.btn_dactyl = QPushButton("Дактилограмма")
        self.btn_crystal = QPushButton("Кристаллограмма")

        ## сигналы кнопок
        self.btn_interf.clicked.connect(self.show_interf)
        self.btn_dactyl.clicked.connect(self.show_dactyl)
        self.btn_crystal.clicked.connect(self.show_crystal)

        ## раскладка кнопок в ряд
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.btn_interf)
        buttons_layout.addWidget(self.btn_dactyl)
        buttons_layout.addWidget(self.btn_crystal)

        ## это общая раскладка: надпись сверху, кнопки снизу
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addLayout(buttons_layout)

        central = QWidget()
        central.setLayout(main_layout)
        self.setCentralWidget(central)

    ## вспомогательный метод, чтобы не дублировать код
    def show_image(self, path, title):
        pixmap = QPixmap(path)
        if pixmap.isNull():
            self.label.setText(f"Файл {path} не найден")
            self.label.setPixmap(QPixmap())  ## очистить картинку
            return
        self.label.setPixmap(pixmap.scaled(
            400, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))
        self.setWindowTitle(f"Лаба 1 — {title}")

    def show_interf(self):
        self.show_image("nterforogramma.PNG", "Интерферограмма")

    def show_dactyl(self):
        self.show_image("dactilogramma.png", "Дактилограмма")

    def show_crystal(self):
        self.show_image("kristalogramma.PNG", "Кристаллограмма")


class Data:
    def __init__(self):
        self.myData = []

    def getData(self):
        return self.myData


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Some()
    window.show()
    app.exec()