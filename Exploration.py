# -*- coding: utf-8 -*-
"""
Created on Mon May 27 08:24:00 2019

@author: Adam
"""
import pandas as pd
import numpy as np

#
from IPython.core.pylabtools import figsize
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(font_scale = 2)

#df1 = pd.read_csv(r'C:\Users\Adam\Desktop\Python\Master\df_Bets.csv')
#df1 = df1.drop(df1.columns[0], axis = 1)
#df2 = pd.read_csv(r'C:\Users\Adam\Desktop\Python\Master\df_Vpip.csv')
#df3 = pd.read_csv(r'C:\Users\Adam\Desktop\Python\Master\df_Agg.csv')
#
#dfs = [df1, df2, df3]
#from functools import reduce
#Data = reduce(lambda left, right: pd.merge(left, right, on = 'Seats', how = 'outer'), dfs)
#
#Data = Data.rename(columns ={'Seats':'Nickname', 'Hand_ID': 'Hands'})
#Data.to_csv(r'C:\Users\Adam\Desktop\Python\Master\Data17_18.csv', index = False)

Data = pd.read_csv(r'C:\Users\AdamPer\Desktop\Python\Master\Data17_18.csv')
Data.info()#informations about dataset
Data['Nickname'].describe()#calcualted statistics for columns



Data = Data.replace({np.NaN: 0})# nan is actually zero due merge uneven dataframes

#calculate more features. Winrate is divided by 0.5 becuase BB is 0.5
Data['Winrate'] = (Data['Winnings']/(Data['Hands']/100))/0.5
Data['Pfr/Vpip'] = Data['Pfr%']/Data['Vpip%']
Data['Vpip_Pfr_diff'] = Data['Vpip%'] - Data['Pfr%']



# =============================================================================
# Eksploracja
# =============================================================================
plt.hist(Data['Winrate'], bins = 10)
plt.xlim((-200, 200))
Data = Data[Data['Nickname'] != '0']#delete row for nickname 0

Data = Data.drop('Winnings', axis = 1)#drop winnings columns

Data = Data[Data['Hands'] > 1000]#choose players that played at least 1000 hands

sns.boxplot(x = Data['Winrate'])

#deleting outliers by quartile method

first_quartile = Data['Winrate'].describe()['25%']
third_quartile = Data['Winrate'].describe()['75%']

iqr = third_quartile - first_quartile

Data = Data[(Data['Winrate'] > (first_quartile - 3 * iqr)) &
            (Data['Winrate'] < (third_quartile + 3 * iqr))]



#creating badges
c1 = (Data['Hands'] > 30) & (Data['Vpip%'] >= 60.0)
c2 = (Data['Hands'] > 30) & (Data['Vpip%'] < 60.0) & (Data['Vpip%'] > 40.0)
c3 = (Data['Hands'] > 30) & (Data['Vpip%'] <= 33.0) & (Data['Vpip%'] > 21.0) & (Data['Pfr%'] > 15.0) & (Data['Pfr%'] <= 28.0)
c4 = (Data['Hands'] > 30) & (Data['Vpip%'] <= 33.0) & (Data['Vpip%'] > 21.0) & (Data['Pfr%'] <= 15.0)
c5 = (Data['Hands'] > 30) & (Data['Vpip%'] <= 21.0) & (Data['Vpip%'] > 17.0) & (Data['Pfr%'] > 13.0)
c6 = (Data['Hands'] > 30) & (Data['Vpip%'] <= 17.0)
c7 = (Data['Hands'] > 30) & (Data['Vpip%'] <= 40.0) & (Data['Vpip%'] > 33.0) & (Data['Pfr%'] <= 15.0)
c8 = (Data['Hands'] > 30) & (Data['Vpip%'] <= 40.0) & (Data['Vpip%'] > 33.0) & (Data['Pfr%'] > 15.0)
c9 = (Data['Hands'] > 30) & (Data['Vpip%'] <= 21.0) & (Data['Vpip%'] > 17.0) & (Data['Pfr%'] <= 13.0)

Data['Badge'] = np.select([c1, c2, c3, c4, c5, c6, c7, c8, c9], ['Wieloryb', 'Ryba', 'Regularny', 'Dokładacz', 'Skała', 'Nit', 'Dokładacz', 'Luźny', 'Nit'], np.nan)

#df3 = Data[['Vpip%', 'Pfr%', 'Agg', 'Hands', 'Badge']]

Data.to_csv(r'C:\Users\Adam\Desktop\Python\Master\regresja\Data1000.csv', index = False)



#raw histograms of some data
figsize(8, 8)
plt.style.use('fivethirtyeight')

plt.hist(Data['Winrate'], bins = 50)
plt.ylabel('Ilosc graczy')
plt.xlabel('Winrate')

plt.hist(Data['Vpip%'], bins = 20)
plt.ylabel('Ilosc graczy')
plt.xlabel('Charytatywne dolozenie do puli [%]')

plt.hist(Data['Pfr%'], bins = 20)
plt.ylabel('Ilosc graczy')
plt.xlabel('Przebicie przed zobaczeniem flopa [%]')

plt.hist(Data['WTSD_WSF%'], bins = 20)
plt.ylabel('Ilosc graczy')
plt.xlabel('Procent czasu, gdy gracz pokazuje karty')

plt.hist(Data['WWSF%'], bins = 20)
plt.ylabel('Ilosc graczy')
plt.xlabel('Procent czasu, gdy gracz wygrywa jesli zobaczyl flop')

plt.hist(Data['WMSD_WSF%'], bins = 20)
plt.ylabel('Ilosc graczy')
plt.xlabel('Procent czasu, gdy gracz wygrywa po okazaniu kart')


#Winrate graph after remove outliers
plt.hist(Data['Winrate'], bins = 50)
plt.ylabel('Ilosc graczy')
plt.xlabel('Winrate')


#visualize that players statistics have influance on winrate
badges = Data.dropna(subset = ['Winrate'])#delete Winrate with null winrate
badges = badges['Badge'].value_counts()#calculates values of badges
badges = list(badges[badges.values > 10].index)#Choose only badges with values more than 10


# Graph showing that different style of playing poker have infulance on Winnigs

figsize(12, 10)

for badge in badges:
    subset = Data[Data['Badge'] == badge]
    
    sns.kdeplot(subset['Winrate'].dropna(), label = badge)
    
plt.xlabel('Winrate', size = 20); plt.ylabel('Density', size = 20)
plt.title('Density Plot of Winrate by Badge', size = 28)


Data[Data['Badge'] == 'Regularny']['Winrate'].describe()

# Correlations counted and sort values
correlations_data = Data.corr()['Winrate'].sort_values()

#columns for correlation higher than 0.25
corr_cols = list(correlations_data[abs(correlations_data.values) > 0.25].index)

#choose numeric type columns 
numeric_subset = Data.select_dtypes('number')[corr_cols]

#creating log and sqrt features but correlation isnt better so i skipped this


#for col in numeric_subset:
#    if col == 'Winrate':
#        next
#    else:
#        numeric_subset['sqrt' + col] = np.sqrt(numeric_subset[col])
#        numeric_subset['log' + col] = np.sqrt(numeric_subset[col])
# zmienne po przeksztalceniam maja mniejsza korelacja

#choose categoricla data

categorical_subset = Data['Badge']

categorical_subset = pd.get_dummies(categorical_subset)#creating dummies var

features = pd.concat([numeric_subset, categorical_subset], axis = 1)

features = features.dropna(subset = ['Winrate'])#delete rows with nan winrate

#korelacja dla wszystkich zmiennych

correlations = features.corr()['Winrate'].dropna().sort_values()

corr_cols = list(correlations[abs(correlations.values) > 0.25].index)


#graph 
figsize(16, 14)
features['Badges'] = Data.dropna(subset = ['Winrate'])['Badge']

features = features[features['Badges'].isin(badges)]

sns.lmplot('Vpip%', 'Winrate',
           hue = 'Badges', data = features,
           scatter_kws= {'alpha': 0.8, 's': 10}, fit_reg= False,
           height = 8, aspect= 1.2)

features = features[corr_cols]

#pairs plot of Winrate


plot_data = features[['Vpip%', 'Winrate', 'WMSD_WSF%', 'Pfr/Vpip']]

plot_data = plot_data.dropna()

def corr_func(x, y, **kwargs):
    r = np.corrcoef(x, y)[0][1]
    ax = plt.gca()
    ax.annotate("r = {:.2f}".format(r),
                xy = (.2, .8), xycoords = ax.transAxes,
                size = 20)

grid = sns.PairGrid(data = plot_data, height = 3)

# Upper is a scatter plot
grid.map_upper(plt.scatter, color = 'red', alpha = 0.6)

# Diagonal is a histogram
grid.map_diag(plt.hist, color = 'red', edgecolor = 'black')

# Bottom is correlation and density plot
grid.map_lower(corr_func);
grid.map_lower(sns.kdeplot, cmap = plt.cm.Reds)

# Title for entire plot
plt.suptitle('Pairs Plot of Energy Data', size = 36, y = 1.02);



## Copy the original data
#features = Data.copy()
#
## Select the numeric columns
#numeric_subset = Data.select_dtypes('number')
#
## Select the categorical columns
#categorical_subset = Data['Badge']
#
## One hot encode
#categorical_subset = pd.get_dummies(categorical_subset)
#
## Join the two dataframes using concat
## Make sure to use axis = 1 to perform a column bind
#features = pd.concat([numeric_subset, categorical_subset], axis = 1)
#
#features.shape


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
    y = x['Winrate']#przypisuje kolumne winrate do zmiennej y
    x = x.drop(columns = ['Winrate'])#wyrzuca winrate, niechcemy badaac kolinearnosc ze zmienna objasniania.
    
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
    x['Winrate'] = y
               
    return x



# Remove the collinear features above a specified correlation coefficient
features = remove_collinear_features(features, 0.6)


# Remove any columns with all na values
features  = features.dropna(axis=1, how = 'all')
features.shape



# Separate out the features and targets
features = features.drop(columns='Winrate')
Data['Winner'] = np.where(Data['Winrate'] > 0, 1, 0)
targets = Data['Winner']


features.to_csv(r'C:\Users\Adam\Desktop\Python\Master\features.csv', index = False)
targets.to_csv(r'C:\Users\Adam\Desktop\Python\Master\targets.csv', index = False, header = True)
