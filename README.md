# Moodify - Facial emotion detection based music recommendation system
#### Submission for Microsoft Engage 2022
![logo](https://user-images.githubusercontent.com/81975567/170825957-55b94708-4893-4e13-a4aa-c5fa4ca9b070.png)

This project is built as a part of [Engage Mentorship Program 2022](https://acehacker.com/microsoft/engage2022) by Microsoft.

### Table of Contents
1. [About the Project](#about)
2. [Useful Links](#useful-links)
3. [Features Implemented](#features)
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
- [Deployed Website]()
- [Demo Video]()
- [Sprint Document]()
- [Design Document]()

### Features

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
-	`git clone https://github.com/khankhushi/Moodify`
-	Run `pip install -r requirements.txt` to install all dependencies.
-	`cd ./moodify`
-	`streamlit run app.py`
-	The app is now running at http://localhost:8501


#### Testing Web App
- Allow permissions for camera and mic when loading the web app.
- While testing, wait for the model to detect your emotions and click on recommend button to get songs based on a particular emotion
- Emotion used previously are stored in the cache and might cause an error in recommending music, REFRESH the site to resolve this. 4.	Emotion used previously are stored in the cache and might cause an error in recommending music, REFRESH the site to resolve this. 
- Recommended music is loaded in next tab as a youtube search query.

### System Architechture
![image](https://user-images.githubusercontent.com/81975567/170823667-70ffb002-f1bd-4578-b9a0-4ed32baee51d.png)

### Repository Structure
 This repository is organised as:
 - [app](/app.py) This file contain the setup of final web app.
 - [model](/model.h5) This file contains the trained model.




### Future Scope
- Integration of an inbuilt music player using  SpotiPy library, with spotify authentication.
- Addition of more gestures, and control of volume using gesture detection.
- Improved Reliablity and addition of User Feedback 

### References
- [Emotional Detection and Music Recommendation System
based on User Facial Expression - S Metilda Florence and M Uma](https://iopscience.iop.org/article/10.1088/1757-899X/912/6/062007/pdf)


