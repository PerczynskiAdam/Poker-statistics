# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:25:24 2019

@author: AdamPer
"""

import pandas as pd
import numpy as np

#dtypes = {'Soft': np.object,
#          'Hand_ID': np.int64,
#          'Table_Name': np.object,
#          'SmallBlind': np.float64,
#          'BigBlind': np.float64,
#          'Currency': np.object,
#          'Day': np.object,
#          'Hour': np.object,
#          'Seat_1': np.object, 'Seat_2': np.object, 'Seat_3': np.object, 'Seat_4': np.object, 'Seat_5': np.object, 'Seat_6': np.object,
#          'Stack_1': np.float64, 'Stack_2': np.float64, 'Stack_3': np.float64, 'Stack_4': np.float64, 'Stack_5': np.float64, 'Stack_6': np.float64,
#'Raise_Pre_S1': np.object, 'Raise_Pre_S2': np.object, 'Raise_Pre_S3': np.object, 'Raise_Pre_S4': np.object, 'Raise_Pre_S5': np.object, 'Raise_Pre_S6': np.object,
#'Call_Pre_S1': np.object, 'Call_Pre_S2': np.object, 'Call_Pre_S3': np.object, 'Call_Pre_S4': np.object, 'Call_Pre_S5': np.object, 'Call_Pre_S6': np.object,
#'Flop_Bet_S1': np.float64, 'Flop_Bet_S2': np.float64, 'Flop_Bet_S3': np.float64, 'Flop_Bet_S4': np.float64, 'Flop_Bet_S5': np.float64, 'Flop_Bet_S6': np.float64,
#'Flop_Raise_S1': np.object, 'Flop_Raise_S2': np.object, 'Flop_Raise_S3': np.object, 'Flop_Raise_S4': np.object, 'Flop_Raise_S5': np.object, 'Flop_Raise_S6': np.object,
#'Flop_Call_S1': np.object, 'Flop_Call_S2': np.object, 'Flop_Call_S3': np.object, 'Flop_Call_S4': np.object, 'Flop_Call_S5': np.object, 'Flop_Call_S6': np.object, 
#'Saw_Flop_S1': np.int64, 'Saw_Flop_S2': np.int64, 'Saw_Flop_S3': np.int64, 'Saw_Flop_S4': np.int64, 'Saw_Flop_S5': np.int64, 'Saw_Flop_S6': np.int64,
#'Turn_Bet_S1': np.float64, 'Turn_Bet_S2': np.float64, 'Turn_Bet_S3': np.float64, 'Turn_Bet_S4': np.float64, 'Turn_Bet_S5': np.float64, 'Turn_Bet_S6': np.float64,
#'Turn_Raise_S1': np.object, 'Turn_Raise_S2': np.object, 'Turn_Raise_S3': np.object, 'Turn_Raise_S4': np.object, 'Turn_Raise_S5': np.object, 'Turn_Raise_S6': np.object,
#'Turn_Call_S1': np.object, 'Turn_Call_S2': np.object, 'Turn_Call_S3': np.object, 'Turn_Call_S4': np.object, 'Turn_Call_S5': np.object, 'Turn_Call_S6': np.float64,
#'Saw_Turn_S1': np.int64, 'Saw_Turn_S2': np.int64, 'Saw_Turn_S3': np.int64, 'Saw_Turn_S4': np.int64, 'Saw_Turn_S5': np.int64, 'Saw_Turn_S6': np.int64,
#'River_Bet_S1': np.float64,'River_Bet_S2': np.float64,'River_Bet_S3': np.float64,'River_Bet_S4': np.float64,'River_Bet_S5': np.float64,'River_Bet_S6': np.float64,
#'River_Raise_S1': np.object, 'River_Raise_S2': np.object,'River_Raise_S3': np.object, 'River_Raise_S4': np.object, 'River_Raise_S5': np.object, 'River_Raise_S6': np.object,
#'River_Call_S1': np.object, 'River_Call_S2': np.object, 'River_Call_S3': np.object, 'River_Call_S4': np.object, 'River_Call_S5': np.object, 'River_Call_S6': np.object,
#'Saw_River_S1': np.int64,'Saw_River_S2': np.int64,'Saw_River_S3': np.int64,'Saw_River_S4': np.int64,'Saw_River_S5': np.int64, 'Saw_River_S6': np.int64,
#'S1_shows?': np.int64, 'S2_shows?': np.int64, 'S3_shows?': np.int64, 'S4_shows?': np.int64, 'S5_shows?': np.int64, 'S6_shows?': np.int64,
#'Winner?_S1': np.int64, 'Winner?_S2': np.int64, 'Winner?_S3': np.int64, 'Winner?_S4': np.int64, 'Winner?_S5': np.int64, 'Winner?_S6': np.int64,
#'W/L_amount_S1': np.float64, 'W/L_amount_S2': np.float64, 'W/L_amount_S3': np.float64, 'W/L_amount_S4': np.float64, 'W/L_amount_S5': np.float64, 'W/L_amount_S6': np.float64,
#'Pot': np.float64,
#'Rake': np.float64}

df = pd.read_csv(r'C:\Users\Adam\Desktop\Python\Master\2017_2018_6plr.csv', encoding= "utf_8_sig",
#                 parse_dates = [['Hour', 'Day']],
                 usecols = ['Hand_ID', 
       'Seat_1','Seat_2','Seat_3', 'Seat_4', 'Seat_5', 'Seat_6',
       'Flop_Bet_S1', 'Flop_Bet_S2', 'Flop_Bet_S3', 'Flop_Bet_S4', 'Flop_Bet_S5', 'Flop_Bet_S6',
       'Flop_Raise_S1', 'Flop_Raise_S2', 'Flop_Raise_S3', 'Flop_Raise_S4', 'Flop_Raise_S5', 'Flop_Raise_S6',
       'Flop_Call_S1', 'Flop_Call_S2', 'Flop_Call_S3', 'Flop_Call_S4', 'Flop_Call_S5', 'Flop_Call_S6',
       'Turn_Bet_S1', 'Turn_Bet_S2', 'Turn_Bet_S3', 'Turn_Bet_S4', 'Turn_Bet_S5', 'Turn_Bet_S6',
       'Turn_Raise_S1', 'Turn_Raise_S2', 'Turn_Raise_S3', 'Turn_Raise_S4', 'Turn_Raise_S5', 'Turn_Raise_S6',
       'Turn_Call_S1', 'Turn_Call_S2', 'Turn_Call_S3', 'Turn_Call_S4', 'Turn_Call_S5', 'Turn_Call_S6',
       'River_Bet_S1', 'River_Bet_S2', 'River_Bet_S3', 'River_Bet_S4', 'River_Bet_S5', 'River_Bet_S6',
       'River_Raise_S1', 'River_Raise_S2', 'River_Raise_S3', 'River_Raise_S4', 'River_Raise_S5', 'River_Raise_S6',
       'River_Call_S1', 'River_Call_S2', 'River_Call_S3', 'River_Call_S4', 'River_Call_S5', 'River_Call_S6'])


df = df.drop_duplicates()#dropuje handy, ktore sie powtorzyly


#zrobic podsumowanie rozdan z podzialem na miesiace
#df.groupby(df['Hour_Day'].dt.strftime('%B')).Hand_ID.value_counts()
##podsumowanie sredniej puli z podzialem na miesiace
#df.groupby(df['Hour_Day'].dt.strftime('%B')).Pot.mean()
##sredni rake zebrany z podzialem na miesiace
#df.groupby(df['Hour_Day'].dt.strftime('%B')).Rake.mean()
#procentowy rake z podzialem na miesiace
#procentowy rake z podzialem na wysokosci puli
# =============================================================================
### ustawienie vertykalne zbiorow. Kazde 6 wierszy to jedna reka.
#df_Seats = pd.melt(df, id_vars = ['Hand_ID','Soft','Table_Name', 'SmallBlind', 'BigBlind', 'Currency', 'Day', 'Hour', 'Pot', 'Rake'],
#                     value_vars = ['Seat_1', 'Seat_2', 'Seat_3', 'Seat_4', 'Seat_5', 'Seat_6'],
#                     var_name = 'Seats_var', value_name = 'Seats')
# 
#df_Seats = df_Seats.drop('Seats_var', 1)

df_Seats = pd.melt(df, id_vars = ['Hand_ID'],#wywal Day, hour, pot i rake, dodaj date
                     value_vars = ['Seat_1', 'Seat_2', 'Seat_3', 'Seat_4', 'Seat_5', 'Seat_6'],
                     var_name = 'Seats_var', value_name = 'Seats')
 
df_Seats = df_Seats.drop('Seats_var', 1)

#df_Stacks = pd.melt(df,
#                     value_vars = ['Stack_1', 'Stack_2', 'Stack_3', 'Stack_4', 'Stack_5', 'Stack_6'],
#                     var_name = 'Stacks_var', value_name = 'Stacks')
# 
#df_Stacks = df_Stacks.drop('Stacks_var', 1)

#df_Pos = pd.melt(df,
#                     value_vars = ['S1_pos', 'S2_pos', 'S3_pos', 'S4_pos', 'S5_pos', 'S6_pos'],
#                     var_name = 'var', value_name = 'Position')
# 
#df_Pos = df_Pos.drop('var', 1)

 
#df_RaisePRE = pd.melt(df,
#                     value_vars = ['Raise_Pre_S1', 'Raise_Pre_S2', 'Raise_Pre_S3', 'Raise_Pre_S4', 'Raise_Pre_S5','Raise_Pre_S6'],
#                     var_name = 'var', value_name = 'Raise_Pre')
# 
#df_RaisePRE = df_RaisePRE.drop('var', 1)
# 
#df_CallPRE = pd.melt(df, 
#                     value_vars = ['Call_Pre_S1', 'Call_Pre_S2', 'Call_Pre_S3', 'Call_Pre_S4', 'Call_Pre_S5', 'Call_Pre_S6'],
#                     var_name = 'var', value_name = 'Call_Pre')
# 
#df_CallPRE = df_CallPRE.drop('var', 1)
# 
 
df_FlopBet = pd.melt(df,
                     value_vars = ['Flop_Bet_S1', 'Flop_Bet_S2', 'Flop_Bet_S3', 'Flop_Bet_S4', 'Flop_Bet_S5', 'Flop_Bet_S6'],
                     var_name = 'var', value_name = 'Flop_Bet')
 
df_FlopBet  = df_FlopBet.drop('var', 1)
 
df_FlopRaise = pd.melt(df,
                     value_vars = ['Flop_Raise_S1', 'Flop_Raise_S2', 'Flop_Raise_S3', 'Flop_Raise_S4', 'Flop_Raise_S5', 'Flop_Raise_S6'],
                     var_name = 'var', value_name = 'Flop_Raise')
 
df_FlopRaise  = df_FlopRaise.drop('var', 1)
 
 
df_FlopCall = pd.melt(df, 
                     value_vars = ['Flop_Call_S1', 'Flop_Call_S2', 'Flop_Call_S3', 'Flop_Call_S4', 'Flop_Call_S5', 'Flop_Call_S6'],
                     var_name = 'var', value_name = 'Flop_Call')
 
df_FlopCall  = df_FlopCall.drop('var', 1)

#df_SawFLop = pd.melt(df,
#                     value_vars = ['Saw_Flop_S1', 'Saw_Flop_S2', 'Saw_Flop_S3', 'Saw_Flop_S4', 'Saw_Flop_S5', 'Saw_Flop_S6'],
#                     var_name = 'var', value_name = 'Saw_Flop')
#
#df_SawFLop  = df_SawFLop.drop('var', 1)
 
 
df_TurnBet = pd.melt(df, 
                     value_vars = ['Turn_Bet_S1', 'Turn_Bet_S2', 'Turn_Bet_S3','Turn_Bet_S4', 'Turn_Bet_S5', 'Turn_Bet_S6'],
                     var_name = 'var', value_name = 'Turn_Bet')
 
df_TurnBet  = df_TurnBet.drop('var', 1)
 
 
df_TurnRaise = pd.melt(df, 
                     value_vars = ['Turn_Raise_S1', 'Turn_Raise_S2', 'Turn_Raise_S3', 'Turn_Raise_S4', 'Turn_Raise_S5', 'Turn_Raise_S6'],
                     var_name = 'var', value_name = 'Turn_Raise')
 
df_TurnRaise  = df_TurnRaise.drop('var', 1)
 
 
df_TurnCall = pd.melt(df, 
                     value_vars = ['Turn_Call_S1', 'Turn_Call_S2', 'Turn_Call_S3', 'Turn_Call_S4', 'Turn_Call_S5', 'Turn_Call_S6'],
                     var_name = 'var', value_name = 'Turn_Call')
 
df_TurnCall  = df_TurnCall.drop('var', 1)

#df_SawTurn = pd.melt(df,
#                     value_vars = ['Saw_Turn_S1', 'Saw_Turn_S2', 'Saw_Turn_S3', 'Saw_Turn_S4', 'Saw_Turn_S5', 'Saw_Turn_S6'],
#                     var_name = 'var', value_name = 'Saw_Turn')
#
#df_SawTurn  = df_SawTurn.drop('var', 1)
 
df_RiverBet = pd.melt(df, 
                     value_vars = ['River_Bet_S1', 'River_Bet_S2', 'River_Bet_S3', 'River_Bet_S4', 'River_Bet_S5', 'River_Bet_S6'],
                     var_name = 'var', value_name = 'River_Bet')
 
df_RiverBet  = df_RiverBet.drop('var', 1)
 
df_RiverRaise = pd.melt(df, 
                     value_vars = ['River_Raise_S1', 'River_Raise_S2', 'River_Raise_S3', 'River_Raise_S4', 'River_Raise_S5', 'River_Raise_S6'],
                     var_name = 'var', value_name = 'River_Raise')
 
df_RiverRaise  = df_RiverRaise.drop('var', 1)
 
df_RiverCall = pd.melt(df, 
                     value_vars = ['River_Call_S1', 'River_Call_S2', 'River_Call_S3', 'River_Call_S4', 'River_Call_S5', 'River_Call_S6'],
                     var_name = 'var', value_name = 'River_Call')
 
df_RiverCall  = df_RiverCall.drop('var', 1)
 
#df_SawRiver = pd.melt(df,
#                     value_vars = ['Saw_River_S1', 'Saw_River_S2', 'Saw_River_S3', 'Saw_River_S4', 'Saw_River_S5', 'Saw_River_S6'],
#                     var_name = 'var', value_name = 'Saw_River')
#
#df_SawRiver  = df_SawRiver.drop('var', 1)
 
#df_Winner = pd.melt(df,
#                     value_vars = ['Winner?_S1', 'Winner?_S2', 'Winner?_S3', 'Winner?_S4', 'Winner?_S5', 'Winner?_S6'],
#                     var_name = 'var', value_name = 'Winner?')
# 
#df_Winner  = df_Winner.drop('var', 1)
#
#df_SD = pd.melt(df,
#                     value_vars = ['S1_shows?', 'S2_shows?', 'S3_shows?', 'S4_shows?', 'S5_shows?', 'S6_shows?'],
#                     var_name = 'var', value_name = 'Showdown?')
#
#df_SD = df_SD.drop('var', 1)


#df_Winnings = pd.melt(df, 
#                      value_vars = ['W/L_amount_S1', 'W/L_amount_S2', 'W/L_amount_S3', 'W/L_amount_S4', 'W/L_amount_S5', 'W/L_amount_S6'],
#                      var_name ='var', value_name = 'Winnings')
#
#df_Winnings = df_Winnings.drop('var', 1)
# =============================================================================
## polaczenie przestawionych zbiorow.
df2 = pd.concat([df_Seats, df_FlopBet, df_FlopCall, df_FlopRaise, df_TurnBet, df_TurnCall, df_TurnRaise, df_RiverBet, df_RiverCall, df_RiverRaise], axis = 1)
    
#df2 = pd.concat([df_Seats, df_Stacks, df_CallPRE, df_RaisePRE, df_SawFLop, df_SawTurn, df_SawRiver, df_Winnings, df_SD, df_Winner], axis = 1)

#df2 = df2.drop_duplicates()#duplikaty dla zer w nazwie. Nie robimy tego. Tego nie bedzie jak wybierzemy tylko pelne stoly 6-max


# =============================================================================
# wyliczanie statystyk
# =============================================================================

##Policzenie ile razy ktos raisowa, callowal
#import ast
#i=0
#for i in range(len(df2)):
#    df2.at[i, 'Flop_Raise_Len'] = len(ast.literal_eval(df2['Flop_Raise'][i]))
#    df2.at[i, 'Flop_Call_Len'] = len(ast.literal_eval(df2['Flop_Call'][i]))
#    df2.at[i, 'Turn_Raise_Len'] = len(ast.literal_eval(df2['Turn_Raise'][i]))
#    df2.at[i, 'Turn_Call_Len'] = len(ast.literal_eval(df2['Turn_Call'][i]))
#    df2.at[i, 'River_Raise_Len'] = len(ast.literal_eval(df2['River_Raise'][i]))
#    df2.at[i, 'River_Call_Len'] = len(ast.literal_eval(df2['River_Call'][i]))
#    i+=1
#
#df2 = pd.read_csv(r'C:\Users\Adam\Desktop\Python\Magisterka\semi_final2.csv',
#                  usecols = ['Hand_ID', 'Seats', 'Flop_Bet', 'Flop_Call', 'Flop_Raise', 'Turn_Bet',
#       'Turn_Call', 'Turn_Raise', 'River_Bet', 'River_Call', 'River_Raise',
#       'Flop_BetL40%', 'Flop_Bet40_60%', 'Flop_Bet60_70%', 'Flop_Bet70_85%',
#       'Flop_Bet85_110%', 'Flop_BetM110%', 'Turn_BetL40%', 'Turn_Bet40_60%',
#       'Turn_Bet60_70%', 'Turn_Bet70_85%', 'Turn_Bet85_110%', 'Turn_BetM110%',
#       'River_BetL40%', 'River_Bet40_60%', 'River_Bet60_70%',
#       'River_Bet70_85%', 'River_Bet85_110%', 'River_BetM110%',
#       'Flop_Raise_Len', 'Flop_Call_Len', 'Turn_Raise_Len', 'Turn_Call_Len',
#       'River_Raise_Len', 'River_Call_Len'])
#
#
##policzenie ile razy ktos betowal
#df2['Flop_Bet_Len'] = [0 if x == 0.0 else 1 for x in df2['Flop_Bet']]
#df2['Turn_Bet_Len'] = [0 if x == 0.0 else 1 for x in df2['Turn_Bet']]
#df2['River_Bet_Len'] = [0 if x == 0.0 else 1 for x in df2['River_Bet']]
#
##policzenie agresji ogolnej oraz flop, turn, river
#df2['Agg'] = (df2['Flop_Bet_Len'] + df2['Turn_Bet_Len'] + df2['River_Bet_Len'] + df2['Flop_Raise_Len'] + df2['Turn_Raise_Len'] +
#   df2['River_Raise_Len'])/(df2['Flop_Call_Len'] + df2['Turn_Call_Len'] + df2['River_Call_Len'])
#
#df2['Agg_Flop'] = (df2['Flop_Bet_Len'] + df2['Flop_Raise_Len'])/(df2['Flop_Call_Len'])
#df2['Agg_Turn'] = (df2['Turn_Bet_Len'] + df2['Turn_Raise_Len'])/(df2['Turn_Call_Len'])
#df2['Agg_River'] = (df2['River_Bet_Len'] + df2['River_Raise_Len'])/(df2['River_Call_Len'])


#policzenie statystyk
#df2['Vpip'] = np.where((df2['Call_Pre'] == '[]') & (df2['Raise_Pre'] == '[]'), 'No', 'Yes')# kazde dolozenie do puli. Poza bycia na BB
#
#df2['Pfr'] = ['No' if x == '[]' else 'Yes' for x in df2['Raise_Pre']]# wszystkie raise pre. Nawet po wczesniejszym callu.
#
#df2['WTSD'] = ['No' if x == 0 else 'Yes' for x in df2['Showdown?']] #Yes jesli pokazal karty
#
#df2['Won'] = ['No' if x == 0 else 'Yes' for x in df2['Winner?']]#Yes gdy wygral. Kazda wygrana, gdy widzial flop - filtrowane pozniej [WWSF], gdy widzial flop i SD (WMSD)

df2['Flop_BetL40%'] = np.where((df2['Flop_Bet'] > 0.0) & (df2['Flop_Bet'] <= 0.40), 'Yes', 'No')
df2['Flop_Bet40_60%'] = np.where((df2['Flop_Bet'] > 0.40) & (df2['Flop_Bet'] <= 0.60), 'Yes', 'No')
df2['Flop_Bet60_70%'] = np.where((df2['Flop_Bet'] > 0.60) & (df2['Flop_Bet'] <= 0.70), 'Yes', 'No')
df2['Flop_Bet70_85%'] = np.where((df2['Flop_Bet'] > 0.70) & (df2['Flop_Bet'] <= 0.85), 'Yes', 'No')
df2['Flop_Bet85_110%'] = np.where((df2['Flop_Bet'] > 0.85) & (df2['Flop_Bet'] <= 1.10), 'Yes', 'No')
df2['Flop_BetM110%'] = np.where(df2['Flop_Bet'] > 1.10, 'Yes', 'No')

df2['Turn_BetL40%'] = np.where((df2['Turn_Bet'] > 0.0) & (df2['Turn_Bet'] <= 0.40), 'Yes', 'No')
df2['Turn_Bet40_60%'] = np.where((df2['Turn_Bet'] > 0.40) & (df2['Turn_Bet'] <= 0.60), 'Yes', 'No')
df2['Turn_Bet60_70%'] = np.where((df2['Turn_Bet'] > 0.60) & (df2['Turn_Bet'] <= 0.70), 'Yes', 'No')
df2['Turn_Bet70_85%'] = np.where((df2['Turn_Bet'] > 0.70) & (df2['Turn_Bet'] <= 0.85), 'Yes', 'No')
df2['Turn_Bet85_110%'] = np.where((df2['Turn_Bet'] > 0.85) & (df2['Turn_Bet'] <= 1.10), 'Yes', 'No')
df2['Turn_BetM110%'] = np.where(df2['Turn_Bet'] > 1.10, 'Yes', 'No')

df2['River_BetL40%'] = np.where((df2['River_Bet'] > 0.0) & (df2['River_Bet'] <= 0.40), 'Yes', 'No')
df2['River_Bet40_60%'] = np.where((df2['River_Bet'] > 0.40) & (df2['River_Bet'] <= 0.60), 'Yes', 'No')
df2['River_Bet60_70%'] = np.where((df2['River_Bet'] > 0.60) & (df2['River_Bet'] <= 0.70), 'Yes', 'No')
df2['River_Bet70_85%'] = np.where((df2['River_Bet'] > 0.70) & (df2['River_Bet'] <= 0.85), 'Yes', 'No')
df2['River_Bet85_110%'] = np.where((df2['River_Bet'] > 0.85) & (df2['River_Bet'] <= 1.10), 'Yes', 'No')
df2['River_BetM110%'] = np.where(df2['River_Bet'] > 1.10, 'Yes', 'No')



# =============================================================================
# df2.groupby(['Seats']).Vpip.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='Vpip%') #level =0 oznacza kolumne pierwsza. 1= druga itd
# 
# df2.groupby(['Seats']).Pfr.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='Pfr%')
# 
# df2.groupby(['Seats']).WTSD.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='WTSD%')
# 
# df2.groupby(['Seats']).WWSF.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='WWSF%')
# 
# df2.groupby(['Seats']).WMSD.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='WMSD%')
# 
# =============================================================================
# =============================================================================
# dfVPIP = df2.groupby(['Seats', 'BigBlind']).Vpip.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).reset_index(level = 1).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index()
# dfPFR = df2.groupby(['Seats', 'BigBlind']).Pfr.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).reset_index(level = 1).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index()
# dfWTSD = df2[df2['Saw_Flop'] == 1].groupby(['Seats', 'BigBlind']).WTSD.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).reset_index(level = 1).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index()
# dfWWSF = df2[df2['Saw_Flop'] == 1].groupby(['Seats', 'BigBlind']).WWSF.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).reset_index(level = 1).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index()
# dfWMSD = df2[df2['Saw_Flop'] == 1].groupby(['Seats', 'BigBlind']).WMSD.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).reset_index(level = 1).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index()
# dfWINNINGS = df2.groupby(['Seats', 'BigBlind']).Winnings.sum().reset_index()
# dfHANDS = df2.groupby(['Seats', 'BigBlind']).Hand_ID.count().reset_index()#ok
# =============================================================================
## % of win
#dfWon = df2.groupby('Seats').Won.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='Won%')

# =============================================================================
#Sizingi
df2_Flop_BetL40 = df2[df2['Flop_Bet'] > 0.0].groupby('Seats')['Flop_BetL40%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='FlopBetLower40%')
df2_Flop_Bet40_60 = df2[df2['Flop_Bet'] > 0.0].groupby('Seats')['Flop_Bet40_60%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='FlopBet40_60%')
df2_Flop_Bet60_70 = df2[df2['Flop_Bet'] > 0.0].groupby('Seats')['Flop_Bet60_70%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='FlopBet60_70%')
df2_Flop_Bet70_85 = df2[df2['Flop_Bet'] > 0.0].groupby('Seats')['Flop_Bet70_85%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='FlopBet70_85%')
df2_Flop_Bet85_110 = df2[df2['Flop_Bet'] > 0.0].groupby('Seats')['Flop_Bet85_110%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='FlopBet85_110%')
df2_Flop_BetM110 = df2[df2['Flop_Bet'] > 0.0].groupby('Seats')['Flop_BetM110%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='FlopBetMore110%')

df2_Turn_BetL40 = df2[df2['Turn_Bet'] > 0.0].groupby('Seats')['Turn_BetL40%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='TurnBetLower40%')
df2_Turn_Bet40_60 = df2[df2['Turn_Bet'] > 0.0].groupby('Seats')['Turn_Bet40_60%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='TurnBet40_60%')
df2_Turn_Bet60_70 = df2[df2['Turn_Bet'] > 0.0].groupby('Seats')['Turn_Bet60_70%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='TurnBet60_70%')
df2_Turn_Bet70_85 = df2[df2['Turn_Bet'] > 0.0].groupby('Seats')['Turn_Bet70_85%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='TurnBet70_85%')
df2_Turn_Bet85_110 = df2[df2['Turn_Bet'] > 0.0].groupby('Seats')['Turn_Bet85_110%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='TurnBet85_110%')
df2_Turn_BetM110 = df2[df2['Turn_Bet'] > 0.0].groupby('Seats')['Turn_BetM110%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='TurnBetMore110%')

df2_River_BetL40 = df2[df2['River_Bet'] > 0.0].groupby('Seats')['River_BetL40%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='RiverBetLower40%')
df2_River_Bet40_60 = df2[df2['River_Bet'] > 0.0].groupby('Seats')['River_Bet40_60%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='RiverBet40_60%')
df2_River_Bet60_70 = df2[df2['River_Bet'] > 0.0].groupby('Seats')['River_Bet60_70%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='RiverBet60_70%')
df2_River_Bet70_85 = df2[df2['River_Bet'] > 0.0].groupby('Seats')['River_Bet70_85%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='RiverBet70_85%')
df2_River_Bet85_110 = df2[df2['River_Bet'] > 0.0].groupby('Seats')['River_Bet85_110%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='RiverBet85_110%')
df2_River_BetM110 = df2[df2['River_Bet'] > 0.0].groupby('Seats')['River_BetM110%'].value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='RiverBetMore110%')
 
# =============================================================================
# Vpip, vpip pozycyjny
#dfVPIP = df2.groupby('Seats').Vpip.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='Vpip%')
#dfVPIP_BB = df2[df2['Position'] == 'BB'].groupby('Seats').Vpip.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='VpipBB%')
#dfVPIP_SB = df2[df2['Position'] == 'SB'].groupby('Seats').Vpip.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='VpipSB%')
#dfVPIP_BTN = df2[df2['Position'] == 'BTN'].groupby('Seats').Vpip.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='VpipBTN%')
#dfVPIP_CO = df2[df2['Position'] == 'CO'].groupby('Seats').Vpip.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='VpipCO%')
#dfVPIP_MP = df2[df2['Position'] == 'MP'].groupby('Seats').Vpip.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='VpipMP%')
#dfVPIP_EP = df2[df2['Position'] == 'EP'].groupby('Seats').Vpip.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='VpipEP%')
#
## Pfr, Pfr pozycyjny
#dfPFR = df2.groupby('Seats').Pfr.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='Pfr%')
#dfPFR_BB = df2[df2['Position'] == 'BB'].groupby('Seats').Pfr.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='PfrBB%')
#dfPFR_SB = df2[df2['Position'] == 'SB'].groupby('Seats').Pfr.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='PfrSB%')
#dfPFR_BTN = df2[df2['Position'] == 'BTN'].groupby('Seats').Pfr.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='PfrBTN%')
#dfPFR_CO = df2[df2['Position'] == 'CO'].groupby('Seats').Pfr.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='PfrCO%')
#dfPFR_MP = df2[df2['Position'] == 'MP'].groupby('Seats').Pfr.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='PfrMP%')
#dfPFR_EP = df2[df2['Position'] == 'EP'].groupby('Seats').Pfr.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name='PfrEP%')
#
##Went to SD, when see flop, turn, river
#dfWTSD_WSF = df2[df2['Saw_Flop'] == 1].groupby('Seats').WTSD.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name = 'WTSD_WSF%')
#dfWTSD_WST = df2[df2['Saw_Turn'] == 1].groupby('Seats').WTSD.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name = 'WTSD_WST%')
#dfWTSD_WSR = df2[df2['Saw_River'] == 1].groupby('Seats').WTSD.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name = 'WTSD_WSR%')
#
## Won When saw flop, turn, river
#dfWWSF = df2[df2['Saw_Flop'] == 1].groupby('Seats').Won.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name = 'WWSF%')
#dfWWST = df2[df2['Saw_Turn'] == 1].groupby('Seats').Won.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name = 'WWST%')
#dfWWSR = df2[df2['Saw_River'] == 1].groupby('Seats').Won.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name = 'WWSR%')
#
## Won money at SD when saw flop, turn, river
#dfWMSD_WSF = df2[(df2['Saw_Flop'] == 1) & (df2['WTSD'] == 'Yes')].groupby('Seats').Won.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name = 'WMSD_WSF%')
#dfWMSD_WST = df2[(df2['Saw_Turn'] == 1) & (df2['WTSD'] == 'Yes')].groupby('Seats').Won.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name = 'WMSD_WST%')
#dfWMSD_WSR = df2[(df2['Saw_River'] == 1) & (df2['WTSD'] == 'Yes')].groupby('Seats').Won.value_counts().groupby(level=0).apply(lambda x: x/x.sum()*100).loc(axis=0)[slice(None), 'Yes'].reset_index(drop=True, level=1).reset_index(name = 'WMSD_WSR%')

##Aggression
#dfAGG = df2.replace([np.inf, -np.inf, 0.0], np.NaN).dropna(subset = ['Agg']).groupby('Seats').Agg.mean().to_frame().reset_index()
#
#dfAGG_Flop = df2.replace([np.inf, -np.inf, 0.0], np.NaN).dropna(subset = ['Agg_Flop']).groupby('Seats').Agg_Flop.mean().to_frame().reset_index()
#dfAGG_Turn = df2.replace([np.inf, -np.inf, 0.0], np.NaN).dropna(subset = ['Agg_Turn']).groupby('Seats').Agg_Turn.mean().to_frame().reset_index()
#dfAGG_River = df2.replace([np.inf, -np.inf, 0.0], np.NaN).dropna(subset = ['Agg_River']).groupby('Seats').Agg_River.mean().to_frame().reset_index()
##Winnings
#dfWINNINGS = df2.groupby('Seats').Winnings.sum().reset_index()
#
##hands played
#dfHANDS = df2.groupby('Seats').Hand_ID.count().reset_index()#ok

#dfs = [dfWon, dfVPIP, dfVPIP_BB, dfVPIP_SB, dfVPIP_BTN, dfVPIP_CO, dfVPIP_MP, dfVPIP_EP,dfPFR, dfPFR_BB, dfPFR_SB, dfPFR_BTN, dfPFR_CO, dfPFR_MP, dfPFR_EP, 
#       dfWTSD_WSF, dfWTSD_WST, dfWTSD_WSR, dfWWSF, dfWWST, dfWWSR, dfWMSD_WSF, dfWMSD_WST, dfWMSD_WSR, dfWINNINGS, dfHANDS]
dfs = [df2_Flop_BetL40, df2_Flop_Bet40_60, df2_Flop_Bet60_70, df2_Flop_Bet70_85, df2_Flop_Bet85_110, df2_Flop_BetM110,
       df2_Turn_BetL40, df2_Turn_Bet40_60, df2_Turn_Bet60_70, df2_Turn_Bet70_85, df2_Turn_Bet85_110, df2_Turn_BetM110,
       df2_River_BetL40, df2_River_Bet40_60, df2_River_Bet60_70, df2_River_Bet70_85, df2_River_Bet85_110, df2_River_BetM110]
#       dfAGG, dfAGG_Flop, dfAGG_Turn, dfAGG_River]
from functools import reduce
df_Bets = reduce(lambda left, right: pd.merge(left, right, on = 'Seats', how = 'outer'), dfs)

df_Bets.to_csv(r'C:\Users\Adam\Desktop\Python\Master\df_Bets.csv')
