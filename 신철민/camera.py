import cv2
from deepface import DeepFace

# Haarcascade를 이용한 얼굴 검출 모델 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 웹캠 열기가 실패한 경우 확인
if not cap.isOpened():
    print("Could not open video device")
    exit()
count = 0
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture frame")
        break

    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 얼굴 검출
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if count % 5 == 0:
        for (x, y, w, h) in faces:
            # 얼굴 영역에 사각형 표시
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # 얼굴 영역을 ROI로 설정
            roi = frame[y:y+h, x:x+w]
            
            # ROI 크기 조정
            resized_roi = cv2.resize(roi, (100, 100))
            
            
            # 얼굴 감지 및 감정 분석
            try:
                # 감정 분석 수행
                result = DeepFace.analyze(roi, actions=['emotion'], enforce_detection=False)
                
            # 결과 출력 (디버깅을 위해)
                print(result)

                # 감정이 결과에 포함되어 있는지 확인
                if result and 'dominant_emotion' in result[0]:
                    dominant_emotion = result[0]['dominant_emotion']
                    # 감정 결과 표시
                    cv2.putText(frame, f"Emotion: {dominant_emotion}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "Emotion not detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            except Exception as e:
                print("Error in emotion detection:", e)
            
        
        
        # 전체 프레임 출력
        cv2.imshow('Face Detection', frame)
        
        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    count += 1

# 자원 해제
cap.release()
cv2.destroyAllWindows()
