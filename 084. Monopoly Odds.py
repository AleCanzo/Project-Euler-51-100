import random
import numpy as np

def next_r(position):
    r = 100
    i = 1
    while r == 100:
        if board[(position + i) % 40][0] == "R":
            r = (position + i) % 40
            return r
        i += 1 

def next_u(position):
    r = 100
    i = 1
    while r == 100:
        if board[(position + i) % 40][0] == "U":
            r = (position + i) % 40 
            return r
        i += 1        

board = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]
"""community_chest = ["GO", "JAIL"] #2/16
chance = ["GO", "JAIL", "C1", "E3", "H2", "R1", "R", "R", "U", "U", "-3"] #10/16"""
squares = np.zeros(40, dtype=int)

roll = 0
position = 0
couple = 0
N = 1000000

community_chest = list(range(1, 17))
random.shuffle(community_chest)
#print(community_chest)
chance = list(range(1, 17))
random.shuffle(chance)
#print(chance)
dice = list(range(1, 5))
#print(dice)


while roll != N:
    dices = [random.choice(dice), random.choice(dice)]
    #print(dices)
    if dices[0] == dices[1]:
        couple += 1
        if couple == 3:
            position = 10
            couple = 0
            squares[position] += 1
            roll += 1
            continue
    else:
        couple = 0

    
    position = (position + sum(dices)) % 40
    
    #CC
    if position == 2 or position == 17 or position == 33: 
        #print("CC")
        card = community_chest.pop(0)
        community_chest.append(card)
        #print(card, community_chest)
        if card == 1:
            position = 0
        elif card == 2:
            position = 10

    
    #CH
    elif position == 7 or position == 22 or position == 36: 
        #print("CH")
        card = chance.pop(0)
        chance.append(card)
        #print(card, chance)
        if card == 1:
            position = 0
        elif card == 2:
            position = 10
        elif card == 3:
            position = 11
        elif card == 4:
            position = 24
        elif card == 5:
            position = 39
        elif card == 6:
            position = 5
        elif card == 7 or card == 8:
            position = next_r(position)
        elif card == 9:
            position = next_u(position)
        elif card == 10:
            position = (position - 3) % 40
         
    elif position == 30:
        position = 10
           
               
    #print(position)
    squares[position] += 1
    roll += 1

#print(squares)

perc = (squares / N) * 100
#print(perc)

indices_top3 = np.argsort(perc)[-3:][::-1]
top3 = perc[indices_top3]

print(indices_top3, top3)
