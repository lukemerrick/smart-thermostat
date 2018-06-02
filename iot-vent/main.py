import network
from umqtt.robust import MQTTClient
import machine
from servo import Servo
from time import sleep

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect("***REMOVED***", "***REMOVED***")

power = machine.Pin(5, machine.Pin.OUT)

srv = Servo(machine.Pin(2), freq=50, min_us=1500, max_us=2300, angle=80)
power.value(1)
srv.write_us(2300)
sleep(0.5)
power.value(0)
last_setting = 2300

while not sta_if.isconnected():
    machine.idle()
print("Connected to Wifi\n")


def sub_cb(topic, msg):
    global last_setting
    new_setting = int(msg)
    if last_setting == new_setting:
        return
    elif last_setting > new_setting:
        power.value(1)
        for i in range(last_setting - new_setting):
            srv.write_us(last_setting - i)
            i += 1
            sleep(0.002)
        last_setting = new_setting
        power.value(0)
        return
    elif last_setting < new_setting:
        power.value(1)
        for i in range(new_setting - last_setting):
            srv.write_us(last_setting + i)
            i += 1
            sleep(0.002)
        last_setting = new_setting
        power.value(0)
        return


client = MQTTClient("vent1_client", "192.168.1.182", user="vent1", password="3zbrEze", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="test/vent1")
client.publish(topic="test/status", msg="Vent 1 controller booted.")

while True:
    client.wait_msg()
