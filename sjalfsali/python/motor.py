def start():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(03,GPIO.OUT)
	pwm = GPIO.PWM(03,50)
	pwm.start(0)


def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)

def stop():
	pwm.stop()
	GPIO.cleanup()