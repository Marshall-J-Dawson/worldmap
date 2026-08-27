from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QHeaderView
)



class DataPage(QWidget):

    def __init__(self, main_window):
        super().__init__()
        layout = QVBoxLayout()

        delete_data = QPushButton("Delete Data")
        delete_data.clicked.connect(main_window.open_prompt)
        

        back_button = QPushButton("← Back")
        back_button.clicked.connect(main_window.go_home)

        self.table = QTableWidget()

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        

        layout.addWidget(delete_data)
        layout.addWidget(back_button)
        layout.addWidget(self.table)

        self.setLayout(layout)