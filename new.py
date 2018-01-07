# Lib to numeric analysis and computer vision (opencv)
import numpy as np
import cv2
import face_recognition
import PIL

#####################################################################
# Numpy array in line 38

# Thêm hình ảnh từng người vào mảng numpy để  lưu trữ
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")
shinzo_abe_image = face_recognition.load_image_file("shinzo_abe.jpg")
dwayne_johnson_image = face_recognition.load_image_file("dwayne_johnson.jpg")
mark_zuckerberg_image = face_recognition.load_image_file("mark_zuckerberg.jpg")
# ###################################################

## Chọn 1 hình ảnh muốn nhận dạng
#image_file =  "0.jpg"
#image_file =  "1.jpg"
#image_file =  "2.jpg"
#image_file =  "3.jpg"
image_file =  "4.jpg"
#image_file =  "biden.jpg"
#image_file =  "mark_zuckerberg.jpg"  # không có trong dữ liệu encoding

unknown_image = face_recognition.load_image_file(image_file)

# Chuyển hình ảnh thành mã encodings
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
dwayne_johnson_encoding = face_recognition.face_encodings(dwayne_johnson_image)[0]
shinzo_abe_encoding = face_recognition.face_encodings(shinzo_abe_image)[0]

mark_zuckerberg_encoding = face_recognition.face_encodings(mark_zuckerberg_image)[0]

# thêm một hình của người lạ mặt vào
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

known_faces = [
    biden_face_encoding,     #0
    obama_face_encoding,     #1
    shinzo_abe_encoding,     #2
    dwayne_johnson_encoding  #3
]
name_data = dict([(0, "Joe Biden"),
                  (1, "Barack Obama"),
                  (2, "Shinzo Abe"),
                  (3, "Dwayne Johnson")
])

#results là mảng True/Flase cho biết liệu khuôn mặt lạ có trùng với khuôn mặt nào
# trong mảng đã biết không?
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

# begin Function
def show_name(who):
    print("Khuôn mặt này là khuôn mặt của ", who)
    print("Đã ghi nhận")
    return
# end Function
#print("{}".format(results[2]))
# begin Function
def detect_face( file_name ): # truyền tên file khi gọi hàm
    # Đọc 1 hình ảnh vào hệ thống
    img = cv2.imread(file_name)
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

    # Vẽ một khung xung quanh khuôn mặt
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        for k, v in name_data.items():
            if(("{}".format(results[k])) == "True" ):
                cv2.putText(img, str(v), (h + 6, w - 6), font, 1.0, (255, 255, 255), 1)
                #else:
                #    cv2.putText(img, "Chua nhan dang", (h + 6, w - 6), font, 1.0, (255, 255, 255), 1)
            cv2.imshow("Faces found", img)
            cv2.waitKey(0)
    return
# end Function detect_face()
#####################################################################
# view more in line 47
for _key, _value in name_data.items():
    if(("{}".format(results[_key])) == "True" ):  # nếu encoding trùng với encoding có index = 3
        show_name(who= _value)
        print (unknown_face_encoding)
        detect_face(image_file)
    else:
        print()
        print("Khuôn mặt này chưa được nhận dạng !")
        detect_face(image_file)

#####################################################################