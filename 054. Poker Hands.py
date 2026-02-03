import numpy as np

def load_hands(N, file):
    hands = np.loadtxt(file, dtype='U2')
    p1 = np.zeros((N, 5), dtype='U2')
    p2 = np.zeros((N, 5), dtype='U2')
    for i in range(N):
        p1[i] = hands[i][0:5]
        p2[i] = hands[i][5:10]
    return (hands, p1, p2)
    
def same_suit(hand):
    c = 0
    suit = hand[0][1]
    for i in range(len(hand)):
        if hand[i][1]==suit:
            c += 1
    return c

def same_value(hand):
    l = np.zeros(5, dtype=str)
    dict = {'1': 0 , '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,  '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}    
    for i in range(len(hand)):
        l[i] = (hand[i][0])
        dict[hand[i][0]] = dict[hand[i][0]] + 1
    l = np.unique(l).tolist()
    c = []
    for x in l:
        c.append(dict[x]) 
    c = np.array(c)
    return c

def royal_flush(hand):
    l = []
    if same_suit(hand) != 5:
        return False
    for i in range(len(hand)):
        l.append(hand[i][0])
    if set(l) != set(['T','J','Q','K','A']):
        return False
    return True

def straight_flush(hand):
    if same_suit(hand) == 5 and straight(hand):
        return True
    else:
        return False

def four_of_a_kind(hand):
    if 4 not in same_value(hand):
        return False
    else:
        return True
    
def full_house(hand):
    c_hand = hand[:]
    dict_values = {'1': 0 , '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,  '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0} 
    dict_suit = {'H': 0, 'D': 0, 'S': 0, 'C': 0}   
    for i in range(len(hand)):
        dict_values[hand[i][0]] = dict_values[hand[i][0]] + 1
        dict_suit[hand[i][1]] = dict_suit[hand[i][1]] + 1
    val = [k for k, v in dict_values.items() if v == 3]
    if val == []:
        return False
    else: 
        val = val[0]
        print(val)
        for i in range(len(c_hand)-1, -1, -1):
            if c_hand[i][0] == val:
                c_hand = np.delete(c_hand, i)
        if len(c_hand) == 2:
            if c_hand[0][0] == c_hand[1][0]:
                return True
        else:
            return False

def flush(hand):
    if same_suit(hand)!=5:
        return False
    return True
 
def straight(hand):
    l = []
    for i in range(len(hand)):
        l.append(hand[i][0])
    if set(l) == set(['T','J','Q','K','A']):
        return True
    elif set(l) == set(['5','4','3','2','A']):
        return True
    if 'A' not in l:
        mapping = {"T": '10', "J": '11', "Q": '12', "K": '13'}
        l = [mapping.get(c, c) for c in l]
        l = list(map(int, l))
        l.sort()
        if l == list(range(min(l), max(l)+1)):
            return True
    return False
  
def three_of_a_kind(hand):
    if 3 in same_value(hand):
        return True
    else:
        return False

def two_pairs(hand):
    if np.count_nonzero(same_value(hand) == 2) == 2:
        return True
    else:
        return False

def one_pair(hand):
    if 2 in same_value(hand):
        return True
    else:
        return False
    
def high_card(hand):
    mapping = {"T": '10', "J": '11', "Q": '12', "K": '13', "A": '14'}
    l = []
    for i in range(len(hand)):
        l.append(hand[i][0])
    l = [mapping.get(c, c) for c in l]
    l = list(map(int, l))
    return max(l)

def rank(hand):
    if royal_flush(hand):
        return 9
    elif straight_flush(hand):
        return 8
    elif four_of_a_kind(hand):
        return 7
    elif full_house(hand):
        return 6
    elif flush(hand):
        return 5
    elif straight(hand):
        return 4
    elif three_of_a_kind(hand):
        return 3
    elif two_pairs(hand):
        return 2
    elif one_pair(hand):
        return 1
    else:
        return 0 
    
def tie_break(hand1, hand2, rank):
    
    if rank == 9:
        return 0
    
    if rank == 8:
        if high_card(hand1) > high_card(hand2):
            return 1
        if high_card(hand1) < high_card(hand2):
            return 2
        else:
            while len(hand1)!=0:
                hand1.remove(high_card(hand1))
                hand2.remove(high_card(hand2))
                if high_card(hand1) > high_card(hand2):
                    return 1
                if high_card(hand1) < high_card(hand2):
                    return 2
            return 0
        
    if rank == 7:  
        dict = {1: 0 , 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
        mapping = {"T": 10, "J": 11, "Q": 12, "K": 13, 'A': 14}
        dict1 = {int(mapping.get(k, k)): v for k, v in dict.items()}  
        dict2 = {int(mapping.get(k, k)): v for k, v in dict.items()}  
        l1 = []
        l2 = []
        for i in range(5):
            #print(hand1[i][0], hand2[i][0])
            l1.append(hand1[i][0])
            l2.append(hand2[i][0])    
        l1 = [mapping.get(c, c) for c in l1]
        l1 = list(map(int, l1))
        l2 = [mapping.get(c, c) for c in l2]
        l2 = list(map(int, l2))            
        for i in range(len(hand1)):
            #print(l1[i], l2[i])
            dict1[l1[i]] = dict1[l1[i]] + 1
            dict2[l2[i]] = dict2[l2[i]] + 1
        k1 = max(dict1, key=dict1.get)   
        k2 = max(dict2, key=dict2.get)     
        #print("dict1={}, k1={}, val1={} \ndict2={}, k2={}, val2={}".format(dict1, k1, val1, dict2, k2, val2))
        if k1 > k2:
            return 1    
        elif k1 < k2:
            return 2
    
    if rank == 6:
        dict = {1: 0 , 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
        mapping = {"T": 10, "J": 11, "Q": 12, "K": 13, 'A': 14}
        dict1 = {int(mapping.get(k, k)): v for k, v in dict.items()}  
        dict2 = {int(mapping.get(k, k)): v for k, v in dict.items()}  
        l1 = []
        l2 = []
        for i in range(5):
            #print(hand1[i][0], hand2[i][0])
            l1.append(hand1[i][0])
            l2.append(hand2[i][0])    
        l1 = [mapping.get(c, c) for c in l1]
        l1 = list(map(int, l1))
        l2 = [mapping.get(c, c) for c in l2]
        l2 = list(map(int, l2))            
        for i in range(len(hand1)):
            #print(l1[i], l2[i])
            dict1[l1[i]] = dict1[l1[i]] + 1
            dict2[l2[i]] = dict2[l2[i]] + 1
        k1 = max(dict1, key=dict1.get)   
        k2 = max(dict2, key=dict2.get)     
        #print("dict1={}, k1={}, val1={} \ndict2={}, k2={}, val2={}".format(dict1, k1, val1, dict2, k2, val2))
        if k1 > k2:
            return 1    
        elif k1 < k2:
            return 2
    
    if rank == 5:
        if high_card(hand1) > high_card(hand2):
            return 1
        if high_card(hand1) < high_card(hand2):
            return 2
        else:
            while len(hand1)!=0:
                hand1.remove(high_card(hand1))
                hand2.remove(high_card(hand2))
                if high_card(hand1) > high_card(hand2):
                    return 1
                if high_card(hand1) < high_card(hand2):
                    return 2
            return 0

    if rank == 4:
        if high_card(hand1) > high_card(hand2):
            return 1
        if high_card(hand1) < high_card(hand2):
            return 2
        else:
            while len(hand1)!=0:
                hand1.remove(high_card(hand1))
                hand2.remove(high_card(hand2))
                if high_card(hand1) > high_card(hand2):
                    return 1
                if high_card(hand1) < high_card(hand2):
                    return 2
            return 0

    if rank == 3:
        dict = {1: 0 , 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
        mapping = {"T": 10, "J": 11, "Q": 12, "K": 13, 'A': 14}
        dict1 = {int(mapping.get(k, k)): v for k, v in dict.items()}  
        dict2 = {int(mapping.get(k, k)): v for k, v in dict.items()}  
        l1 = []
        l2 = []
        for i in range(5):
            #print(hand1[i][0], hand2[i][0])
            l1.append(hand1[i][0])
            l2.append(hand2[i][0])    
        l1 = [mapping.get(c, c) for c in l1]
        l1 = list(map(int, l1))
        l2 = [mapping.get(c, c) for c in l2]
        l2 = list(map(int, l2))            
        for i in range(len(hand1)):
            #print(l1[i], l2[i])
            dict1[l1[i]] = dict1[l1[i]] + 1
            dict2[l2[i]] = dict2[l2[i]] + 1
        k1 = max(dict1, key=dict1.get)   
        k2 = max(dict2, key=dict2.get)     
        #print("dict1={}, k1={}, val1={} \ndict2={}, k2={}, val2={}".format(dict1, k1, val1, dict2, k2, val2))
        if k1 > k2:
            return 1    
        elif k1 < k2:
            return 2
        
    if rank == 2:
        dict = {1: 0 , 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
        mapping = {"T": 10, "J": 11, "Q": 12, "K": 13, 'A': 14}
        dict1 = {int(mapping.get(k, k)): v for k, v in dict.items()}  
        dict2 = {int(mapping.get(k, k)): v for k, v in dict.items()}  
        l1 = []
        l2 = []
        for i in range(5):
            l1.append(hand1[i][0])
            l2.append(hand2[i][0])    
        l1 = [mapping.get(c, c) for c in l1]
        l1 = list(map(int, l1))
        l2 = [mapping.get(c, c) for c in l2]
        l2 = list(map(int, l2))            
        for i in range(len(hand1)):
            dict1[l1[i]] = dict1[l1[i]] + 1
            dict2[l2[i]] = dict2[l2[i]] + 1
        k1 = max([k for k, v in dict1.items() if v == 2])   
        k2 = max([k for k, v in dict2.items() if v == 2])     
        #print("dict1={}, k1={} \ndict2={}, k2={}".format(dict1, k1, dict2, k2))
        if k1 > k2:
            return 1    
        elif k1 < k2:
            return 2
        else:
            dict1.pop(k1, None)
            dict2.pop(k2, None)
            k1 = max(dict1, key=dict1.get)   
            k2 = max(dict2, key=dict2.get)    
            if k1 > k2:
                return 1    
            elif k1 < k2:
                return 2
            else:
                dict1.pop(k1, None)
                dict2.pop(k2, None)
                k1 = max(dict1, key=dict1.get)   
                k2 = max(dict2, key=dict2.get)   
                if k1 > k2:
                    return 1    
                elif k1 < k2:
                    return 2 
                else:
                    return 0
        
    if rank == 1:
        dict = {1: 0 , 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
        mapping = {"T": 10, "J": 11, "Q": 12, "K": 13, 'A': 14}
        dict1 = {int(mapping.get(k, k)): v for k, v in dict.items()}  
        dict2 = {int(mapping.get(k, k)): v for k, v in dict.items()}  
        l1 = []
        l2 = []
        for i in range(5):
            #print(hand1[i][0], hand2[i][0])
            l1.append(hand1[i][0])
            l2.append(hand2[i][0])    
        l1 = [mapping.get(c, c) for c in l1]
        l1 = list(map(int, l1))
        l2 = [mapping.get(c, c) for c in l2]
        l2 = list(map(int, l2))            
        for i in range(len(hand1)):
            #print(l1[i], l2[i])
            dict1[l1[i]] = dict1[l1[i]] + 1
            dict2[l2[i]] = dict2[l2[i]] + 1
        k1 = max(dict1, key=dict1.get)   
        k2 = max(dict2, key=dict2.get)     
        print("dict1={}, k1={}, \ndict2={}, k2={}".format(dict1, k1, dict2, k2))
        if k1 > k2:
            return 1    
        elif k1 < k2:
            return 2
        else:
            while len(l1)!=0:
                if max(l1) > max(l2):
                    return 1
                elif max(l1) < max(l2):
                    return 2
                l1.remove(max(l1))
                l2.remove(max(l2))
            return 0
        
    if rank == 0:
        if high_card(hand1) > high_card(hand2):
            return 1
        if high_card(hand1) < high_card(hand2):
            return 2
        else:
            while len(hand1)!=0:
                hand1.remove(high_card(hand1))
                hand2.remove(high_card(hand2))
                if high_card(hand1) > high_card(hand2):
                    return 1
                if high_card(hand1) < high_card(hand2):
                    return 2
            return 0
       
def count_wins_p1(N, p1, p2):
    c = 0
    for i in range(N):
        print("MANO {}:".format(i+1))
        rank_p1 = rank(p1[i])
        rank_p2 = rank(p2[i])
        print("Il giocatore 1 ha la seguente mano {} con valore {}.".format(p1[i], rank_p1))
        print("Il giocatore 2 ha la seguente mano {} con valore {}.".format(p2[i], rank_p2))
        if rank_p1 > rank_p2:
            c += 1
            print("Vince la mano il giocatore 1!")
            print("///////////////////////////////////////////////////////////////////////////")
        elif rank_p1 < rank_p2:
            print("Vince la mano il giocatore 2!")
            print("///////////////////////////////////////////////////////////////////////////")
        else:
            print("Rank pari:")
            tie = tie_break(p1[i], p2[i], rank_p2)
            if tie == 1:
                print("Vince la mano il giocatore 1!")
                print("///////////////////////////////////////////////////////////////////////////")
                c += 1
            elif tie == 2:
                print("Vince la mano il giocatore 2!")
                print("///////////////////////////////////////////////////////////////////////////")
            else:
                print("Pareggio!")
    return c
  
N = 1000 
file = "0054_poker.txt"
(hands, p1, p2) = load_hands(N, file) 
   
c = count_wins_p1(N, p1, p2)

print("Il giocatore 1 ha vinto {} mani.".format(c))
