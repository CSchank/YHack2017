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
	testString = testString.reshape(1,-1)

	directory = os.path.dirname(os.path.realpath(__file__))
	pipe = joblib.load(os.path.join(directory, 'pipeline_bronze.pkl'))
	model = models.load_model(os.path.join(directory, 'model_bronze.h5'))
	pipe.steps.append(('nn', model))
	bronze_pred = pipe.predict(testString)

	print(bronze_pred)
	directory = os.path.dirname(os.path.realpath(__file__))
	pipe = joblib.load(os.path.join(directory, 'pipeline_silver.pkl'))
	model = models.load_model(os.path.join(directory, 'model_silver.h5'))
	pipe.steps.append(('nn', model))
	silver_pred = pipe.predict(testString)
	print(silver_pred)

	directory = os.path.dirname(os.path.realpath(__file__))
	pipe = joblib.load(os.path.join(directory, 'pipeline_gold.pkl'))
	model = models.load_model(os.path.join(directory, 'model_gold.h5'))
	pipe.steps.append(('nn', model))
	gold_pred = pipe.predict(testString)

	print(gold_pred)

	directory = os.path.dirname(os.path.realpath(__file__))
	pipe = joblib.load(os.path.join(directory, 'pipeline_plat.pkl'))
	model = models.load_model(os.path.join(directory, 'model_plat.h5'))
	pipe.steps.append(('nn', model))
	plat_pred = pipe.predict(testString)
	print(plat_pred)

	directory = os.path.dirname(os.path.realpath(__file__))
	pipe = joblib.load(os.path.join(directory, 'pipeline_picker.pkl'))
	model = models.load_model(os.path.join(directory, 'model_picker.h5'))
	pipe.steps.append(('nn', model))
	picker_pred = pipe.predict(testString)
	print(picker_pred)
	print(bronze_pred[0][0],silver_pred[0][0],gold_pred[0][0],plat_pred[0][0],picker_pred[0][0])
def main():
	fitData("24,0,70,102,3,-113,32,1,0,800000,400000,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,3,0,0,0,0,0")

	# id: 722 , ,24,46,79,123,1
if __name__ == "__main__":
	main()