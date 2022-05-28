## Source Code for training the Machine Learning Model
This contains data and scripts for collecting and training the machine learning model for detecting emotions.
- `data_collection.py` contains script for collecting the data.
- `data_training.py` contains python script for training the data using mediapipe.
- `data` contains the data collected in form of numpy arrays.

### Instructions to run
To build the model from scratch:
- Run `data_collection.py` and create various expressions to depict emotions and collect the data.
- Secondly train the data using `data_training.py` by running `python data_training.py` in the terminal.
- Lastly run `inference` to test your model.
