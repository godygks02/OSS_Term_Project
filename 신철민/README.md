# 202135790 신철민

---

# 프로젝트 개요

이 프로젝트는 OpenCV와 DeepFace를 이용하여 웹캠을 통해 얼굴을 인식하고, 인식된 얼굴의 표정을 분석하는 프로그램입니다. 프로그램은 실시간으로 표정을 감지하고, 주요 감정(예: 행복, 슬픔, 분노 등)을 출력합니다.

## 사용한 패키지와 버전

- **OpenCV**: 4.10.0.84
- **DeepFace**: 0.0.93

## 실행 방법

1. 필수 패키지 설치:
   ```bash
   pip install opencv-python deepface
   ```
2. `camera.py` 파일 실행:
   ```bash
   python camera.py
   ```
3. 프로그램이 실행되면 웹캠이 켜지고 얼굴 인식 및 감정 분석이 시작됩니다. 'q' 키를 눌러 프로그램을 종료할 수 있습니다.

## 이미지

![프로젝트 실행 화면](image/result_img1.png)
![프로젝트 실행 화면](image/result_img2.png)

## 참고 자료

- [얼굴 인식 및 표정 분석 참고 블로그](https://m.blog.naver.com/tmvmffpsej/223104743267)
- OpenCV 공식 문서: [https://docs.opencv.org/](https://docs.opencv.org/)
- DeepFace 공식 GitHub: [https://github.com/serengil/deepface](https://github.com/serengil/deepface)
