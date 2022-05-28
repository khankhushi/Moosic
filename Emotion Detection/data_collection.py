import mediapipe as mp
import numpy as np
import cv2


#Establishing connection to the webcam camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#Entering the file name for collected data
name = input("Enter the name of the data : ")

#Using holistic solution from Media Pipe library
holistic = mp.solutions.holistic
hands = mp.solutions.hands
hol = holistic.Holistic()
drawing = mp.solutions.drawing_utils

row_collection = []
data_size = 0


while True:
    lst = [] #List for storing all the landmarks as numpy array

    _, frm = cap.read()

    frm = cv2.flip(frm, 1) #Flipping the frame from left to right

    res = hol.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)) #Converting color from BGR to RGB


    #Storing Landmark data
    if res.face_landmarks:
        for i in res.face_landmarks.landmark:
                lst.append(i.x - res.face_landmarks.landmark[1].x)
                lst.append(i.y - res.face_landmarks.landmark[1].y)

    if res.left_hand_landmarks:
            for i in res.left_hand_landmarks.landmark:
                lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
    else:
            for i in range(42):
                lst.append(0.0)

    if res.right_hand_landmarks:
            for i in res.right_hand_landmarks.landmark:
                lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
    else:
            for i in range(42):
                lst.append(0.0)
    
    row_collection.append(lst)
    data_size = data_size + 1


    #Drawing landmarks on the frame
    drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_TESSELATION)
    drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS)
    drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)
 

    # Show image back to  screen
    cv2.imshow("window", frm)


    if cv2.waitKey(1) == 27 or data_size>99:
        cv2.destroyAllWindows() # Close the image show frame
        cap.release() #Releasing WebCam
        break

#Optimising the data collected
np.save(f"{name}.npy", np.array(row_collection))
print(np.array(row_collection).shape)


