# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:41:02 2019

@author: Adam
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

#Policzenie ile razy ktos raisowa, callowal
import ast
i=0
for i in range(len(df2)):
    df2.at[i, 'Flop_Raise_Len'] = len(ast.literal_eval(df2['Flop_Raise'][i]))
    df2.at[i, 'Flop_Call_Len'] = len(ast.literal_eval(df2['Flop_Call'][i]))
    df2.at[i, 'Turn_Raise_Len'] = len(ast.literal_eval(df2['Turn_Raise'][i]))
    df2.at[i, 'Turn_Call_Len'] = len(ast.literal_eval(df2['Turn_Call'][i]))
    df2.at[i, 'River_Raise_Len'] = len(ast.literal_eval(df2['River_Raise'][i]))
    df2.at[i, 'River_Call_Len'] = len(ast.literal_eval(df2['River_Call'][i]))
    i+=1
  
    



#policzenie ile razy ktos betowal
df2['Flop_Bet_Len'] = [0 if x == 0.0 else 1 for x in df2['Flop_Bet']]
df2['Turn_Bet_Len'] = [0 if x == 0.0 else 1 for x in df2['Turn_Bet']]
df2['River_Bet_Len'] = [0 if x == 0.0 else 1 for x in df2['River_Bet']]

#policzenie agresji ogolnej oraz flop, turn, river
df2['Agg'] = (df2['Flop_Bet_Len'] + df2['Turn_Bet_Len'] + df2['River_Bet_Len'] + df2['Flop_Raise_Len'] + df2['Turn_Raise_Len'] +
   df2['River_Raise_Len'])/(df2['Flop_Call_Len'] + df2['Turn_Call_Len'] + df2['River_Call_Len'])

df2['Agg_Flop'] = (df2['Flop_Bet_Len'] + df2['Flop_Raise_Len'])/(df2['Flop_Call_Len'])
df2['Agg_Turn'] = (df2['Turn_Bet_Len'] + df2['Turn_Raise_Len'])/(df2['Turn_Call_Len'])
df2['Agg_River'] = (df2['River_Bet_Len'] + df2['River_Raise_Len'])/(df2['River_Call_Len'])

df2.to_csv(r'C:\Users\Adam\Desktop\Python\Master\afterast.csv') 
 
df2 = pd.read_csv(r'C:\Users\Adam\Desktop\Python\Master\afterast.csv', 
                  usecols = ['Seats', 'Agg', 'Agg_Flop', 'Agg_Turn', 'Agg_River']) 
#Aggression
dfAGG = df2.replace([np.inf, -np.inf, 0.0], np.NaN).dropna(subset = ['Agg']).groupby('Seats').Agg.mean().to_frame().reset_index()

dfAGG_Flop = df2.replace([np.inf, -np.inf, 0.0], np.NaN).dropna(subset = ['Agg_Flop']).groupby('Seats').Agg_Flop.mean().to_frame().reset_index()
dfAGG_Turn = df2.replace([np.inf, -np.inf, 0.0], np.NaN).dropna(subset = ['Agg_Turn']).groupby('Seats').Agg_Turn.mean().to_frame().reset_index()
dfAGG_River = df2.replace([np.inf, -np.inf, 0.0], np.NaN).dropna(subset = ['Agg_River']).groupby('Seats').Agg_River.mean().to_frame().reset_index()
##Winnings


dfs = [dfAGG, dfAGG_Flop, dfAGG_Turn, dfAGG_River]

from functools import reduce
df_Agg = reduce(lambda left, right: pd.merge(left, right, on = 'Seats', how = 'outer'), dfs)

df_Agg.to_csv(r'C:\Users\Adam\Desktop\Python\Master\df_Agg.csv', index = False)
