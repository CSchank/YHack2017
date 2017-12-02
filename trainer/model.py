
"""Implements the Keras Sequential model."""

import itertools

import keras
import pandas as pd
from keras import backend as K
from keras import layers, models
from keras.utils import np_utils
from keras.backend import relu, sigmoid, tanh

from urlparse import urlparse

import tensorflow as tf
from tensorflow.python.saved_model import builder as saved_model_builder
from tensorflow.python.saved_model import utils
from tensorflow.python.saved_model import tag_constants, signature_constants
from tensorflow.python.saved_model.signature_def_utils_impl import build_signature_def, predict_signature_def
from tensorflow.contrib.session_bundle import exporter

# csv columns in the input file
# CSV_COLUMNS = ('age', 'workclass', 'fnlwgt', 'education', 'education_num',
#                'marital_status', 'occupation', 'relationship', 'race',
#                'gender', 'capital_gain', 'capital_loss', 'hours_per_week',
#                'native_country', 'income_bracket')

# CSV_COLUMN_DEFAULTS = [[0], [''], [0], [''], [0], [''], [''], [''], [''],
#                        [''], [0], [0], [0], [''], ['']]

# # Categorical columns with vocab size
# # native_country and fnlwgt are ignored
# CATEGORICAL_COLS = (('education', 16), ('marital_status', 7),
#                     ('relationship', 6), ('workclass', 9), ('occupation', 15),
#                     ('gender', [' Male', ' Female']), ('race', 5))

# CONTINUOUS_COLS = ('age', 'education_num', 'capital_gain', 'capital_loss',
#                    'hours_per_week')

# LABELS = [' <=50K', ' >50K']
# LABEL_COLUMN = 'income_bracket'
CSV_COLUMNS = ('age', 'sex','height', 'weight', 'city','state',
              'longitude','latitude','marital_status', 'tobacco',
               'optional_insurance', 'annual_income', 'people_covered'
               'a00_b99_high', 'a00_b99_med','a00_b99_low',
               'c00_d49_high', 'c00_d49_med','c00_d49_low',
               'd50_d89_high', 'd50_d89_med','d50_d89_low',
               'e00_e89_high', 'e00_e89_med','e00_e89_low',
               'f01_f99_high', 'f01_f99_med','f01_f99_low',
               'g00_g99_high', 'g00_g99_med','g00_g99_low',
               'h00_h59_high', 'h00_h59_med','h00_h59_low',
               'h60_h95_high', 'h60_h95_med','h60_h95_low',
               'i00_i99_high', 'i00_i99_med','i00_i99_low',
               'j00_j99_high', 'j00_j99_med','j00_j99_low',
               'k00_k95_high', 'k00_k95_med','k00_k95_low',
               'l00_l99_high', 'l00_l99_med','l00_l99_low',
               'm00_m99_high', 'm00_m99_med','m00_m99_low',
               'n00_n99_high', 'n00_n99_med','n00_n99_low',
               'o00_o9a_high', 'o00_o9a_med','o00_o9a_low',
               'p00_p96_high', 'p00_p96_med','p00_p96_low',
               'q00_q99_high', 'q00_q99_med','q00_q99_low',
               'r00_r99_high', 'r00_r99_med','r00_r99_low',
               's00_t88_high', 's00_t88_med','s00_t88_low',
               'v00_y99_high', 'v00_y99_med','v00_y99_low',
               'z00_z99_high', 'z00_z99_med','z00_z99_low',
               'bronze_quote','silver_quote', 'gold_quote',
               'platinum_quote','purchased_plan')

CSV_COLUMN_DEFAULTS = [[0], ['F'], [0], [0], [''], [''],
                       [0], [0], ['S'],['Y'],
                       [500000],[0],[1],
                       [0],[0],[0], #a
                       [0],[0],[0], #c
                       [0],[0],[0], #d
                       [0],[0],[0], #e
                       [0],[0],[0], #f
                       [0],[0],[0], #g
                       [0],[0],[0], #h0`
                       [0],[0],[0], #h6
                       [0],[0],[0], #i
                       [0],[0],[0], #j
                       [0],[0],[0], #k
                       [0],[0],[0], #l
                       [0],[0],[0], #m
                       [0],[0],[0], #n
                       [0],[0],[0], #o 
                       [0],[0],[0], #p
                       [0],[0],[0], #q
                       [0],[0],[0], #r
                       [0],[0],[0], #s
                       [0],[0],[0], #v
                       [0],[0],[0], #z
                       [20],[40],[70],[110],['']]

# Categorical columns with vocab size
# native_country and fnlwgt are ignored
CATEGORICAL_COLS = (('marital_status', ['S','M']),('tobacco', ['Y','N']),
                    ('state',51),())

CONTINUOUS_COLS = ('age', 'height','weight','longitude','latitude',
                 'annual_income','optional_insurance','people_covered',
                 'a00_b99_high', 'a00_b99_med','a00_b99_low',
                 'c00_d49_high', 'c00_d49_med','c00_d49_low',
                 'd50_d89_high', 'd50_d89_med','d50_d89_low',
                 'e00_e89_high', 'e00_e89_med','e00_e89_low',
                 'f01_f99_high', 'f01_f99_med','f01_f99_low',
                 'g00_g99_high', 'g00_g99_med','g00_g99_low',
                 'h00_h59_high', 'h00_h59_med','h00_h59_low',
                 'h60_h95_high', 'h60_h95_med','h60_h95_low',
                 'i00_i99_high', 'i00_i99_med','i00_i99_low',
                 'j00_j99_high', 'j00_j99_med','j00_j99_low',
                 'k00_k95_high', 'k00_k95_med','k00_k95_low',
                 'l00_l99_high', 'l00_l99_med','l00_l99_low',
                 'm00_m99_high', 'm00_m99_med','m00_m99_low',
                 'n00_n99_high', 'n00_n99_med','n00_n99_low',
                 'o00_o9a_high', 'o00_o9a_med','o00_o9a_low',
                 'p00_p96_high', 'p00_p96_med','p00_p96_low',
                 'q00_q99_high', 'q00_q99_med','q00_q99_low',
                 'r00_r99_high', 'r00_r99_med','r00_r99_low',
                 's00_t88_high', 's00_t88_med','s00_t88_low',
                 'v00_y99_high', 'v00_y99_med','v00_y99_low',
                 'z00_z99_high', 'z00_z99_med','z00_z99_low',
                 'bronze_quote','silver_quote', 'gold_quote',
                 'platinum_quote' )

LABELS = ['Bronze', 'Silver', 'Gold' ,'Platinum']
LABEL_COLUMN = 'purchased_plan'

# UNUSED_COLUMNS = set(CSV_COLUMNS) - set(
#     zip(*CATEGORICAL_COLS)[0] + CONTINUOUS_COLS + (LABEL_COLUMN,))


def model_fn(input_dim,
             labels_dim,
             hidden_units=[100, 70, 50, 20],
             learning_rate=0.1):

  """Create a Keras Sequential model with layers."""
  model = models.Sequential()

  for units in hidden_units:
    model.add(layers.Dense(units=units,
                           input_dim=input_dim,
                           activation=relu))
    input_dim = units

  # Add a dense final layer with sigmoid function
  model.add(layers.Dense(labels_dim, activation=tanh))

  compile_model(model, learning_rate)
  return model

def compile_model(model, learning_rate):
  model.compile(loss='categorical_crossentropy',
                optimizer=keras.optimizers.SGD(lr=learning_rate),
                metrics=['accuracy'])
  return model

def to_savedmodel(model, export_path):
  """Convert the Keras HDF5 model into TensorFlow SavedModel."""

  builder = saved_model_builder.SavedModelBuilder(export_path)

  signature = predict_signature_def(inputs={'input': model.inputs[0]},
                                    outputs={'income': model.outputs[0]})

  with K.get_session() as sess:
    builder.add_meta_graph_and_variables(
        sess=sess,
        tags=[tag_constants.SERVING],
        signature_def_map={
            signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: signature}
    )
    builder.save()


def to_numeric_features(features):
  """Convert the pandas input features to numeric values.
     Args:
        features: Input features in the data
          age (continuous)
          workclass (categorical)
          fnlwgt (continuous)
          education (categorical)
          education_num (continuous)
          marital_status (categorical)
          occupation (categorical)
          relationship (categorical)
          race (categorical)
          gender (categorical)
          capital_gain (continuous)
          capital_loss (continuous)
          hours_per_week (continuous)
          native_country (categorical)
  """

  for col in CATEGORICAL_COLS:
    features = pd.concat([features, pd.get_dummies(features[col[0]], drop_first = True)], axis = 1)
    features.drop(col[0], axis = 1, inplace = True)

  # Remove the unused columns from the dataframe
  for col in UNUSED_COLUMNS:
    features.pop(col)

  return features

def generator_input(input_file, chunk_size):
  """Generator function to produce features and labels
     needed by keras fit_generator.
  """
  input_reader = pd.read_csv(tf.gfile.Open(input_file[0]),
                           names=CSV_COLUMNS,
                           chunksize=chunk_size,
                           na_values=" ?")

  for input_data in input_reader:
    input_data = input_data.dropna()
    label = pd.get_dummies(input_data.pop(LABEL_COLUMN))

    input_data = to_numeric_features(input_data)
    n_rows = input_data.shape[0]
    return ( (input_data.iloc[[index % n_rows]], label.iloc[[index % n_rows]]) for index in itertools.count() )
