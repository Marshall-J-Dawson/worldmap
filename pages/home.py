from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout
)


class HomePage(QWidget):

    def __init__(self, main_window):
        super().__init__()

        layout = QVBoxLayout()

        #home button options
        map_button = QPushButton("Open Map")
        table_button = QPushButton("Data")
        stats_button = QPushButton("Stats")

        #action triggers
        map_button.clicked.connect(main_window.open_map)
        table_button.clicked.connect(main_window.open_data)
        stats_button.clicked.connect(main_window.open_stats)


        layout.addWidget(map_button)
        layout.addWidget(table_button)
        layout.addWidget(stats_button)
        self.setLayout(layout)