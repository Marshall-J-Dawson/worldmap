from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)
from PySide6.QtCore import Qt


class MapPage(QWidget):

    def __init__(self, main_window):
        super().__init__()

        layout = QVBoxLayout()

        message = "Map will go here"
        label = QLabel(message)

        back_button = QPushButton("← Back")
        back_button.clicked.connect(main_window.go_home)

        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(back_button)

        self.setLayout(layout)