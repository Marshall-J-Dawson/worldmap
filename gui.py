import sys

from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QTableWidgetItem,
    QApplication
)

from PySide6.QtCore import QTimer

from pages.home import HomePage
from pages.map import MapPage
from pages.data import DataPage
from pages.stats import StatsPage
from pages.prompt import PromptPage

from database import get_locations, clear_database, initialise_database


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Location Database")
        self.resize(900, 500)

        # Create stacked pages
        self.pages = QStackedWidget()

        # Create pages
        self.home_page = HomePage(self)
        self.map_page = MapPage(self)
        self.data_page = DataPage(self)
        self.stats_page = StatsPage(self)
        self.prompt_page = PromptPage(self)

        # Add pages to stacked widget
        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.map_page)
        self.pages.addWidget(self.data_page)
        self.pages.addWidget(self.stats_page)
        self.pages.addWidget(self.prompt_page)

        # Show stacked widget
        self.setCentralWidget(self.pages)

        # Start on home page
        self.go_home()

        # Create timer
        self.timer = QTimer()

        # Run refresh_database every 1000ms
        self.timer.timeout.connect(self.refresh_database)

        # Start timer
        self.timer.start(1000)

        # Load immediately
        self.refresh_database()


    def go_home(self):

        self.pages.setCurrentWidget(self.home_page)


    def open_map(self):

        self.pages.setCurrentWidget(self.map_page)

    def open_prompt(self):

        self.pages.setCurrentWidget(self.prompt_page)


    def open_data(self):

        self.pages.setCurrentWidget(self.data_page)


    def open_stats(self):

        self.pages.setCurrentWidget(self.stats_page)

    def delete_database(self):
        clear_database()
        initialise_database()



    def refresh_database(self):

        rows = get_locations()

        # Update table
        self.data_page.table.setRowCount(len(rows))
        self.data_page.table.setColumnCount(4)

        self.data_page.table.setHorizontalHeaderLabels([
            "Latitude",
            "Longitude",
            "Timestamp",
            "Battery"
        ])

        for row_number, row in enumerate(rows):

            for column_number, value in enumerate(row):

                self.data_page.table.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(str(value))
                )

def run_gui(): 
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show() 
    app.exec() 

if __name__ == "__main__": 
    run_gui()