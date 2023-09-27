import RPi.GPIO as GPIO
from time import sleep
global a
a=0
def KeyHandler(n):
    print("Key is pressed [%d]" % n)
    global a
    if (a==0):
        servo.ChangeDutyCycle(2)
        a=1
    else:
        servo.ChangeDutyCycle(12)
        a=0
PIN_INTERRUPT = 4
PIN_SERVO = 12
sec=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_INTERRUPT, GPIO.IN)
GPIO.setup(PIN_SERVO, GPIO.OUT)
servo = GPIO.PWM(PIN_SERVO, 50)
servo.start(2)
d=[4,12]
GPIO.add_event_detect(PIN_INTERRUPT,GPIO.FALLING,callback=KeyHandler)
try:
    while True:
        pass

except KeyboardInterrupt:
    GPIO.cleanup()