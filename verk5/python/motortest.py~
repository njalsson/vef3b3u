import RPi.GPIO as GPIO
from time import sleep
import wiringpi
# GPIO.setmode(GPIO.BOARD)

# GPIO.setup(03,GPIO.OUT)
# pwm = GPIO.PWM(03, 50)
# pwm.start(90)


# def setangle(angle):
#     duty = angle / 18 + 2
#     GPIO.output(03, True)
#     pwm.ChangeDutyCycle(duty)
#     sleep(1)
#     GPIO.output(03,False)
#     pwm.ChangeDutyCycle(0)


# setangle(180)
# sleep(0.5)
# setangle(90)

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()
# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
delay_period = 0.01


while True:
	for pulse in range(50, 250, 1):
		wiringpi.pwmWrite(03, pulse)
		wiringpi.pwmWrite(05, pulse)
		sleep(delay_period)
	for pulse in range(250, 50, -1):
		wiringpi.pwmWrite(03, pulse)
		wiringpi.pwmWrite(05, pulse)
		sleep(delay_period)