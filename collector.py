#take mqqt data parse valuable to db
import paho.mqtt.client as mqtt
import json
import ssl

with open("config.json") as f:
    config = json.load(f)


def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print("Connected to broker.")
        client.subscribe("owntracks/#")
    else:
        print(f"Connection failed: {reason_code}")

def start_mqtt(on_connect, on_message):
    client = mqtt.Client(client_id="marshalltracks_collector")

    #mqtt user and pass
    client.username_pw_set(
        config["username"],
        config["password"]
    )

    client.on_message = on_message
    client.on_connect = on_connect

    client.tls_set(
    ca_certs="/etc/ssl/certs/ca-certificates.crt",
    tls_version=ssl.PROTOCOL_TLS
    )



    client.connect(
    config["broker"],
    8883
    )
    
   

    client.loop_forever()









