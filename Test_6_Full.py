# Lib to numeric analysis and computer vision (opencv)
import numpy as np
import cv2
import face_recognition

import urllib

# Đọc 1 hình ảnh vào hệ thống
#img = cv2.imread('dwayne_johnson.jpg')
img = cv2.imread('dwayne_johnson.jpg')
cascPath = 'hasCascade.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
# Chuyển ảnh ở không gian màu RGB sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Xác định các khuôn mặt có trong hình
faces = faceCascade.detectMultiScale(
  gray,
  scaleFactor=1.1,
  minNeighbors=5,
  minSize=(30, 30),
  flags = cv2.CASCADE_SCALE_IMAGE
)
# In ra số lượng khuôn mặt có trong hình
#print ("Tìm thấy {0} khuôn mặt!".format(len(faces)) )

#####################################################################

# Thêm hình ảnh từng người vào mảng numpy để  lưu trữ
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")

dwayne_johnson_image = face_recognition.load_image_file("dwayne_johnson.jpg")

#
unknown_image = face_recognition.load_image_file("dwayne_johnson.jpg")

# Chuyển hình ảnh thành mã encodings

biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
dwayne_johnson_encoding = face_recognition.face_encodings(dwayne_johnson_image)[0]

# thêm một hình của người lạ mặt vào
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

known_faces = [
    biden_face_encoding,
    obama_face_encoding,
    dwayne_johnson_encoding
]

#results là mảng True/Flase cho biết liệu khuôn mặt lạ có trùng với khuôn mặt nào
# trong mảng đã biết không?
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

#print("{}".format(results[2]))
if(("{}".format(results[2])) == "True" ):
    print("Khuôn mặt này là khuôn mặt của Dwayne Johnson")
    print("Đã ghi nhận")
else:
    print("Đây không phải Dwayne Johnson")

#####
# Draw a rectangle around the faces in the original image
# Vẽ một khung xung quanh khuôn mặt
for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces found" ,img)
cv2.waitKey(0)