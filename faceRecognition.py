import face_recognition 
from putin.encodings import encodings

def compare(image):
    unknown_image = face_recognition.load_image_file(image) 
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    for encoding in encodings:
        result = face_recognition.compare_faces([encoding], unknown_encoding)
        if result[0]:
            return True
    return False