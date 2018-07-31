import sys
from time import sleep

# 74000 is fully closed, 110000 is fully open

current_setting = 74000  # This will eventually come from a config file of some sort
step_delay = 0.001

new_setting = int(sys.argv[1])

try:
    import pigpio
except RuntimeError:
    print("Error importing pigpio!  This is probably because you need superuser privileges.  You can achieve this by"
          "using 'sudo' to run your script")

pi = pigpio.pi()

pi.hardware_PWM(18, 50, current_setting)
sleep(.5)

if new_setting > current_setting:
    diff = int(((new_setting - current_setting) / 100))
    print("New > current, diff is : {}".format(diff))
    for i in range(diff):
        pi.hardware_PWM(18, 50, current_setting + i * 100)
        sleep(step_delay)
elif new_setting < current_setting:
    diff = int(((current_setting - new_setting) / 100))
    print("Current > new, diff is : {}".format(diff))
    for i in range(diff):
        pi.hardware_PWM(18, 50, current_setting - i * 100)
        sleep(step_delay)

current_setting = new_setting  # This will eventually be written back to a config file


sleep(0.2)

# Stop the pwm here
pi.set_mode(18, pigpio.OUTPUT)
pi.write(18, 0)
