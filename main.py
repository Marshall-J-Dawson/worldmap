import json
import database
import collector



database.initialise_database()

def on_message(client, userdata, message):
    print("Topic; ", message.topic)
    data = json.loads(message.payload.decode())



    database.insert_location(
        data["lat"],
        data["lon"],
        database.convert_time(data["tst"]),
        data.get("batt")
    )
    print("location saved")



collector.start_mqtt(collector.on_connect, on_message)



