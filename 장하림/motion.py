import cv2
import numpy as np

# 웹캡 캡처 설정
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access the camera")
    exit()

# 이전 프레임을 저장하기 위한 변수
prev_frame = None

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break
    
    # 이미지를 흑백으로 변환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 이전 프레임과 현재 프레임의 차이 계산
    if prev_frame is None:
        prev_frame = gray_frame
        continue
    
    # 두 프레임 간의 차이 계산
    frame_diff = cv2.absdiff(prev_frame, gray_frame)
    
    # 차이를 이진화하여 보여주기
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
    
    # 결과 이미지 표시
    cv2.imshow("Motion Detection", thresh)
    
    # 이전 프레임을 현재 프레임으로 업데이트
    prev_frame = gray_frame
    
    # 'q' 키를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
