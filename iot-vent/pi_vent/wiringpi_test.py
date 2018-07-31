import wiringpi
import sys
from time import sleep

# 150 is fully closed, 210 is fully open

current_setting = 150  # This will eventually come from a config file of some sort
step_delay = 0.02

new_setting = int(sys.argv[1])

wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

if new_setting > current_setting:
    for i in range((new_setting - current_setting) + 1):
        wiringpi.pwmWrite(18, current_setting + 1)
        sleep(step_delay)

elif new_setting < current_setting:
    for i in range((current_setting - new_setting) + 1):
        wiringpi.pwmWrite(18, current_setting - 1)
        sleep(step_delay)

current_setting = new_setting  # This will eventually be written back to a config file


sleep(0.5)
wiringpi.pwmWrite(18, 0)

# wiringpi.pwmWrite(18, new_setting)
