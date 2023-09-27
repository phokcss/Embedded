from picamera.array import PiRGBArray
from picamera import PiCamera
import time
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
# 정면 얼굴 검출을 위한 Haarcascade 특징이 정의된 xml 파일
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# 연속적인 카메라 캡처 시작
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    image = frame.array # NumPy 배열 형태로 프레임 정보 획득
    cv2.imshow("Frame", image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 컬러 변환
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) # 얼굴 검출

    for (x, y, w, h) in faces: # 검출된 얼굴을 사각형으로 표시
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Face Image", image) # 화면에 표시

    key = cv2.waitKey(1) & 0xFF # 사용자 입력 확인
    rawCapture.truncate(0) # 다음 프레임을 준비하기 위해 스트림 정리

    if key == ord("q"): # 키보드 `q` 를 누른 경우 루프를 탈출
        break