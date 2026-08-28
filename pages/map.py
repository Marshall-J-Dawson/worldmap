from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout
)
from PySide6.QtWebEngineWidgets import QWebEngineView
import json


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

        # Temporary test locations
        locations = [
            {
                "latitude": 36.2048,
                "longitude": 138.2529,
                "timestamp": "2026-08-27 10:00"
            },
            {
                "latitude": 40.7128,
                "longitude": -74.0060,
                "timestamp": "2026-08-27 10:15"
            },
            {
                "latitude": -37.8136,
                "longitude": 144.9631,
                "timestamp": "2026-08-27 10:30"
            },
            {
                "latitude": 51.5074,
                "longitude": 0.1278,
                "timestamp": "2026-08-27 10:45"
            }
        ]

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