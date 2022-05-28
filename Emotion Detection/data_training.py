import os
import numpy as np
import cv2

from tensorflow.keras.utils import to_categorical
from keras.layers import Input, Dense
from keras.models import Model

is_init = False
size = -1


# Converting associated labels to float/int
label = []
dictionary = {}
c = 0


#Searching for all the data in same directory
for i in os.listdir():
        if i.split(".")[-1] == "npy" and not(i.split(".")[0] == "labels"):  
                #Loading the files
                if not(is_init):
                        is_init = True 
                        X = np.load(i)
                        size = X.shape[0]
                        y = np.array([i.split('.')[0]]*size).reshape(-1,1)
                else:
                        X = np.concatenate((X, np.load(i)))
                        y = np.concatenate((y, np.array([i.split('.')[0]]*size).reshape(-1,1)))

                
                label.append(i.split('.')[0])
                dictionary[i.split('.')[0]] = c  
                c = c+1


#Converting associated labels to integers
for i in range(y.shape[0]):
	y[i, 0] = dictionary[y[i, 0]]
y = np.array(y, dtype="int32")


#Converting Integer to binary class matrix
y = to_categorical(y)


#Shuffling data to avoid clustering
id_new = X.copy()
al_new = y.copy()
counter = 0 

cnt = np.arange(X.shape[0])
np.random.shuffle(cnt)

for i in cnt: 
	id_new[counter] = X[i]
	al_new[counter] = y[i]
	counter = counter + 1

#Creating the model
input_layer = Input(shape=(X.shape[1]))
middle_layer1 = Dense(512, activation="relu")(input_layer)
middle_layer2 = Dense(256, activation="relu")(middle_layer1)
output_layer = Dense(y.shape[1], activation="softmax")(middle_layer2) 


model = Model(inputs=input_layer, outputs=output_layer)
model.compile(optimizer='rmsprop', loss="categorical_crossentropy", metrics=['acc'])

#Training the model
model.fit(X, y, epochs=50)

#Saving the model to use it later
model.save("model.h5")
np.save("labels.npy", np.array(label))
