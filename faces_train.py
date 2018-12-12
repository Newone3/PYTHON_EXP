import os
import numpy as np
from PIL import Image
import cv2
import pickle



BASE_DIR = os.path.dirname(os.path.abspath(__file__))


image_dir = os.path.join(BASE_DIR, "images")

y_labels = []
x_train = []
current_id = 0
label_ids = {}

face_casdade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face_LBPHFaceRecognizer
recognizer.create()


for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            # print(label, path)

            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]
            # print(label_ids)


            # y_labels.append(label)  # nejaky cislo
            # x_train.append(path)    #overi obrazek, numpy array , gray
            pil_image = Image.open(path).convert("L") # grayscale
            image_array = np.array(pil_image, "uint8")
            # print(image_array)
            faces = face_casdade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

print(y_labels)
print(x_train)

with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.ym1")
