import face_recognition
from tkinter import *
import tkinter as tk

# Load the jpg files into numpy arrays
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")

unknown_image = face_recognition.load_image_file("obama2.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encordings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# thêm một hình của người lạ mặt vào
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

known_faces = [
    biden_face_encoding,
    obama_face_encoding
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
#results là mảng True/Flase cho biết liệu khuôn mặt lạ có trùng với khuôn mặt nào
# trong mảng đã biết không?
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

#print("Is the unknown face a picture of Biden? {}".format(results[0]))
#print("Is the unknown face a picture of Obama? {}".format(results[1]))
#print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))

print("Khuôn mặt chưa nhận dạng này có phải là hình của Biden? {}".format(results[0]))
print("Khuôn mặt chưa nhận dạng này có phải là hình của Obama? {}".format(results[1]))
print("Khuôn mặt chưa nhận dạng này có phải là một người mới mà "
      "chúng ta chưa từng thấy trước đây ? {}".format(not True in results))

'''
### main:
root = tk.Tk()
root.title("Face Regconition")
root.configure(background="brown")
root.geometry("600x450")



### show_result function:





### Run button
#Button(root, text="Run demo", width=14, command=show_result).grid(row=4, column=0, sticky=W)

### Result label
Label(root, text="\nResult:", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)

### create a text box
output = Text(root, width=75, height=6, wrap=WORD, background="white")
output.grid(row=7, column=0, columnspan=2, sticky=W)

### exit label:
Label(root, text="Click 'Exit' to exit", bg="white", fg="black", font="none 12 bold").grid(row=8, column=0, sticky=W)


### exit function
def close_window():
    root.destroy()
    exit()


### exit button:
Button(root, text="Exit", width=14, command=close_window).grid(row=9, column=0, sticky=W)


###
root.mainloop() 
'''
