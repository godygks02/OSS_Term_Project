import cv2

# Open the device at the ID 0
cap = cv2.VideoCapture(0)
# Check whether user selected camera is opened successfully.
if not (cap.isOpened()):
    print("Could not open video device")

while(True):
# Capture frame-by-frame
    ret, frame = cap.read()

    cv2.imshow('bin',frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
