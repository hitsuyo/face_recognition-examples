import cv2
camera = cv2.VideoCapture(0)
while (True):
#while (camera.isOpened()):
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(100) & 0xFF == ord('s'):
        cv2.imwrite('biden.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()