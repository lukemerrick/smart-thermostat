import wiringpi
import sys
from time import sleep

# 150 is fully closed, 210 is fully open

current_setting = 150  # This will eventually come from a config file of some sort
step_delay = 0.02

new_setting = int(sys.argv[1])

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(17, wiringpi.GPIO.OUTPUT)
wiringpi.softPwmCreate(17, 0, 200)
wiringpi.digitalWrite(17, 0)
sleep(.5)
wiringpi.softPwmWrite(17, 180)
# sleep(.5)
# wiringpi.softPwmWrite(17, 150)

# if new_setting > current_setting:
#     for i in range((new_setting - current_setting) + 1):
#         wiringpi.softPwmWrite(17, (current_setting + 1) * 10)
#         sleep(step_delay)
#
# elif new_setting < current_setting:
#     for i in range((current_setting - new_setting) + 1):
#         wiringpi.softPwmWrite(17, (current_setting - 1) * 10)
#         sleep(step_delay)
#
# current_setting = new_setting  # This will eventually be written back to a config file


sleep(2)
wiringpi.softPwmStop(17)
