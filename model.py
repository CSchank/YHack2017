
import numpy
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
with tf.device('/gpu:0'):
	seed = 7
	(x_train,y_train), (x_test,y_test) = boston_housing.load_data()
	# define base model
		
	# define wider model
	#def wider_model():
		# create model


	model = Sequential()
	model.add(Dense(10, input_dim=13, kernel_initializer='normal', activation='relu'))
	model.add(Dense(6, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal'))
		# Compile model
	model.compile(loss='mean_squared_error', optimizer='adam')
	history = model.fit(x_train,y_train,epochs = 800, batch_size = 10)
	score = model.evaluate(x_test,y_test)
	print(history.history.keys())

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