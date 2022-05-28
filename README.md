# Moodify - Facial emotion detection based music reccomendation system
#### Submission for Microsoft Engage 2022
This project is built as a part of [Engage Mentorship Program 2022](https://acehacker.com/microsoft/engage2022) by Microsoft.

### Table of Contents
1. [About the Project](#about)
2. [Features Implemented](#features)
3. [Dependencies](#dependencies)
4. [Instructions](#instructions)
5. [Structure of this repository](#repository-structure)
6. [Useful Links](#useful-links)
7. [Future Scope](#future-scope)
8. [References](#references)


### About
This repository demonstrates an end-to-end pipeline for real-time Facial emotion recognition application along with reccommending music based on detected emotions.
Done in three steps:
1. Face Detection: from the video source using OpenCV.
2. Emotion Recognition: using a model trained by using Mediapipe library.
3. Music Recommendation: Using detected emotion to create a search query on Youtube

### Features

### Dependencies
- 
-
-
-
 
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

### Repository Structure
 This repository is organised as:
 - [app](/app.py) This file contain the setup of final web app.
 - [model](/model.h5) This file contains the trained model.


### Useful Links
- [Deployed Website]()
- [Demo Video]()
- [Sprint Document]()
- [Design Document]()

### Future Scope
- Integration of an inbuilt music player using  SpotiPy library, with spotify authentication.
- Addition of more gestures, and control of volume using gesture detection.
- Improved Reliablity and addition of User Feedback 


