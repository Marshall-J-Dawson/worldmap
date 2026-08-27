from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)
from PySide6.QtCore import Qt


class PromptPage(QWidget):

    def __init__(self, main_window):
        super().__init__()

        layout = QVBoxLayout()

        message = "are you sure you want to delete data?"
        label = QLabel(message)

        delete_data = QPushButton("Yes")
        delete_data.clicked.connect(main_window.delete_database)
        delete_data.clicked.connect(main_window.open_data)

        back_button = QPushButton("No")
        back_button.clicked.connect(main_window.open_data)

        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(delete_data)
        layout.addWidget(back_button)

        self.setLayout(layout)