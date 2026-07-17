#take mqqt data parse valuable to db
import paho.mqtt.client as mqtt
import json
import ssl

with open("config.json") as f:
    config = json.load(f)

def on_message(client, userdata, message):
    print("Topic; ", message.topic)
    data = json.loads(message.payload.decode())
    print(data)


client = mqtt.Client(client_id="marshalltracks_collector")

#mqtt user and pass
client.username_pw_set(
    config["username"],
    config["password"]
)

client.tls_set(
    ca_certs="/etc/ssl/certs/ca-certificates.crt",
    tls_version=ssl.PROTOCOL_TLS
)

client.on_message = on_message

client.connect(
    config["broker"],
    8883
)

client.subscribe("owntracks/#")

client.loop_forever()