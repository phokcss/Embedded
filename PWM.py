import RPi.GPIO as GPIO
from time import sleep
PIN_LED = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)
pi_pwm = GPIO.PWM(PIN_LED, 1000)    #PIN_LED울 PWM으로 사용
pi_pwm.start(0)
try:
    while True:
        for duty in range(0, 101, 1):
            pi_pwm.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)
        for duty in range(100, -1, -1):
            pi_pwm.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)
except KeyboardInterrupt:
    print("Cleaning up")
    GPIO.cleanup()