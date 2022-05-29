import streamlit as st
from streamlit_webrtc import webrtc_streamer

import av
import cv2
import numpy as np
import mediapipe as mp
from keras.models import load_model
import webbrowser



col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.write("")

with col2:
    st.image(".\Images\logo.png" , width=530, use_column_width=True)

with col3:
    st.write("")

st.title("Moosic")
st.write('Moosic is emotion detection based music reccommendation system. To get reccommended songs, start by allowing mic and camera for this web app.')




model  = load_model("model.h5")
label = np.load("labels.npy")

holistic = mp.solutions.holistic
hands = mp.solutions.hands
hol = holistic.Holistic()
drawing = mp.solutions.drawing_utils




if "run" not in st.session_state:
	st.session_state["run"] = "true"
try:
    detected_emotion = np.load("detected_emotion.npy")[0]
except:
    detected_emotion = ""

if not(detected_emotion):
	st.session_state["run"] = "true"
else:
	st.session_state["run"] = "false"




class EmotionDetector:
    def recv(self, frame):
        
        frm = frame.to_ndarray(format="bgr24")

        frm = cv2.flip(frm, 1) #Flipping the frame from left to right

        res = hol.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)) 

        lst = []

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
        
        lst = np.array(lst).reshape(1,-1)

        pred = label[np.argmax(model.predict(lst))]

        print(pred)
        cv2.putText(frm, pred, (50,50),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
        np.save("detected_emotion.npy", np.array([pred]))
        

        drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_TESSELATION)
        drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS)
        drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)

        return av.VideoFrame.from_ndarray(frm, format="bgr24")




lang = st.text_input("Enter your preferred language")
artist = st.text_input("Enter your preferred artist")

if lang and artist and st.session_state["run"] != "false":
    webrtc_streamer(key="key", desired_playing_state=True,
				video_processor_factory=EmotionDetector)


btn = st.button("Recommend music")

if btn:
	if not(detected_emotion):
		st.warning("Please let me capture your emotion first!")
		st.session_state["run"] = "true"
	else:
		webbrowser.open(f"https://www.youtube.com/results?search_query={lang}+{detected_emotion}+songs+{artist}")
		np.save("detected_emotion.npy", np.array([""]))
		st.session_state["run"] = "false"


st.write('Made with ❤ by [Khushi](https://github.com/khankhushi/Moosic)')

#Streamlit Customisation
st.markdown(""" <style>
header {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


