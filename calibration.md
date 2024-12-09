# Calibration Model 

The following files contain the code for the model and the required pipelining. 

In order to generate predictions only the MLP.py file is required to be run. Change the folder and files in main() in order to change what data sets are being loaded. 

In its current state MLP.py will use the data in /data and correctly output numpy arrays to the neural network. 

Expected input of files:
1. Raw data from quectel scripts as seen in /Measureing Scripts 
2. Unmodified data from Ray tracer

Output file: Currently no output prediction file is being made but the output is saved. 

**Changes to be done:**
1. Select a bigger data set. 
2. Tune network parameters 

**Limitations:**
The model performance will be heavily tied to the amount of training data availible. Since data has been collected manually our data set is too small for a good MLP performance. 
