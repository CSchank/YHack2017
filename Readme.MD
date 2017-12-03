#Vitech Insurance Quote Predictor and Plan Recommender: Mcmaster Team #1 (The Beard)



##Quoting the Price:
--------------
A wide neural network was used to model the quoted price for each plan. Unfortunately there was little time/processing power to play around with the hyperparameters of the network, however for price prediction were able to achieve a low mean squared error (between 10-12 each plan) which would be an average absolute error of **around $3** in the montly plan price. Four seperate regression networks were for each plan using 5500 randomly selected entries from the database of people. As there were too many ICD codes to process, we condensed the codes into their hierarchical buckets and tracked the number of "high","medium", and "low" risk conditions per bucket and fed that into the network. The network parameters and hyperparameters were saved to two files per network and loaded as needed. *Network could be improved with more training time and data*

###Code
-bronze_quote_model.py: model for the network used to quote prices for the bronze plan (Mean Square Error ~ 10)
-silver_quote_model.py: model for the network used to quote prices for the silver plan (Mean Square Error ~ 11)
-gold_quote_model.py: model for the network used to quote prices for the gold plan (Mean Square Error ~ 12)
-plat_quote_model.py: model for the network used to quote prices for the platinum plan (Mean Square Error ~ 12)
-fitData.py: used by the server to compile the saved network data and make predictions

##Guessing the Purchased Plan:
--------------
Guessing the plan the customer picks was one of our ambitious goals. We were able to construct a basic wide neural network for classification(no reason for width instead of depth) however there was not enough time or processing power to tune the hyperparameters. Prediction accuracy was low for the test data we used, indicating that either **not enough training data was used, or that there was no relation between parameters and plan chosen**
 Initially the quoted price plans were included in the parameters, however we found that these did not actually affect the accuracy of our network for the limited training data we had. In the end, this classification network made use of the same 5500 randomly selected entries as the regression networks. 
###Code
-picker_model.py: model for the network used to quote prices for the bronze plan (Accuracy ~ 35%)
-fitData.py: used by the server to compile the saved network data and make predictions

##Modules and Architecture:
--------------
- The neural networks made use o
##Problems:
--------------
Unfortunately there were many limiting factors towards training our model. The primary issue we ran into was the lack of internet connectivity which incredibely restricted our ability to work on this problem. Our initial intention was to host all the parameters we needed in a Google Cloud bucket and make use of the Google Cloud Platform's machine learning to make use of the platforms power and robustness. 

##Future Work and Improvements:
--------------









*This will be Italic*

**This will be Bold**

- This will be a list item
- This will be a list item
