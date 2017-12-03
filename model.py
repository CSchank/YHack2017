
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
#
dataset = np.loadtxt("new.csv", delimiter=",",skiprows=1)
#dataset = dataframe.values
#dataframe = np.loadtxt("data.csv", delimiter=",",skiprows=1,converters = converters)

#my_data = genfromtxt('housing.csv', delimiter=',')
# split into input (X) and output (Y) variables
np.random.shuffle(dataset)
training,test = dataset[:1000,:],dataset[1000:,:]
X_TRAIN = training[:,1:75]
#np.delete(X,0,1)
Y_TRAIN = training[:,79]

X_TEST=test[:,1:75]
Y_TEST=test[:,79]
with tf.device('/gpu:0'):
	seed = 7
	# define base model
		
	# define wider model
	#def wider_model():
		# create model


	model = Sequential()
	model.add(Dense(75, input_dim=74, kernel_initializer='normal', activation='tanh'))
	#model.add(Dense(30, input_dim=74, kernel_initializer='normal', activation='relu'))
	model.add(Dense(50, input_dim=74, kernel_initializer='normal', activation='tanh'))
	model.add(Dense(25, input_dim=74, kernel_initializer='normal', activation='tanh'))
	model.add(Dense(10, input_dim=74, kernel_initializer='normal', activation='tanh'))
	model.add(Dense(5, input_dim=74, kernel_initializer='normal', activation='tanh'))
	#model.add(Dense(6, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal'))
		# Compile model
	model.compile(loss='mean_absolute_error', optimizer='adam')
	history = model.fit(X_TRAIN,Y_TRAIN,epochs = 200, batch_size = 10)
	score = model.evaluate(X_TEST,Y_TEST)
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