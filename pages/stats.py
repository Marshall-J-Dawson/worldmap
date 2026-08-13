from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt


class StatsPage(QWidget):

    def __init__(self, main_window):
        super().__init__()

        layout = QVBoxLayout()

        back_button = QPushButton("← Back")
        back_button.clicked.connect(main_window.go_home)

        message = "This is where I might display stats, like total data points etc, fully undecided"
        
        self.label = QLabel(message)

        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(back_button)

        self.setLayout(layout)