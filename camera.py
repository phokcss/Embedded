import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (640, 480)
time.sleep(3)
print("Now saving a picture....!!!")
camera.capture('snapshot_test.jpg')