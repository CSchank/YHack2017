import tensorflow as tf
import os
import numpy 
import pandas
from keras import models
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from sklearn.externals import joblib
from keras.models import load_model
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib
# load dataset

dataset = numpy.loadtxt("6k.csv", delimiter=",",skiprows=1)
#dataset = dataframe.values
#dataframe = np.loadtxt("data.csv", delimiter=",",skiprows=1,converters = converters)

#my_data = genfromtxt('housing.csv', delimiter=',')
# split into input (X) and output (Y) variables
#numpy.random.shuffle(dataset)
training,test = dataset[:5500,:],dataset[5999:,:]
X_TRAIN = training[:,1:75]
#np.delete(X,0,1)
Y_TRAIN = training[:,76]

X_TEST=test[:,1:75]
Y_TEST=test[:,76]
# define base model
sess = tf.Session()
K.set_session(sess)

def wider_model():
	# create model
	model = Sequential()
	model.add(Dense(50, input_dim=74, kernel_initializer='normal', activation='relu'))
	#model.add(Dense(6, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal'))
	# Compile model
	model.compile(loss='mean_squared_error', optimizer='adam')
	return model



# fix random seed for reproducibility
seed = 7
# evaluate model with standardized dataset
numpy.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
model = KerasRegressor(build_fn=wider_model, epochs=100, batch_size=10, verbose=0)
estimators.append(('mlp', model))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, X_TRAIN, Y_TRAIN, cv=kfold)
print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))
pipeline.fit(X_TRAIN,Y_TRAIN)
pred = pipeline.predict(X_TEST)
print(pred)
# print(pred.shape)
# print (mean_absolute_error(Y_TEST,pred))
directory = os.path.dirname(os.path.realpath(__file__))
model_step = pipeline.steps.pop(-1)[1]
joblib.dump(pipeline, os.path.join(directory,'pipeline_bronze.pkl'))
models.save_model(model_step.model,os.path.join(directory,'model_bronze.h5'))

print("loading")
directory2 = os.path.dirname(os.path.realpath(__file__))
pipe = joblib.load(os.path.join(directory2, 'pipeline_bronze.pkl'))
model = models.load_model(os.path.join(directory2, 'model_bronze.h5'))
pipe.steps.append(('nn', model))
pred = pipe.predict(X_TEST)
print(pred)