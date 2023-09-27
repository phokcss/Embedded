import RPi.GPIO as GPIO
from time import sleep
PIN_LED = 4
PIN_INTERRUPT = 17
def KeyHandler(n):
    print("Key is pressed [%d]" % n)
    if GPIO.input(PIN_LED):
        GPIO.output(PIN_LED, False)
    else:
        GPIO.output(PIN_LED, True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_INTERRUPT, GPIO.IN)
GPIO.add_event_detect(PIN_INTERRUPT,GPIO.FALLING,callback=KeyHandler)
sec = 0
try:
    while True:
        print("sec : %d" %sec)
        sec = sec + 1
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()