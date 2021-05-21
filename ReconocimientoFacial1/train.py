import cv2
import numpy as np
import os

data_path='C:/Github/Python/ReconocimientoFacial1/data'
data_list=os.listdir(data_path)

ids=[]
data_face=[]
id=0
for row in data_list:
    final_path=data_path+"/"+row
    for file in os.listdir(final_path):
        ids.append(id)
        data_face.append(cv2.imread(final_path+"/"+file,0))
    id+=1

model1_train=cv2.face.EigenFaceRecognizer_create()
print("Train")
model1_train.train(data_face,np.array(ids))

