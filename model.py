
import numpy as np
import pandas
import tensorflow as tf
#import keras.backend as K
from numpy import genfromtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import boston_housing
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# load dataset
#dataframe = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)
#dataset = dataframe.values

#my_data = genfromtxt('housing.csv', delimiter=',')
# split into input (X) and output (Y) variables
#X = dataset[:,0:12]
#Y = dataset[:,13]
dataframe = pandas.read_csv("housing.csv", delim_whitespace=True,header = None, usecols=[0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76] )
dataset = dataframe.values
#dataframe = np.loadtxt("data.csv", delimiter=",",skiprows=1,converters = converters)

#my_data = genfromtxt('housing.csv', delimiter=',')
# split into input (X) and output (Y) variables
X = dataset[1:,1:76]
#np.delete(X,0,1)
Y = dataset[1:,76]
with tf.device('/gpu:0'):
	seed = 7
	# define base model
		
	# define wider model
	#def wider_model():
		# create model


	model = Sequential()
	model.add(Dense(200, input_dim=75, kernel_initializer='normal', activation='relu'))
	#model.add(Dense(6, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal'))
		# Compile model
	model.compile(loss='mean_squared_error', optimizer='adam')
	history = model.fit(X,Y,epochs = 200, batch_size = 10)
	#score = model.evaluate(x_test,y_test)
	#print(history.history.keys())

	#print('Test loss: ', score)
		#return model



# fix random seed for reproducibility
# seed = 7
# # evaluate model with standardized dataset
# numpy.random.seed(seed)
# estimators = []
# estimators.append(('standardize', StandardScaler()))
# estimators.append(('mlp', KerasRegressor(build_fn=wider_model, epochs=100, batch_size=10, verbose=0)))
# pipeline = Pipeline(estimators)
# kfold = KFold(n_splits=10, random_state=seed)
# results = cross_val_score(pipeline, X, Y, cv=kfold)
# print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))
# print(history.history.keys())