from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
#image = face_recognition.load_image_file("biden.jpg")
image = face_recognition.load_image_file("trump-putin.jpg")

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

#print("I found {} face(s) in this photograph.".format(len(face_locations)))
print("Tìm thấy {} khuôn mặt trong tấm hình này.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    print(
        "Khuôn mặt được xác định tại vị trí có tọa độ Trên: {}, Trái: {}, Dưới: {}, Phải: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
