# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:36:07 2019

@author: AdamPer
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Data = pd.read_csv(r'C:\Users\AdamPer\Desktop\Python\Master\regresja\Data1000.csv')
Data = Data.drop(columns = ['Hands'])#usuwamy ilosc rak

x = Data.corr()

sns.lmplot(data=Data, x ='Vpip%', y = 'Winrate')

Data.dropna(inplace = True)
Data.head()
Data.info()

#kategoryzacja zmiennej
Data['Score'] = np.where(Data.loc[:,'Winrate'] > 0, 1, 0)# 1 wygrywa, 0 przegrywa
Data.drop(columns = 'Winrate', inplace = True)


Data.groupby('Score').mean()['Vpip%']
plt.hist(np.log(Data['Vpip%']),bins = 20)

#przygotowanie danych do modelowania
features = Data.select_dtypes('number')
features = features.drop(columns = ['Agg', 'Agg_Flop', 'Agg_Turn', 'Agg_River'])
#categorical_subset = Data['Badge']
#categorical_subset = pd.get_dummies(categorical_subset)#creating dummies var
#features = pd.concat([numeric_subset, categorical_subset], axis = 1)



#Policzenie ilosci graczy wygrywajacych i przegrywajacych
Data['Score'].value_counts()
#wykres
sns.countplot(x = 'Score', data = Data, palette= 'hls')#kiedy uznajemy, ze klasy sa nie zbalansowane?
plt.show()
plt.savefig('count_plot')

#wskazanie procentowych roznic pomiedzy klasami
count_winner = len(Data[Data['Score'] == 1])
count_no_winner = len(Data[Data['Score'] == 0])

pct_winner = count_winner/(count_winner + count_no_winner)
print('Procent wygrywających graczy to:', round(pct_winner*100, 2))
pct_no_winner = count_no_winner/(count_winner + count_no_winner)
print('Procent przegrywających graczy to:', round(pct_no_winner*100, 2))

#wskazanie wygrywajacych/przegrywajacych w grupach
pd.crosstab(Data['Badge'], Data['Score']).plot(kind = 'bar')#stworzenie tabeli kontygencji zmiennej Badge ze wskazaniem liczebnosci wygrywajacych/przegrywajacych
plt.title('Liczebnosc graczy w zaleznosc od wynikow')
plt.xlabel('Badge')
plt.ylabel('Liczebnosc graczy')


# =============================================================================
# usuniecie wspolliniowosci
# =============================================================================
def remove_collinear_features(x, threshold):
    '''
    Objective:
        Remove collinear features in a dataframe with a correlation coefficient
        greater than the threshold. Removing collinear features can help a model
        to generalize and improves the interpretability of the model.
        
    Inputs: 
        threshold: any features with correlations greater than this value are removed
    
    Output: 
        dataframe that contains only the non-highly-collinear features
    '''
    
    # Dont want to remove correlations between Energy Star Score
    y = x['Score']#przypisuje kolumne winrate do zmiennej y
    x = x.drop(columns = ['Score'])#wyrzuca winrate, niechcemy badaac kolinearnosc ze zmienna objasniania.
    
    # Calculate the correlation matrix
    corr_matrix = x.corr()
    iters = range(len(corr_matrix.columns) - 1)
    drop_cols = []

    # Iterate through the correlation matrix and compare correlations
    for i in iters:
        for j in range(i):
            item = corr_matrix.iloc[j:(j+1), (i+1):(i+2)]
            col = item.columns
            val = abs(item.values)
            
            # If correlation exceeds the threshold
            if val >= threshold:
                # Print the correlated features and the correlation value
                # print(col.values[0], "|", row.values[0], "|", round(val[0][0], 2))
                drop_cols.append(col.values[0])

    # Drop one of each pair of correlated columns
    drops = set(drop_cols)
    x = x.drop(columns = drops)
#    x = x.drop(columns = ['Weather Normalized Site EUI (kBtu/ft²)', 
#                          'Water Use (All Water Sources) (kgal)',
#                          'log_Water Use (All Water Sources) (kgal)',
#                          'Largest Property Use Type - Gross Floor Area (ft²)'])
    
    # Add the score back in to the data
    x['Score'] = y
               
    return x



# Remove the collinear features above a specified correlation coefficient
features = remove_collinear_features(features, 0.6)


X = features.drop(columns = 'Score')
y = features['Score']



# =============================================================================
# balansowanie proby
# =============================================================================

#mozna dodac balansowanie proby z wykorzystaniem SMOTE - oversampling
from imblearn.over_sampling import SMOTE
os = SMOTE(random_state=0)

from sklearn.model_selection import train_test_split
X_train_all, X_test, y_train_all, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

columns = X_train_all.columns


os_X, os_y = os.fit_sample(X_train_all, y_train_all)
os_X = pd.DataFrame(data = os_X, columns = columns)#stworzenie df z nazwami kolumn
os_y= pd.DataFrame(data = os_y, columns = ['y'])

print("Długosc przeprobkowanych danych to: ",len(os_X))
print("Ilosc graczy przegrwajacych w przeprobkowanych danych to: ",len(os_y[os_y['y']==0]))
print("Ilosc graczy wygrywajacych w przeprobkowanych danych to: ",len(os_y[os_y['y']==1]))
print("Proporcja danych przegrywających graczy to ",len(os_y[os_y['y']==0])/len(os_X))
print("Proporcja danych wygrywających graczy to ",len(os_y[os_y['y']==1])/len(os_X))

#tylko treningowe w srodku
X = os_X
y = os_y['y']


# =============================================================================
# model dla wszystkich zmiennych po zbalansowaniu proby
# =============================================================================
#implementowanie modelu
import statsmodels.api as sm
logit_model = sm.Logit(y, X)
result=logit_model.fit()
print(result.summary2())

#ocena modelu na podstawie zbioru testowego i treningowego
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()

# fit the model with data
logreg.fit(X, y)

#Przwidywane y na podstawie zbbudowanego modelu oraz nie uzytych do budowy X
y_pred_all = logreg.predict(X_test)


# import the metrics class
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred_all)
cnf_matrix#276 i 117 to nie popprawne predykcje


class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Macierz klasyfikacji', y=1.1)
plt.ylabel('Wartosci rzeczywiste')
plt.xlabel('Wartosci przewidywane')

#Ocena modelu
print("Accuracy_os:",metrics.accuracy_score(y_test, y_pred_all))
print("Precision_os:",metrics.precision_score(y_test, y_pred_all))
print("Recall_os:",metrics.recall_score(y_test, y_pred_all))




from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Regresja logistyczna (AUC = %0.5f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('1 - Specyficznosc')
plt.ylabel('Czulosc')
plt.title('Krzywa ROC')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()

# =============================================================================
# RFE - selekcja zmiennych
# =============================================================================
from sklearn.feature_selection import RFE

logreg = LogisticRegression()

rfe = RFE(logreg)
rfe = rfe.fit(X, y)
print(rfe.support_)
print(rfe.ranking_)
print("Optimal number of features: %d" % rfe.n_features_)
print('Selected features: %s' % list(X.columns[rfe.support_]))

sel_features = ['FlopBetLower40%', 'FlopBet40_60%', 'FlopBet60_85%', 'FlopBetMore85%', 'Won%', 'WWSF%', 'WWSR%']
X_rfe = X[sel_features]# final features`
y_rfe = y

#implementowanie modelu
import statsmodels.api as sm
logit_model = sm.Logit(y_rfe, X_rfe)
result_rem=logit_model.fit()# jest konwergencja
print(result_rem.summary2())

#Ocena modelu
# instantiate the model (using the default parameters)
logreg = LogisticRegression()
# fit the model with data
logreg.fit(X_rfe, y_rfe)
#
X_test_rfe = X_test[sel_features]
y_pred_rfe = logreg.predict(X_test_rfe)


# metrics class
cnf_matrix = metrics.confusion_matrix(y_test, y_pred_rfe)
cnf_matrix#284 i 124to nie popprawne predykcje




class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

#ocena modelu bez selekcji zmiennych
#dokladnosc predykcji.
print("Accuracy_rfe_os:",metrics.accuracy_score(y_test, y_pred_rfe))
#precyzja czyli poprawna klasyfikacja. TP/(TP+FP)
print("Precision_rfe_os:",metrics.precision_score(y_test, y_pred_rfe))
#czulosc - zdolnosc klasyfikatora do znalezienia wszystkich pozytywnych predykcji TP/(TP+FN)
print("Recall_rfe_os:",metrics.recall_score(y_test, y_pred_rfe))

#krzywa ROC
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test_rfe))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test_rfe)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Regresja logistyczna (AUC = %0.5f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('1 - Specyficznosc')
plt.ylabel('Czulosc')
plt.title('Krzywa ROC')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()
# =============================================================================
# RFECV - selekcja zmiennych
# =============================================================================
from sklearn.feature_selection import RFECV

rfecv = RFECV(estimator = LogisticRegression(), step=1, cv=10, scoring='accuracy')
rfecv.fit(X, y)

print("Optimal number of features: %d" % rfecv.n_features_)
print('Selected features: %s' % list(X.columns[rfecv.support_]))
sel_features_cv_os = ['FlopBetLower40%', 'FlopBet40_60%', 'FlopBet60_85%', 'FlopBetMore85%', 'Won%', 'Vpip%', 'VpipBB%', 'Pfr%', 'PfrBB%', 
                      'WTSD_WSF%', 'WTSD_WST%', 'WWSF%', 'WWST%', 'WWSR%']
# Plot number of features VS. cross-validation scores
plt.figure(figsize=(10,6))
plt.xlabel("Ilosc wybranych zamiennych")
plt.ylabel("Ocena walidacji krzyżowej (liczba prawidłowych klasyfikacji)")
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.show()



X_rfecv = X[sel_features_cv_os]
y_rfecv = y

#implementowanie modelu
import statsmodels.api as sm
logit_model = sm.Logit(y_rfecv, X_rfecv)
result_rem=logit_model.fit()
print(result_rem.summary2())

#Ocena modelu
# instantiate the model (using the default parameters)
logreg = LogisticRegression()
# fit the model with data
logreg.fit(X_rfecv, y_rfecv)
#
X_test_rfecv = X_test[sel_features_cv_os]
y_pred_rfecv = logreg.predict(X_test)


# metrics class
cnf_matrix = metrics.confusion_matrix(y_test, y_pred_rfecv)
cnf_matrix#267 i 126 to nie popprawne predykcje




class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

#ocena modelu bez selekcji zmiennych
#dokladnosc predykcji.
print("Accuracy_rfecv_os:",metrics.accuracy_score(y_test, y_pred_rfecv))
#precyzja czyli poprawna klasyfikacja. TP/(TP+FP)
print("Precision_rfecv_os:",metrics.precision_score(y_test, y_pred_rfecv))
#czulosc - zdolnosc klasyfikatora do znalezienia wszystkich pozytywnych predykcji TP/(TP+FN)
print("Recall_rfecv_os:",metrics.recall_score(y_test, y_pred_rfecv))

#krzywa ROC
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test_rfecv))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test_rfecv)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.5f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()
