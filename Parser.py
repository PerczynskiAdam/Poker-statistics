# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:29:40 2019

@author: Adam
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:21:29 2019

@author: AdamPer
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:24:46 2019

@author: AdamPer
"""

# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
import csv
import glob
import re
import collections

soft = ''
hand_id = ''
currency = ''
day = ''
hour = ''
table_name = ''
position = ['BTN', 'SB', 'BB', 'EP', 'MP', 'CO']
button = 0
writer = 0
myState = 0
numPlayers = 0
potSize = 0
rake = 0
SmallBlind = 0
BigBlind = 0
seatVec = [0, 0, 0, 0, 0, 0]
stackVec = [0, 0, 0, 0, 0, 0]
raiseVecPre = [[], [], [], [], [], []]
callVecPre = [[], [],[],[],[],[]]
betVecFlop = [0, 0, 0, 0, 0, 0]
raiseVecFlop = [[], [], [], [], [], []]
callVecFlop = [[], [], [], [], [], []]
betVecTurn = [0, 0, 0, 0, 0, 0]
raiseVecTurn = [[], [], [], [], [], []]
callVecTurn = [[], [], [], [], [], []]
betVecRiver = [0, 0, 0, 0, 0, 0]
raiseVecRiver = [[], [], [], [], [], []]
callVecRiver = [[], [], [], [], [], []]
winVecSd = [0, 0, 0, 0, 0, 0]
SdVec = [0, 0, 0, 0, 0, 0]
PutPRE = [0, 0, 0, 0, 0, 0]
PutFLOP = [0, 0, 0, 0, 0, 0]
SawFLOP = [0, 0, 0, 0, 0, 0]
PutTURN = [0, 0, 0, 0, 0, 0]
SawTURN = [0, 0, 0, 0, 0, 0]
PutRIVER = [0, 0, 0, 0, 0, 0]
SawRIVER = [0, 0, 0, 0, 0, 0]
Winnings = [0, 0, 0, 0, 0, 0]
Win_money = [0, 0, 0, 0, 0, 0]

#setRaises(stringy,raisey,dingle,4)

# setState
# INPUTS: a string for every line
# The current gamestate
def setState(myStr):
    global myState
    if "PokerStars" in myStr:
        myState = 1
        return
#    # Check to see if we have proper number of players
#    if ("sits out" in myStr) or ("is sitting out" in myStr):
#        myState = 0
    if "posts small blind" in myStr:
        if numPlayers !=6:#parse hands with only full tables.
            myState = 0
            return
        else:
            myState = 2 
            return
    # If we have more than 2 players proceed parsing normally
    # o/w gameState doesn't change
    if myState != 0:        
        if "*** HOLE CARDS ***" in myStr:
            myState = 3
            return
        if "*** FLOP ***" in myStr:
            myState = 4
            return
        if "*** TURN ***" in myStr:
            myState = 5
            return
        if "*** RIVER ***" in myStr:
            myState = 6
            return
        if " SHOW DOWN " in myStr:
            myState = 7
            return
        if "*** SUMMARY ***" in myStr:
            myState = 8
            return
        else:
            return
    else:
        return


# setSeats
# INPUTS: a string in the gamestate 1
#         a vector linking player names to seats
#         and an index for current seat number
# OUTPUTS: an updated vector linking player names
#         to seats
def setSeats(myStr):
    global seatVec
    global numPlayers
    if "chips" in myStr:
        if not(numPlayers >= 6):
            #Get player name from myString
            namesky = myStr.split(":")[1].split('(')[0].strip()
            seatVec[numPlayers] = namesky#wpisuje na pierwsza pozycje nickname i dodaje 1.
            numPlayers = numPlayers + 1
            return
        else: 
            numPlayers = numPlayers + 1
            return
    else:
        return
    
# set positions to players depened where BTN is
#def setPositionsBTN(myStr):
#    global button
#    if "Table" in myStr:
#        button += int(myStr.split('#')[1].split(' ')[0])
#        return
#    else:
#        return

        

# setChipCount
# INPUTS: a string in the gamestate 1
#         a vector linking chip counts to seats
#         and an index for current seat number
# OUTPUTS: an updated vector linking player names
#         to seats
def setChipCount(myStr):
    global stackVec
    if "chips" in myStr:
        if not(numPlayers >= 7):
            chipskystr = re.split('[\$\€\£]', myStr.split('(')[1])[1].split(' ')[0]
            chipsky = float(chipskystr)
            stackVec[numPlayers-1] = chipsky#nie rozumiem tego -1
            return
        else: 
            return
    else: 
        return

#set soft name
def setSoft(myStr):
    global soft
    if "PokerStars" in myStr:
        soft = myStr.split(' ')[0]
        return
    else:
        return
    
#set Hand_id
def setHandID(myStr):
    global hand_id
    if "PokerStars" in myStr:
        hand_id = myStr.split('#')[1].split(':')[0]
        return
    else:
        return

#set blinds
def setBlinds(myStr):
    global currency
    global SmallBlind
    global BigBlind
    if "PokerStars" in myStr:
        currency = myStr.split('(')[1].split(')')[0].split(' ')[1]
        SmallBlind = re.split('[\$\€\£]', myStr.split('(')[1].split(')')[0].split('/')[0])[1]
        BigBlind = re.split('[\$\€\£]', myStr.split('(')[1].split(')')[0].split('/')[1].split(' ')[0])[1]
        return
    else:
        return
    
#set day
def setDay(myStr):
    global day
    global hour
    if "PokerStars" in myStr:
        day = myStr.split('-')[1].split(' ')[1]
        hour = myStr.split('-')[1].split(' ')[2]
        return
    else:
        return

#set hour
#def setHour(myStr):
#    global hour
#    if "PokerStars" in myStr:
#        hour = myStr.split(' ')[11]
#        return
#    else:
#        return        
    
#set table size
def setTableName(myStr):
    global table_name
    if "Table" in myStr:
        table_name = myStr.split('\'')[1]
        return
    else:
        return
    

# setPotSize
# INPUTS: a string in the gamestate 2-5
#         a float of current pot size
# OUTPUTS: an updated pot size        
def setPotSize(myStr):
    global potSize# to jest zero na poczatku
    if "posts" in myStr:
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(' ')[-1])[1])
        potSize = round((potSize + moneys), 2)
        PutPRE[indy] += -moneys
    elif ("raises" in myStr) and ("is all-in" not in myStr):
        moneys = float(re.split('[\$\€\£]', myStr.split('to ')[1])[1])
        potSize = round((potSize + moneys), 2)
        return
    elif ("raises" in myStr) and ("is all-in" in myStr):
        moneys = float(re.split('[\$\€\£]', myStr.split('to ')[1].split(' ')[0])[1])
        potSize = round((potSize + moneys), 2)
        return
    elif ("calls" in myStr) and ("is all-in" not in myStr):
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1])[1])
        potSize = round((potSize + moneys), 2)
        return
    elif ("calls" in myStr) and ("is all-in" in myStr):
        moneys = float(re.split('[\$\€\£]', myStr.split('calls')[1].split(' ')[1])[1])
        potSize = round((potSize + moneys), 2)
        return
    elif ("bets" in myStr) and ("is all-in" not in myStr):
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1])[1])
        potSize = round((potSize + moneys), 2)
        return
    elif ("bets" in myStr) and ("is all-in" in myStr):
        moneys = float(re.split('[\$\€\£]', myStr.split('bets')[1].split(' ')[1])[1])
        potSize = round((potSize + moneys), 2)
    elif "Uncalled" in myStr:
        moneys = float(re.split('[\$\€\£]', myStr.split(')')[0])[1])
        potSize = round((potSize - moneys), 2)
        return

    

# setBets
# INPUTS: a string in gamestate 2-5
#         a vector of bet info
#         a vector of seat info
#def setBets3(myStr):
#    global betVec3       
#    if ("bets" in myStr):
#        name = myStr.split(" ")[0]
#        indy = seatVec.index(name)
#        moneys = float(myStr.split("$")[1].split(" ")[0])
#        betVec3[indy] = float(moneys/potSize)
#        return
#    else:
#        return

# setRaises
# INPUTS: a string in gamestate 2-5
#         a vector of raise info
#         a vector of seat info
def setRaises3(myStr):
    global raiseVecPre
    global PutPRE
    if ("raises" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        raises = float(re.split('[\$\€\£]', myStr.split(':')[1].split('to ')[0])[1].strip())
        raises_to = float(re.split('[\$\€\£]', myStr.split('to ')[1])[1])
        raiseVecPre[indy].append(round(raises/(potSize + (raises_to - raises)), 2))
        PutPRE[indy] = -raises_to
        return
    elif ("raises" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        raises = float(re.split('[\$\€\£]', myStr.split(':')[1].split('to ')[0])[1].strip())
        raises_to = float(re.split('[\$\€\£]', myStr.split('to ')[1])[1].split(' ')[0])
        raiseVecPre[indy].append(round(raises/(potSize + (raises_to - raises)), 2))
        PutPRE[indy] = -raises_to
        return
    elif "Uncalled" in myStr:
        name = myStr.split('to ')[1].strip()
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(')')[0])[1])
        PutPRE[indy] -= -moneys
        return          
    else:
        return

# setCall
# INPUTS: a string in gamestate 2-5
#         a vector of call info
#         a vector of seat info
def setCalls3(myStr):
    global callVecPre
    global PutPRE
    if ("calls" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1])[1])
        callVecPre[indy].append(moneys)
        PutPRE[indy] += -moneys
        return
    elif ("calls" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1].split(' ')[2])[1])
        callVecPre[indy].append(moneys)
        PutPRE[indy] += -moneys
        return        
    else:
        return

# setBets
# INPUTS: a string in gamestate 2-5
#         a vector of bet info
#         a vector of seat info
def setBets4(myStr):
    global betVecFlop 
    global PutFLOP      
    if ("bets" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1])[1])
        betVecFlop[indy] = round((moneys/potSize), 2)
        PutFLOP[indy] += -moneys
        return
    elif ("bets" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1].split(' ')[2])[1])
        betVecFlop[indy] = round((moneys/potSize), 2)
        PutFLOP[indy] += -moneys
        return
    elif "Uncalled bet" in myStr:
        name = myStr.split('to ')[1].strip()
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(')')[0])[1])
        PutFLOP[indy] -= -moneys
        return 
    else:
        return

# setRaises
# INPUTS: a string in gamestate 2-5
#         a vector of raise info
#         a vector of seat info
def setRaises4(myStr):
    global raiseVecFlop
    global PutFLOP
    if ("raises" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        raises = float(re.split('[\$\€\£]', myStr.split(':')[1].split('to ')[0])[1].strip())
        raises_to = float(re.split('[\$\€\£]', myStr.split('to ')[1])[1])
        raiseVecFlop[indy].append(round(raises/(potSize + (raises_to - raises)), 2))
        PutFLOP[indy] = -raises_to
        return
    elif ("raises" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        raises = float(re.split('[\$\€\£]', myStr.split(':')[1].split('to ')[0])[1].strip())
        raises_to = float(re.split('[\$\€\£]', myStr.split('to ')[1])[1].split(' ')[0])
        raiseVecFlop[indy].append(round(raises/(potSize + (raises_to - raises)), 2))
        PutFLOP[indy] = -raises_to
        return
    elif "Uncalled raise" in myStr:
        name = myStr.split('to ')[1].strip()
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(')')[0])[1])
        PutFLOP[indy] -= -moneys
        return   
    else:
        return

# setCall
# INPUTS: a string in gamestate 2-5
#         a vector of call info
#         a vector of seat info
def setCalls4(myStr):
    global callVecFlop
    global PutFLOP
    if ("calls" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1])[1])
        callVecFlop[indy].append(moneys)
        PutFLOP[indy] += -moneys
        return
    elif ("calls" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1].split(' ')[2])[1])
        callVecFlop[indy].append(moneys)
        PutFLOP[indy] += -moneys
        return        
    else:
        return


def setSawFLOP(myStr):
    global SawFLOP
    if ("checks" in myStr) or ("calls" in myStr) or ("bets" in myStr) or ("raises" in myStr) or ("folds" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        SawFLOP[indy] = 1
        return
    else:
        return

# setBets
# INPUTS: a string in gamestate 2-5
#         a vector of bet info
#         a vector of seat info
def setBets5(myStr):
    global betVecTurn    
    global PutTURN
    if ("bets" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1])[1])
        betVecTurn[indy] = round((moneys/potSize), 2)
        PutTURN[indy] += -moneys
        return
    elif ("bets" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1].split(' ')[2])[1])
        betVecTurn[indy] = round((moneys/potSize), 2)
        PutTURN[indy] += -moneys
        return 
    elif "Uncalled bet" in myStr:
        name = myStr.split('to ')[1].strip()
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(')')[0])[1])
        PutTURN[indy] += moneys
        return        
    else:
        return

# setRaises
# INPUTS: a string in gamestate 2-5
#         a vector of raise info
#         a vector of seat info
def setRaises5(myStr):
    global raiseVecTurn
    global PutTURN
    if ("raises" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        raises = float(re.split('[\$\€\£]', myStr.split(':')[1].split('to ')[0])[1].strip())
        raises_to = float(re.split('[\$\€\£]', myStr.split('to ')[1])[1])
        raiseVecTurn[indy].append(round(raises/(potSize + (raises_to - raises)), 2))
        PutTURN[indy] = -raises_to
        return
    elif ("raises" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        raises = float(re.split('[\$\€\£]', myStr.split(':')[1].split('to ')[0])[1].strip())
        raises_to = float(re.split('[\$\€\£]', myStr.split('to ')[1])[1].split(' ')[0])
        raiseVecTurn[indy].append(round(raises/(potSize + (raises_to - raises)), 2))  
        PutTURN[indy] = -raises_to
        return
    elif "Uncalled raise" in myStr:
        name = myStr.split('to ')[1].strip()
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(')')[0])[1])
        PutTURN[indy] -= -moneys
        return   
    else:
        return

# setCall
# INPUTS: a string in gamestate 2-5
#         a vector of call info
#         a vector of seat info
def setCalls5(myStr):
    global callVecTurn
    global PutTURN
    if ("calls" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1])[1])
        callVecTurn[indy].append(moneys)
        PutTURN[indy] += -moneys
        return
    elif ("calls" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1].split(' ')[2])[1])
        callVecTurn[indy].append(moneys)
        PutTURN[indy] += -moneys
        return        
    else:
        return
    
def setSawTURN(myStr):
    global SawTURN
    if ("checks" in myStr) or ("calls" in myStr) or ("bets" in myStr) or ("raises" in myStr) or ("folds" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        SawTURN[indy] = 1
        return
    else:
        return

# setBets
# INPUTS: a string in gamestate 2-5
#         a vector of bet info
#         a vector of seat info
def setBets6(myStr):
    global betVecRiver 
    global PutRIVER     
    if ("bets" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1].split(' ')[2])[1])
        betVecRiver[indy] = round((moneys/potSize), 2)
        PutRIVER[indy] += -moneys
        return
    elif ("bets" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1].split(' ')[2])[1])
        betVecRiver[indy] = round((moneys/potSize), 2)
        PutRIVER[indy] += -moneys
        return
    elif "Uncalled bet" in myStr:
        name = myStr.split('to ')[1].strip()
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(')')[0])[1])
        PutRIVER[indy] -= -moneys
        return  
    else:
        return

# setRaises
# INPUTS: a string in gamestate 2-5
#         a vector of raise info
#         a vector of seat info
def setRaises6(myStr):
    global raiseVecRiver
    global PutRIVER
    if ("raises" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        raises = float(re.split('[\$\€\£]', myStr.split(':')[1].split('to ')[0])[1].strip())
        raises_to = float(re.split('[\$\€\£]', myStr.split('to ')[1])[1])
        raiseVecRiver[indy].append(round(raises/(potSize + (raises_to - raises)), 2))
        PutRIVER[indy] = -raises_to
        return
    elif ("raises" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        raises = float(re.split('[\$\€\£]', myStr.split(':')[1].split('to ')[0])[1].strip())
        raises_to = float(re.split('[\$\€\£]', myStr.split('to ')[1])[1].split(' ')[0])
        raiseVecRiver[indy].append(round(raises/(potSize + (raises_to - raises)), 2))
        PutRIVER[indy] = -raises_to
    elif "Uncalled raise" in myStr:
        name = myStr.split('to ')[1].strip()
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(')')[0])[1])
        PutRIVER[indy] -= -moneys
        return   
    else:
        return

# setCall
# INPUTS: a string in gamestate 2-5
#         a vector of call info
#         a vector of seat info
def setCalls6(myStr):
    global callVecRiver
    global PutRIVER
    if ("calls" in myStr) and ("is all-in" not in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1])[1])
        callVecRiver[indy].append(moneys)
        PutRIVER[indy] += -moneys
        return
    elif ("calls" in myStr) and ("is all-in" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        moneys = float(re.split('[\$\€\£]', myStr.split(':')[1].split(' ')[2])[1])
        callVecRiver[indy].append(moneys) 
        PutRIVER[indy] += -moneys
        return
    else:
        return

#            moneys1 = float(re.split('[\$\€\£]', re.split(r'collected|and won', myStr)[1].split(')')[0])[1])
#            moneys2 = float(re.split('[\$\€\£]', re.split(r'collected|and won', myStr)[2].split(')')[0])[1])        


def setSawRIVER(myStr):
    global SawRIVER
    if ("checks" in myStr) or ("calls" in myStr) or ("bets" in myStr) or ("raises" in myStr) or ("folds" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        SawRIVER[indy] = 1
        return
    else:
        return
#
def setWinner(myStr):
    global winVecSd 
    global Win_money      
    if ("collected" in myStr) or ("and won" in myStr):
        if ("big blind" in myStr) or ("small blind" in myStr) or ("button" in myStr):
            if (myStr.count("and won") == 2):
                name = re.split("collected", myStr)[0].split(':')[1].split('(')[0].strip()
                indy = seatVec.index(name)
                winVecSd[indy] = 1
                moneys1 = float(re.split('[\$\€\£]', re.split(r'collected|and won', myStr)[1].split(')')[0])[1])
                moneys2 = float(re.split('[\$\€\£]', re.split(r'collected|and won', myStr)[2].split(')')[0])[1]) 
                Win_money[indy] = moneys1 + moneys2
            else:
                name = re.split("collected", myStr)[0].split(':')[1].split('(')[0].strip()
                indy = seatVec.index(name)
                winVecSd[indy] = 1
                moneys = float(re.split('[\$\€\£]', re.split(r'collected|and won', myStr)[1].split(')')[0])[1])
                Win_money[indy] = moneys
            return
        else: #("big blind" not in myStr) and ("small blind" not in myStr)
            if (myStr.count("and won") == 2):
                name = re.split(r'collected|and won', myStr)[0].split(':')[1].split('showed')[0].strip()
                indy = seatVec.index(name)
                winVecSd[indy] = 1
                moneys1 = float(re.split('[\$\€\£]', re.split(r'collected|and won', myStr)[1].split(')')[0])[1])
                moneys2 = float(re.split('[\$\€\£]', re.split(r'collected|and won', myStr)[2].split(')')[0])[1])
                Win_money[indy] = moneys1 + moneys2                              
            else:
                name = re.split(r'collected|and won', myStr)[0].split(':')[1].split('showed')[0].strip()
                indy = seatVec.index(name)
                winVecSd[indy] = 1
                moneys = float(re.split('[\$\€\£]', re.split(r'collected|and won', myStr)[1].split(')')[0])[1])
                Win_money[indy] = moneys
            return
    else:
        return

def setWinnings():
    global Winnings
    Winnings = [sum(x) for x in zip(PutFLOP, PutPRE, PutTURN, PutRIVER, Win_money)]
    return

def setSawSD(myStr):
    global SdVec
    if ("shows" in myStr) or ("mucks" in myStr):
        name = myStr.split(':')[0]
        indy = seatVec.index(name)
        SdVec[indy] = 1
        return
    else:
        return
        

#set rake size
def setRake(myStr):
    global rake
    if "Total pot" in myStr:
        rake += float(re.split('[\$\€\£]', myStr.split('|')[1])[1])
        return
    else:
        return


def setPosVec(myStr):
    global position
    global button
#    global numplayers
    if "Table" in myStr:
        button = int(myStr.split('#')[1].split(' ')[0])
#        position = position[:numPlayers]
        position = collections.deque(position)
        position.rotate(button-1)
        position = list(position)
        return



def initGame():
     global soft
     global hand_id
     global currency
     global day
     global hour
     global table_name
     global myState
     global numPlayers
     global button
     global position
     global potSize
     global rake
     global seatVec
     global stackVec
     global raiseVecPre
     global callVecPre
     global betVecFlop
     global raiseVecFlop
     global callVecFlop
     global betVecTurn
     global raiseVecTurn
     global callVecTurn
     global betVecRiver
     global raiseVecRiver
     global callVecRiver
     global winVecSd
     global SdVec
     global PutPRE
     global PutFLOP
     global SawFLOP
     global PutTURN
     global SawTURN
     global PutRIVER
     global SawRIVER
     global Winnings
     global Win_money
     global SmallBlind
     global BigBlind
     soft = ''
     hand_id = ''
     currency = ''
     day = ''
     hour = ''
     table_name = ''
     myState = 0
     numPlayers = 0
     potSize = 0
     rake = 0
     button = 0
     SmallBlind = 0
     BigBlind = 0
     position = ['BTN', 'SB', 'BB', 'EP', 'MP', 'CO']
     seatVec = [0, 0, 0, 0, 0, 0]
     stackVec = [0, 0, 0, 0, 0, 0]
     raiseVecPre = [[], [], [], [], [], []]
     callVecPre = [[], [], [], [], [], []]
     betVecFlop = [0,0,0,0,0,0]
     raiseVecFlop = [[], [], [], [], [], []]
     callVecFlop = [[], [], [], [], [], []]
     betVecTurn = [0, 0, 0, 0, 0, 0]
     raiseVecTurn = [[], [], [], [], [], []]
     callVecTurn = [[], [], [], [], [], []]
     betVecRiver = [0, 0, 0, 0, 0, 0]
     raiseVecRiver = [[], [], [], [], [], []]
     callVecRiver = [[], [], [], [], [], []]
     winVecSd = [0, 0, 0, 0, 0, 0]
     SdVec = [0, 0, 0, 0, 0, 0]
     PutPRE = [0, 0, 0, 0, 0, 0]
     PutFLOP = [0, 0, 0, 0, 0, 0]
     SawFLOP = [0, 0, 0, 0, 0, 0]
     PutTURN = [0, 0, 0, 0, 0, 0]
     SawTURN = [0, 0, 0, 0, 0, 0]
     PutRIVER = [0, 0, 0, 0, 0, 0]
     SawRIVER = [0, 0, 0, 0, 0, 0]
     Winnings = [0, 0, 0, 0, 0, 0]
     Win_money = [0, 0, 0, 0, 0, 0]

def makeGameArray():
    gameArray = []
    gameArray.append(soft)
    gameArray.append(hand_id)
    gameArray.append(table_name)
    gameArray.append(SmallBlind)
    gameArray.append(BigBlind)
    gameArray.append(currency)
    gameArray.append(day)
    gameArray.append(hour)
#    gameArray.append(numPlayers)
    gameArray.extend(seatVec)
    gameArray.extend(stackVec)
    gameArray.extend(position)
    gameArray.extend(raiseVecPre)
    gameArray.extend(callVecPre)
#    gameArray.extend(avgVec(raiseVec3))
#    gameArray.extend(avgVec(callVec3))
    gameArray.extend(betVecFlop)
    gameArray.extend(raiseVecFlop)
    gameArray.extend(callVecFlop)
    gameArray.extend(SawFLOP)
#    gameArray.extend(avgVec(raiseVec4))
#    gameArray.extend(avgVec(callVec4))
    gameArray.extend(betVecTurn)
    gameArray.extend(raiseVecTurn)
    gameArray.extend(callVecTurn)
    gameArray.extend(SawTURN)
#    gameArray.extend(avgVec(raiseVec5))
#    gameArray.extend(avgVec(callVec5))
    gameArray.extend(betVecRiver)
    gameArray.extend(raiseVecRiver)
    gameArray.extend(callVecRiver)
    gameArray.extend(SawRIVER)
#    gameArray.extend(avgVec(raiseVec6))
#    gameArray.extend(avgVec(callVec6))
    gameArray.extend(SdVec)
    gameArray.extend(winVecSd)
    gameArray.extend(Winnings)
    gameArray.append(potSize)
    gameArray.append(rake)
    return gameArray

#def makeDict():
#    dicty = {'Soft':soft,
#            'Hand_ID': hand_id,
#            'Table_Size': table_size,
#            'Blinds': blinds,
#            'Day': day,
#            'No_of_players':numPlayers,
#            'Pot_Size':potSize,
#            'Rake':rake,
#            'Seats':seatVec,
#            'Stacks':stackVec,
#            'RaisePre':raiseVecPre,
#            'CallPre':callVecPre,
#            'BetFlop':betVecFlop,
#            'RaiseFlop':raiseVecFlop,
#            'CallFlop':callVecFlop,
#            'BetTurn':betVecTurn,
#            'RaiseTurn':raiseVecTurn,
#            'CallTurn':callVecTurn,
#            'BetRiver':betVecRiver,
#            'RaiseRiver':raiseVecRiver,
#            'CallRiver':callVecRiver,
#            'Winner':winVe cSd}

header = ['Soft',
          'Hand_ID',
          'Table_Name',
          'SmallBlind',
          'BigBlind',
          'Currency',
          'Day',
          'Hour',
#          'No_of_players',
          'Seat_1','Seat_2','Seat_3', 'Seat_4', 'Seat_5', 'Seat_6', 
          'Stack_1', 'Stack_2', 'Stack_3', 'Stack_4','Stack_5', 'Stack_6',
          'S1_pos', 'S2_pos', 'S3_pos', 'S4_pos', 'S5_pos', 'S6_pos',
'Raise_Pre_S1', 'Raise_Pre_S2', 'Raise_Pre_S3', 'Raise_Pre_S4', 'Raise_Pre_S5', 'Raise_Pre_S6',
'Call_Pre_S1', 'Call_Pre_S2', 'Call_Pre_S3', 'Call_Pre_S4', 'Call_Pre_S5', 'Call_Pre_S6',
'Flop_Bet_S1', 'Flop_Bet_S2', 'Flop_Bet_S3', 'Flop_Bet_S4', 'Flop_Bet_S5', 'Flop_Bet_S6',
'Flop_Raise_S1', 'Flop_Raise_S2', 'Flop_Raise_S3', 'Flop_Raise_S4', 'Flop_Raise_S5', 'Flop_Raise_S6',
'Flop_Call_S1', 'Flop_Call_S2', 'Flop_Call_S3', 'Flop_Call_S4', 'Flop_Call_S5', 'Flop_Call_S6',
'Saw_Flop_S1', 'Saw_Flop_S2', 'Saw_Flop_S3', 'Saw_Flop_S4', 'Saw_Flop_S5', 'Saw_Flop_S6',
'Turn_Bet_S1', 'Turn_Bet_S2', 'Turn_Bet_S3', 'Turn_Bet_S4', 'Turn_Bet_S5', 'Turn_Bet_S6',
'Turn_Raise_S1', 'Turn_Raise_S2', 'Turn_Raise_S3', 'Turn_Raise_S4', 'Turn_Raise_S5', 'Turn_Raise_S6',
'Turn_Call_S1', 'Turn_Call_S2', 'Turn_Call_S3', 'Turn_Call_S4', 'Turn_Call_S5', 'Turn_Call_S6',
'Saw_Turn_S1', 'Saw_Turn_S2', 'Saw_Turn_S3', 'Saw_Turn_S4', 'Saw_Turn_S5', 'Saw_Turn_S6',
'River_Bet_S1', 'River_Bet_S2', 'River_Bet_S3', 'River_Bet_S4', 'River_Bet_S5', 'River_Bet_S6',
'River_Raise_S1', 'River_Raise_S2', 'River_Raise_S3', 'River_Raise_S4', 'River_Raise_S5', 'River_Raise_S6',
'River_Call_S1', 'River_Call_S2', 'River_Call_S3', 'River_Call_S4', 'River_Call_S5', 'River_Call_S6',
'Saw_River_S1', 'Saw_River_S2', 'Saw_River_S3', 'Saw_River_S4', 'Saw_River_S5', 'Saw_River_S6',
'S1_shows?', 'S2_shows?', 'S3_shows?', 'S4_shows?', 'S5_shows?', 'S6_shows?',
'Winner?_S1', 'Winner?_S2', 'Winner?_S3', 'Winner?_S4', 'Winner?_S5', 'Winner?_S6',
'W/L_amount_S1', 'W/L_amount_S2', 'W/L_amount_S3', 'W/L_amount_S4', 'W/L_amount_S5', 'W/L_amount_S6',
'Pot',
'Rake']


def parseHandFile(filename):
    global writer
    file = open(filename,'r', encoding = 'utf-8')
    for line in file:
        myStr = line.strip()
       # print(myStr)
        if ("PokerStars" in myStr):          
            if myState != 0:
               gmAry = makeGameArray()
               writer.writerow(gmAry) 
        ### Write to CSV ###
            initGame()
        setState(myStr) 
       # print(myStr + ":   " + str(myState))   
        if myState == 1: 
            setSeats(myStr)
            setChipCount(myStr)
            setSoft(myStr)
            setHandID(myStr)
            setBlinds(myStr)
            setDay(myStr)
#            setHour(myStr)
            setTableName(myStr)
            setPosVec(myStr)
#            setPositionsBTN(myStr)
        if myState == 2:
            setPotSize(myStr)
        if myState == 3:
#            setBets3(myStr)
            setRaises3(myStr)
            setCalls3(myStr)
            setPotSize(myStr)
        if myState == 4:
            setBets4(myStr)
            setRaises4(myStr)
            setCalls4(myStr)
            setSawFLOP(myStr)
            setPotSize(myStr)
        if myState == 5:
            setBets5(myStr)
            setRaises5(myStr)
            setCalls5(myStr)
            setSawTURN(myStr)
            setPotSize(myStr)
        if myState == 6:
            setBets6(myStr)
            setRaises6(myStr)
            setCalls6(myStr)
            setSawRIVER(myStr)
            setPotSize(myStr)
        if myState == 7:
            setSawSD(myStr)
        if myState == 8:
            setPotSize(myStr)
            setRake(myStr)
            setWinner(myStr)
            setWinnings()
#            setPosVec()



def main():
    global writer
    f = open('2017_2018_6pl.csv', 'w', encoding = 'utf_8_sig')
    writer = csv.writer(f)
    writer.writerow(header)
    listy = glob.glob('**/./*.txt', recursive = True)#**/
    for file in listy:
        try:
            print(file)
            parseHandFile(file)
        except:
            continue
    f.close()

main()


