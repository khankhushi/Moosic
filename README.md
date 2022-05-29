# Moosic - Facial emotion detection based music recommendation system
#### Submission for Microsoft Engage 2022
![logo](https://user-images.githubusercontent.com/81975567/170825957-55b94708-4893-4e13-a4aa-c5fa4ca9b070.png)

This project is built as a part of [Engage Mentorship Program 2022](https://acehacker.com/microsoft/engage2022) by Microsoft.

### Table of Contents
1. [About the Project](#about)
2. [Useful Links](#useful-links)
3. [Features](#features)
4. [Dependencies](#dependencies)
5. [Instructions](#instructions)
6. [System Architecture](#system-architechture)
7. [Structure of this repository](#repository-structure)
8. [Future Scope](#future-scope)
9. [References](#references)


### About
This repository demonstrates an end-to-end pipeline for real-time Facial emotion recognition application along with reccommending music based on detected emotions.
Done in three steps:
1. Face Detection: from the video source using OpenCV.
2. Emotion Recognition: using a model trained by using Mediapipe library.
3. Music Recommendation: Using detected emotion to create a search query on Youtube

The model is trained for 50 epochs and runs at 87% accuracy.
![image](https://user-images.githubusercontent.com/81975567/170823927-bd313103-7b34-42fd-9635-1b913ec65667.png)

### Useful Links
- [Demo Video](https://drive.google.com/file/d/18LERP3mieY1IuGvB4rP2dNVi7-gSJYCW/view?usp=sharing)
- [Sprint Document](https://drive.google.com/file/d/16Hw_z2g4PVrzBO97enPeikW0-3zO8n5i/view?usp=sharing)
- [Design Document](https://docs.google.com/presentation/d/1XoSN0gW_lVGJQSsLhSe6WVx80PbyMRAg/edit?usp=sharing&ouid=109023606663997444374&rtpof=true&sd=true)

### Features
1. Landing Page
![image](https://user-images.githubusercontent.com/81975567/170835333-7a69618e-3f3c-46e9-90b1-b6fc72cc5553.png)


Seamless landing page filled with dark-theme.

2. Detection of various emotions like [Sad, Angry, Happy, Neutral, Surprise]
![image](https://user-images.githubusercontent.com/81975567/170837282-d7f80ebc-cb69-4b86-ba6e-5f1c3f58e7d8.png)

3. Detection of various gestures like [Hello, Thumbsup, Nope, Rock]
![image](https://user-images.githubusercontent.com/81975567/170837584-d47e2b7f-0499-4a99-b8f3-25a8e743d97d.png)





### Dependencies
This project depends on Python and following packages which can be easily installed through `requirements.txt` file by running the following command:
`pip install -r requirements.txt`
- Python 3.9.6
- pip 22.1.1
- streamlit 1.9.1
- streamlit-webrtc 0.37.0
- opencv-python 4.5.5.64
- mediapipe 0.8.10
 
### Instructions
#### Testing Locally
-	`git clone https://github.com/khankhushi/Moosic`
-	Run `pip install -r requirements.txt` to install all dependencies.
-	`cd ./moosic`
-	`streamlit run app.py`
-	The app is now running at http://localhost:8501
-	While testing, wait for the model to detect your emotions and click on recommend button to get songs based on a particular emotion
- Emotion used previously are stored as cache and might cause an error in recommending music, delete `detected_emotion.npy file` in the directory to resolve this. 
- Recommended music is loaded in next tab as a youtube search query.

### System Architechture
![image](https://user-images.githubusercontent.com/81975567/170823667-70ffb002-f1bd-4578-b9a0-4ed32baee51d.png)

### Repository Structure
 This repository is organised as:
 - [app](/app.py) This file contain the setup of final web app.
 - [model](/model.h5) This file contains the trained model.
 - [Emotion Detection](./Emotion%20Detection) This folder contains python scripts to train the model.
 - [.streamlit](./.streamlit) This folder contains configuration files for the streamlit theme in Web App.




### Future Scope
- Deploying the web app.
- Integration of an inbuilt music player using  SpotiPy library, with spotify authentication.
- Addition of more gestures, and control of volume using gesture detection.
- Improved Reliablity and addition of User Feedback 

### References
- [Emotional Detection and Music Recommendation System
based on User Facial Expression - S Metilda Florence and M Uma](https://iopscience.iop.org/article/10.1088/1757-899X/912/6/062007/pdf)


