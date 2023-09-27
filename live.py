from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
# 카메라 초기화
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# 워밍업을 위한 딜레이
time.sleep(0.1)
# 연속적인 카메라 캡처 시작
for frame in camera.capture_continuous(rawCapture,
                                       format="bgr",
                                       use_video_port=True ):
    image = frame.array
    # 화면에 표시
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    # 다음 프레임을 준비하기 위해 스트림 정리
    rawCapture.truncate(0)
    # 키보드 `q` 를 누른 경우 루프를 탈출
    if key == ord("q"):
        break
