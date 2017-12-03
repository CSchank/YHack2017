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
from keras import callbacks
def fitData(testData):
	testString = numpy.fromstring(testData,sep = ',')

	directory1 = os.path.dirname(os.path.realpath(__file__))
	pipe1 = joblib.load(os.path.join(directory2, 'pipeline_bronze.pkl'))
	model1 = models.load_model(os.path.join(directory2, 'model_bronze.h5'))
	pipe1.steps.append(('nn', model))
	bronze_pred = pipe.predict(X_TEST)


	directory1 = os.path.dirname(os.path.realpath(__file__))
	pipe1 = joblib.load(os.path.join(directory2, 'pipeline_silver.pkl'))
	model1 = models.load_model(os.path.join(directory2, 'model_silver.h5'))
	pipe1.steps.append(('nn', model))
	silver_pred = pipe.predict(X_TEST)

	directory1 = os.path.dirname(os.path.realpath(__file__))
	pipe1 = joblib.load(os.path.join(directory2, 'pipeline_gold.pkl'))
	model1 = models.load_model(os.path.join(directory2, 'model_gold.h5'))
	pipe1.steps.append(('nn', model))
	gold_pred = pipe.predict(X_TEST)


	directory1 = os.path.dirname(os.path.realpath(__file__))
	pipe1 = joblib.load(os.path.join(directory2, 'pipeline_plat.pkl'))
	model1 = models.load_model(os.path.join(directory2, 'model_plat.h5'))
	pipe1.steps.append(('nn', model))
	plat_pred = pipe.predict(X_TEST)


	directory1 = os.path.dirname(os.path.realpath(__file__))
	pipe1 = joblib.load(os.path.join(directory2, 'pipeline_picker.pkl'))
	model1 = models.load_model(os.path.join(directory2, 'model_picker.h5'))
	pipe1.steps.append(('nn', model))
	picker_pred = pipe.predict(X_TEST)

