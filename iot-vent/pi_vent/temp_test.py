import Adafruit_DHT
import gc
from time import sleep

gc.enable()  # This should happen

sensor = Adafruit_DHT.DHT22

pin = 17

delay = 10

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    deg_f = 1.8 * temperature + 32
    if humidity is not None and temperature is not None:
        print('Temp={0:0.2f} F  Humidity={1:0.1f}%'.format(deg_f, humidity))
    else:
        print('Failed to get reading. Try again!')

    sleep(delay)
