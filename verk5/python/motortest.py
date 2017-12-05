import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(05,GPIO.OUT)
GPIO.setup(03,GPIO.OUT)
pwm2 = GPIO.PWM(05,50)
pwm = GPIO.PWM(03, 50)
pwm.start(90)
pwm2.start(90)

def setangle(angle):
    duty = angle / 18 + 2
    GPIO.output(05, True)
    GPIO.output(03, True)
    pwm2.ChangeDutyCycle(duty)
    pwm.ChangeDutyCycle(duty)
    GPIO.output(03,False)
    pwm.ChangeDutyCycle(0)
    GPIO.output(05,False)
    pwm2.ChangeDutyCycle(0)

setangle(180)
sleep(0.5)
setangle(90)

