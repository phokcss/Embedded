import RPi.GPIO as GPIO
PIN_SERVO = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_SERVO, GPIO.OUT)
servo = GPIO.PWM(PIN_SERVO, 50)
servo.start(2)
try:
    while True:
        c = input("Select: c, r, l, q: ")
        if c == "c":
            servo.ChangeDutyCycle(2)
        elif c == "r":
            servo.ChangeDutyCycle(7)
        elif c == "l":
            servo.ChangeDutyCycle(12)
        elif c == "q":
            break
    servo.stop()
except KeyboardInterrupt:
    GPIO.cleanup()