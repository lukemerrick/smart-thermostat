import paho.mqtt.client as mqtt
import ssl

client = mqtt.Client(client_id="WESLEY-DT")

client.tls_set(ca_certs="ca.crt", certfile="wesley-dt.crt", keyfile="wesley-dt.key")

# client.username_pw_set("vent1", "3zbrEze")

client.connect("thermostat", port=8883)

client.publish("test/vent1", payload="vent1 test complete")

client.disconnect()
