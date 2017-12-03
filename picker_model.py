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
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
# load dataset

dataset = numpy.loadtxt("6k.csv", delimiter=",",skiprows=1)
#dataset = dataframe.values
#dataframe = np.loadtxt("data.csv", delimiter=",",skiprows=1,converters = converters)

#my_data = genfromtxt('housing.csv', delimiter=',')
# split into input (X) and output (Y) variables
#numpy.random.shuffle(dataset)

training,test = dataset[:5000,:],dataset[5900:,:]
encoder = LabelEncoder()

X_TRAIN = training[:,1:76]
#np.delete(X,0,1)
Y_TRAIN = training[:,80]
print(Y_TRAIN.shape)
for i in range(Y_TRAIN.size):
	Y_TRAIN[i] += 1
	print(Y_TRAIN[i] )
encoder.fit(Y_TRAIN)
encoded_Y = encoder.transform(Y_TRAIN)
dummy_y = np_utils.to_categorical(encoded_Y)

X_TEST=test[:,1:76]
Y_TEST=test[:,80]
# define base model
sess = tf.Session()
K.set_session(sess)

def wider_model():
	# create model
	model = Sequential()
	model.add(Dense(50, input_dim=75,  activation='relu'))
	#model.add(Dense(6, kernel_initializer='normal', activation='relu'))
	model.add(Dense(4, activation = 'softmax'))
	# Compile model
	model.compile(loss='mean_squared_error', optimizer='adam',metrics=['accuracy'])
	return model



# fix random seed for reproducibility
seed = 7
# evaluate model with standardized dataset
numpy.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
model = KerasClassifier(build_fn=wider_model, epochs=100, batch_size=50, verbose=0)
estimators.append(('mlp', model))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10,shuffle = True, random_state=seed)
results = cross_val_score(pipeline, X_TRAIN, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
pipeline.fit(X_TRAIN,dummy_y)
pred = pipeline.predict_proba(X_TEST)
print(pred)
#print (accuracy_score(Y_TEST,pred))
directory = os.path.dirname(os.path.realpath(__file__))
model_step = pipeline.steps.pop(-1)[1]
joblib.dump(pipeline, os.path.join(directory,'pipeline_picker.pkl'))
models.save_model(model_step.model,os.path.join(directory,'model_picker.h5'))

print("test")
directory2 = os.path.dirname(os.path.realpath(__file__))
pipe = joblib.load(os.path.join(directory2, 'pipeline_picker.pkl'))
model = models.load_model(os.path.join(directory2, 'model_picker.h5'))
pipe.steps.append(('nn', model))
pred = pipe.predict(X_TEST)
print(pred)