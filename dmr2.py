# -*- coding: utf-8 -*-
"""dmr2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OEAYorz8S4i_xTu48M-h357yLIf0YoCf

## **Import some libraries**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

train = pd.read_csv('Training.csv')

train.head()

"""## **data wrangling**"""

train.columns.values

#List of the symptoms.
symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions',
       'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
       'vomiting', 'burning_micturition', 'spotting_ urination',
       'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
       'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
       'patches_in_throat', 'irregular_sugar_level', 'cough',
       'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
       'dehydration', 'indigestion', 'headache', 'yellowish_skin',
       'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
       'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
       'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
       'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
       'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
       'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
       'fast_heart_rate', 'pain_during_bowel_movements',
       'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
       'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
       'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
       'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
       'excessive_hunger', 'extra_marital_contacts',
       'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
       'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
       'swelling_joints', 'movement_stiffness', 'spinning_movements',
       'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
       'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
       'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
       'altered_sensorium', 'red_spots_over_body', 'belly_pain',
       'abnormal_menstruation', 'dischromic _patches',
       'watering_from_eyes', 'increased_appetite', 'polyuria',
       'family_history', 'mucoid_sputum', 'rusty_sputum',
       'lack_of_concentration', 'visual_disturbances',
       'receiving_blood_transfusion', 'receiving_unsterile_injections',
       'coma', 'stomach_bleeding', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload.1',
       'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
       'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
       'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
       'inflammatory_nails', 'blister', 'red_sore_around_nose',
       'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

train.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_train= train[symptoms]

y_train = train[["prognosis"]]
#change a 2-dimensional array or a multi-dimensional array into a contiguous flattened array.
np.ravel(y_train)

input_data = pd.read_csv('Training.csv')
input_data.head()

#They are 4920 rows, 133 columns
input_data.shape

"""## **See the Target Variable Distribution**"""

#looking how much percent each diseases having
input_data['prognosis'].value_counts(normalize = True)

#as we can see each no. diseases having the same percentage through bar chart
input_data['prognosis'].value_counts(normalize = True).plot.bar(color='pink')
plt.subplots_adjust(left = 0.9, right = 2 , top = 2, bottom = 1)

"""Check the relationship between the variables by applying the correlation"""

#checking the relationship between the variables by applying the correlation 
corr = input_data.corr()
mask = np.array(corr)
mask[np.tril_indices_from(mask)] = False
plt.subplots_adjust(left = 0.5, right = 16 , top = 20, bottom = 0.5)
sns.heatmap(corr, mask=mask,vmax=.9, square=True,annot=True, cmap="YlGnBu")

"""DECISION TREE!!!!"""

# decision treee:::::

import numpy as np
import pandas as pd
from sklearn import metrics

#read and print dataset
df=pd.read_csv("Training.csv")
value=['itching', 'skin_rash', 'nodal_skin_eruptions',
       'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
       'vomiting', 'burning_micturition', 'spotting_ urination',
       'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
       'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
       'patches_in_throat', 'irregular_sugar_level', 'cough',
       'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
       'dehydration', 'indigestion', 'headache', 'yellowish_skin',
       'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
       'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
       'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
       'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
       'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
       'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
       'fast_heart_rate', 'pain_during_bowel_movements',
       'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
       'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
       'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
       'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
       'excessive_hunger', 'extra_marital_contacts',
       'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
       'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
       'swelling_joints', 'movement_stiffness', 'spinning_movements',
       'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
       'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
       'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
       'altered_sensorium', 'red_spots_over_body', 'belly_pain',
       'abnormal_menstruation', 'dischromic _patches',
       'watering_from_eyes', 'increased_appetite', 'polyuria',
       'family_history', 'mucoid_sputum', 'rusty_sputum',
       'lack_of_concentration', 'visual_disturbances',
       'receiving_blood_transfusion', 'receiving_unsterile_injections',
       'coma', 'stomach_bleeding', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload.1',
       'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
       'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
       'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
       'inflammatory_nails', 'blister', 'red_sore_around_nose',
       'yellow_crust_ooze']
df

from sklearn import preprocessing
string_to_int= preprocessing.LabelEncoder()                
df=df.apply(string_to_int.fit_transform) 
df

feature_cols = ['itching', 'skin_rash', 'nodal_skin_eruptions',
       'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
       'vomiting', 'burning_micturition', 'spotting_ urination',
       'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
       'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
       'patches_in_throat', 'irregular_sugar_level', 'cough',
       'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
       'dehydration', 'indigestion', 'headache', 'yellowish_skin',
       'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
       'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
       'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
       'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
       'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
       'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
       'fast_heart_rate', 'pain_during_bowel_movements',
       'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
       'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
       'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
       'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
       'excessive_hunger', 'extra_marital_contacts',
       'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
       'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
       'swelling_joints', 'movement_stiffness', 'spinning_movements',
       'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
       'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
       'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
       'altered_sensorium', 'red_spots_over_body', 'belly_pain',
       'abnormal_menstruation', 'dischromic _patches',
       'watering_from_eyes', 'increased_appetite', 'polyuria',
       'family_history', 'mucoid_sputum', 'rusty_sputum',
       'lack_of_concentration', 'visual_disturbances',
       'receiving_blood_transfusion', 'receiving_unsterile_injections',
       'coma', 'stomach_bleeding', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload.1',
       'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
       'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
       'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
       'inflammatory_nails', 'blister', 'red_sore_around_nose',
       'yellow_crust_ooze']
X = df[feature_cols]                        
y = df.prognosis

#The train_test_split function of the sklearn. model_selection package in Python splits arrays or matrices into random subsets for train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

#DecisionTreeClassifier is a class capable of performing multi-class classification on a dataset. 
#The 'fit' method trains the algorithm on the training data, after the model is initialized.

from sklearn.tree import DecisionTreeClassifier                            
classifier =DecisionTreeClassifier(criterion="entropy", random_state=100)   
classifier.fit(X_train, y_train)

#predict() function enables us to predict the labels of the data values on the basis of the trained model. 

y_pred= classifier.predict(X_test)

X_test

y_pred

#In multilabel classification, this function computes subset accuracy: the set of labels predicted for a sample must exactly match the corresponding set of labels in y_test.
from sklearn.metrics import accuracy_score
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

data_p=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})  
data_p

#Compute confusion matrix to evaluate the accuracy of a classification.
from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test, y_pred))  
print(classification_report(y_test, y_pred))

import graphviz

#This function generates a GraphViz representation of the decision tree, 
from sklearn.tree import export_graphviz

#Six is a Python 2 and 3 compatibility library
#The sys module provides information about constants, functions and methods of the Python interpreter
import six
import sys
sys.modules['sklearn.externals.six'] = six
from sklearn.externals.six import StringIO

# improved version of the old pydot project that provides a Python Interface to Graphviz's Dot language.
import pydotplus

from IPython.display import Image

dot_data = StringIO()

export_graphviz(classifier, out_file=dot_data, filled=True, rounded=True, special_characters=True,feature_names=value,class_names=['Fungal infection' ,
'Hepatitis C ',                               
'Hepatitis E ',                              
'Alcoholic hepatitis '                       ,
'Tuberculosis  '                             ,
'Common Cold     '                           ,
'Pneumonia '                                 ,
'Dimorphic hemmorhoids(piles)'               ,
'Heart attack'                               ,
'Varicose veins'                             ,
'Hypothyroidism'                             ,
'Hyperthyroidism'                            ,
'Hypoglycemia '                              ,
'Osteoarthristis'                            ,
'Arthritis  '                                ,
'(vertigo) Paroymsal  Positional Vertigo '   ,
'Acne ',
'Urinary tract infection '                   ,
'Psoriasis  '                                ,
'Hepatitis D   '                             ,
'Hepatitis B   '                             ,
'Allergy'                                    ,
'hepatitis A '                               ,
'GERD '                                      ,
'Chronic cholestasis'                        ,
'Drug Reaction '                             ,
'Peptic ulcer diseae '                       ,
'AIDS  '                                     ,
'Diabetes  '                                 ,
'Gastroenteritis  '                          ,
'Bronchial Asthma '                          ,
'Hypertension  '                             ,
'Migraine '                                  ,
'Cervical spondylosis '                      ,
'Paralysis (brain hemorrhage) '              ,
'Jaundice'                                  , 
'Malaria '                                   ,
'Chicken pox '                           ,
'Dengue'                                   ,
'Typhoid' ,
'Impetigo'])

graph=pydotplus.graph_from_dot_data(dot_data.getvalue())

Image(graph.create_png())

#GINI INDEX
from sklearn.tree import DecisionTreeClassifier                            
classifier =DecisionTreeClassifier(criterion="gini", random_state=100)   
classifier.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

"""## **Using Random Forest:**

## **Import Libraries**
"""

import pandas as pd
import numpy as np

"""## **Importing Dataset**"""

dataset = pd.read_csv('/content/Training.csv')

dataset.head()

"""## **Preparing Data For Training**"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

"""## **Feature Scaling**"""

# Feature Scaling
#it would be beneficial to scale our data 
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""## **Training the Algorithm**"""

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

"""## **Evaluating the Algorithm**"""

# MAE: Its an evaluation metrics
# MSE: Its an average squared deviation between the y-pred and y-test
# RMSE: Its used for evaluating the quality of predicitons.
from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

#from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#print(classification_report(y_test,y_pred))
#print(accuracy_score(y_test, y_pred))

"""## **Perform Prediction**"""

from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=20)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

# prediction on test set
y_pred=clf.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

"""## **NaiveBayes**"""

#NaiveBayes

"""# **GaussianNB**"""

#GaussianNB

import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

df=pd.read_csv("Training.csv", index_col=0)

df

df_c=df.astype('category')
df_c["prognosis"]=df_c["prognosis"].cat.codes
df_c.head

#iloc integer-location based indexing for selection by position.
X=df_c.iloc[:,:6].values
Y=df_c.iloc[:,6].values

#random state that you provide is used as a seed to the random number generator. 
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.5,random_state=15)
print(X_train.shape,y_train.shape)

model=GaussianNB()

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test,y_pred))

#

"""# **CategoricalNB**"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
#CategoricalNB suitable for classification with discrete features that are categorically distributed.

cnb = CategoricalNB()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape)
print(y_test.shape)

cnb.fit(X_train, y_train)
y_predict = cnb.predict(X_test)
print(y_predict)

print("Number of mislabeled points out of a total %d points : %d"%(X_test.shape[0], (y_test != y_predict).sum()))

from sklearn import metrics
print('Accucary:', metrics.accuracy_score(y_test, y_predict))
print('Confusion Matrix\n',metrics.confusion_matrix(y_test, y_predict))

"""# **MultinomialNB**"""

#MultinomialNB
#The multinomial Naive Bayes classifier is suitable for classification with discrete features

x = df.drop(['prognosis'],axis =1)
y = df['prognosis']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

#imported naive_baye algorithm
from sklearn.naive_bayes import MultinomialNB

#fitted the model
mnb = MultinomialNB()
mnb = mnb.fit(X_train, y_train)

score = mnb.score(X_test, y_test)
print("Accuracy Score: ",score)

"""# **GradientBoostingClassifier**"""

#GradientBoostingClassifier
#

from sklearn.ensemble import GradientBoostingClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

gbm_clf = GradientBoostingClassifier()
gbm_clf.fit(X_train, y_train)
score = gbm_clf.score(X_train, y_train)
print(score)

score2 = gbm_clf.score(X_test, y_test)
print(score2)

"""# **XGBClassifier**"""

#XGBClassifier
#XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable.

#XGBoost is used for supervised learning problems, where we use the training data (with multiple features) to predict a target variable

from xgboost import XGBClassifier

xgb_clf = XGBClassifier()
xgb_clf.fit(X_train, y_train)

score = xgb_clf.score(X_train, y_train)
print(score)

score1 = xgb_clf.score(X_test, y_test)
print(score1)