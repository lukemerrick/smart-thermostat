### Configuring the ESP8266

1) Flash microPython firmware using esptool
2) Install ampy (adafruit tool)
3) Edit your copy of the `setup.py` and `boot.py` (in the boot/custom directory), replacing  `<ssid>` and `<psk>`
with your WiFi network name and password, respectively.
4) Run `ampy -p <serial port here> rm boot.py`, `ampy -p <serial port here> put <path to this iot-vent folder>
/boot/custom/boot.py`, `ampy -p <serial port here> put <path to this iot-vent folder> main.py`, and `ampy -p
<serial port here> put <path to this iot-vent folder> setup.py`
5) Reset the ESP8266 and open a serial connection with a baud rate of `115200` (you can use screen, Tera Term, etc.)
6) Make sure you have a microPython REPL prompt, you'll see the characters `>>>` in front of your cursor. Press enter
if it's showing to check the connection.
7) Run `import webrepl_setup` and follow the instructions to enable the web REPL service
8) Run `import setup` and wait while the network settings are configured. 
9) Reset the ESP826, you should be able to access the board from
[http://micropython.org/webrepl/](http://micropython.org/webrepl/)
