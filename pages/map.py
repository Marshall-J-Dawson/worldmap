from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout
)
from PySide6.QtWebEngineWidgets import QWebEngineView
import json
from database import get_locations
from PySide6.QtCore import QTimer


class MapPage(QWidget):

    def __init__(self, main_window):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.map = QWebEngineView()

        back_button = QPushButton("← Back")
        back_button.clicked.connect(main_window.go_home)

        layout.addWidget(self.map)
        layout.addWidget(back_button)

        self.setLayout(layout)


        # Check database for new locations every 500 ms
        self.last_location_count = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_map)
        self.timer.start(1000)

        # loads map and updates if there are changes
    def update_map(self):

        database_locations = get_locations()
        if len(database_locations) > self.last_location_count:

            self.last_location_count = len(database_locations)

            locations = []
            #potentially might be too laggy in future rewriting and loading the whole database
            for latitude, longitude, timestamp, battery in database_locations:

                locations.append({
                    "latitude": latitude,
                    "longitude": longitude,
                    "timestamp": timestamp,
                    "battery": battery
                })

            self.load_map(locations)



    def load_map(self, locations):

        # Convert Python data into JSON
        locations_json = json.dumps(locations)

        html = f"""
        <!DOCTYPE html>

        <html>
        <head>

            <meta charset="utf-8">

            <!-- Leaflet CSS -->
            <link
                rel="stylesheet"
                href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
            />

            <!-- Leaflet JavaScript -->
            <script
                src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js">
            </script>

            <style>

                html, body, #map {{
                    width: 100%;
                    height: 100%;
                    margin: 0;
                    padding: 0;
                }}

            </style>

        </head>

        <body>

            <div id="map"></div>

            <script>

                const locations = {locations_json};


                // Create the Leaflet map
                const map = L.map('map');


                // OpenStreetMap background
                L.tileLayer(
                    'https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',
                    {{
                        maxZoom: 19,
                        attribution: '&copy; OpenStreetMap contributors'
                    }}
                ).addTo(map);

                //L.tileLayer(
                //    'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}',
                //    {{
                //        maxZoom: 19,
                //        attribution: 'Tiles © Esri'
                //    }}
                // ).addTo(map);               


                // Convert locations into coordinates
                const coordinates = locations.map(location => [
                    location.latitude,
                    location.longitude
                ]);


                // Add a marker for every location
                locations.forEach((location) => {{

                    const marker = L.marker([
                        location.latitude,
                        location.longitude
                    ]).addTo(map);

                    marker.bindPopup(
                        "<b>Location</b><br>" +
                        location.timestamp
                    );

                }});


                // Only continue if we have locations
                if (locations.length > 0) {{

                    // Get the most recent location
                    const latest = locations[locations.length - 1];


                    // Create highlighted marker
                    const latestMarker = L.circleMarker(
                        [
                            latest.latitude,
                            latest.longitude
                        ],
                        {{
                            radius: 10,
                            color: 'red',
                            fillColor: 'red',
                            fillOpacity: 0.9
                        }}
                    ).addTo(map);


                    // Popup for most recent location
                    latestMarker.bindPopup(
                        "<b>Most Recent Location</b><br>" +
                        latest.timestamp
                    );


                    // Zoom map to show all locations
                    map.fitBounds(
                        coordinates,
                        {{
                            padding: [30, 30]
                        }}
                    );

                }}

            </script>

        </body>
        </html>
        """

        self.map.setHtml(html)