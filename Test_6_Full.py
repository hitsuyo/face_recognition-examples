# Lib to numeric analysis and computer vision (opencv)
import numpy as np
import cv2
import face_recognition

import urllib


#####################################################################

# Thêm hình ảnh từng người vào mảng numpy để  lưu trữ
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")
shinzo_abe_image = face_recognition.load_image_file("shinzo_abe.jpg")
dwayne_johnson_image = face_recognition.load_image_file("dwayne_johnson.jpg")
mark_zuckerberg_image = face_recognition.load_image_file("mark_zuckerberg.jpg")

## Chọn hình ảnh muốn nhận dạng
unknown_image = face_recognition.load_image_file("dwayne_johnson.jpg")
#unknown_image = face_recognition.load_image_file("biden.jpg")
#unknown_image = face_recognition.load_image_file("obama.jpg")
#unknown_image = face_recognition.load_image_file("shinzo_abe.jpg")
#unknown_image = face_recognition.load_image_file("mark_zuckerberg.jpg")

# Chuyển hình ảnh thành mã encodings
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
dwayne_johnson_encoding = face_recognition.face_encodings(dwayne_johnson_image)[0]
shinzo_abe_encoding = face_recognition.face_encodings(shinzo_abe_image)[0]

mark_zuckerberg_encoding = face_recognition.face_encodings(mark_zuckerberg_image)[0]

# thêm một hình của người lạ mặt vào
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

known_faces = [
    biden_face_encoding,    #0
    obama_face_encoding,    #1
    shinzo_abe_encoding,    #2
    dwayne_johnson_encoding #3
]

#results là mảng True/Flase cho biết liệu khuôn mặt lạ có trùng với khuôn mặt nào
# trong mảng đã biết không?
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

# begin Function
def choose_image(who):
    print("Khuôn mặt này là khuôn mặt của ", who )
    return
# end Function
#print("{}".format(results[2]))
def detect_face(file_name):
    img = cv2.imread(file_name)
    # Đọc 1 hình ảnh vào hệ thống
    # img = cv2.imread('obama.jpg')
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
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # In ra số lượng khuôn mặt có trong hình
    # print ("Tìm thấy {0} khuôn mặt!".format(len(faces)) )
    #####
    # Draw a rectangle around the faces in the original image
    # Vẽ một khung xung quanh khuôn mặt
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Faces found", img)
        cv2.waitKey(0)

    return
#####################################################################
#try:
if(("{}".format(results[3])) == "True" ):
        choose_image(who="Dwayne Johnson")
        print("Đã ghi nhận")
        print (unknown_face_encoding)
        detect_face("dwayne_johnson.jpg")
    # print (len(unknown_face_encoding))
if(("{}".format(results[2])) == "True" ):
        choose_image(who="Shinzo Abe")
        print("Đã ghi nhận")
        print (unknown_face_encoding)
        detect_face("shinzo_abe.jpg")
if(("{}".format(results[1])) == "True" ):
        choose_image(who="Barack Obama")
        print("Đã ghi nhận")
        print (unknown_face_encoding)
        detect_face("obama.jpg")
if(("{}".format(results[0])) == "True"):
        choose_image(who="Joe Biden")
        print("Đã ghi nhận")
        print(unknown_face_encoding)
        detect_face("biden.jpg")
    # print (len(unknown_face_encoding))
else:
        print()
        print("Người này chưa được nhận dạng !")





#####################################################################