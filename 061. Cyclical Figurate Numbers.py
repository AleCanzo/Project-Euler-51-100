def list_num():
    list_tri = []
    list_sq = []
    list_pent = []
    list_hex = []
    list_hept =[]
    list_oct = []

    for n in range(45, 141):
        list_tri.append(int(n*(n + 1)/2))
        
    for n in range(32, 100):
        list_sq.append(int(pow(n,2)))
        
    for n in range(26, 82):
        list_pent.append(int(n*(3*n - 1)/2))

    for n in range(23, 71):
        list_hex.append(int(n*(2*n - 1)))
        
    for n in range(21, 64):
        list_hept.append(int(n*(5*n - 3)/2))
        
    for n in range(19, 59):
        list_oct.append(int(n*(3*n - 2)))
        
    return list_tri, list_sq, list_pent, list_hex, list_hept, list_oct

def match_tri(x):
    for y in list_tri:
        y = str(y)
        if x == y[0:2]:
            return y
    return 0
def match_sq(x):
    for y in list_sq:
        y = str(y)
        if x == y[0:2]:
            return y
    return 0
def match_pent(x):
    for y in list_pent:
        y = str(y)
        if x == y[0:2]:
            return y
    return 0
def match_hex(x):
    for y in list_hex:
        y = str(y)
        if x == y[0:2]:
            return y
    return 0
def match_hept(x):
    for y in list_hept:
        y = str(y)
        if x == y[0:2]:
            return y
    return 0
def match_oct(x):
    for y in list_oct:
        y = str(y)
        if x == y[0:2]:
            return y
    return 0


def f(list_tri, list_sq, list_pent, list_hex, list_hept, list_oct, l):
    print(l)
    
    if len(list_sq) != 0 and l != []:
        x = l[-1]
        y = match_sq(x[2:4])
        if y != 0:
            l.append(y)
            print("sq", y)
            l = f(list_tri, [], list_pent, list_hex, list_hept, list_oct, l)
            if len(l) == 6 and (list_sq != [] or list_pent != [] or list_hex != [] or list_hept != [] or list_oct != []):
                print("pre-pop", l)
                l.pop()
                print("after-pop", l)
                return l
            elif len(l) == 6:
                print("eccoci qua", l)
                return l
            
    if len(list_pent) != 0 and l != []:
        x = l[-1]
        y = match_pent(x[2:4])
        if y != 0:
            l.append(y)
            print("pent", y)
            l = f(list_tri, list_sq, [], list_hex, list_hept, list_oct, l)
            if len(l) == 6 and (list_sq != [] or list_pent != [] or list_hex != [] or list_hept != [] or list_oct != []):
                print("pre-pop", l)
                l.pop()
                print("after-pop", l)
                return l
            elif len(l) == 6:
                print("eccoci qua", l)
                return l
            
    if len(list_hex) != 0 and l != []:
        x = l[-1]
        y = match_hex(x[2:4])
        if y != 0:
            l.append(y)
            print("hex", y)
            l = f(list_tri, list_sq, list_pent, [], list_hept, list_oct, l)
            if len(l) == 6 and (list_sq != [] or list_pent != [] or list_hex != [] or list_hept != [] or list_oct != []):
                print("pre-pop", l)
                l.pop()
                print("after-pop", l)
                return l
            elif len(l) == 6:
                print("eccoci qua", l)
                return l
            
    if len(list_hept) != 0 and l != []:
        x = l[-1]
        y = match_hept(x[2:4])
        if y != 0:
            l.append(y)
            print("hept", y)
            l = f(list_tri, list_sq, list_pent, list_hex, [], list_oct, l)
            if len(l) == 6 and (list_sq != [] or list_pent != [] or list_hex != [] or list_hept != [] or list_oct != []):
                print("pre-pop", l)
                l.pop()
                print("after-pop", l)
                return l
            elif len(l) == 6:
                print("eccoci qua", l)
                return l
            
    if len(list_oct) != 0 and l != []:
        x = l[-1]
        y = match_oct(x[2:4])
        if y != 0:
            l.append(y)
            print("oct", y)
            l = f(list_tri, list_sq, list_pent, list_hex, list_hept, [], l)
            if len(l) == 6 and (list_sq != [] or list_pent != [] or list_hex != [] or list_hept != [] or list_oct != []):
                print("pre-pop", l)
                l.pop()
                print("after-pop", l)
                return l
            elif len(l) == 6:
                print("eccoci qua", l)
                return l
            
    if len(l) == 6:
        #print("eccoci qui")
        return l
    
    return []
  
def is_solution(state):
    if state[0][3:] == [True, True, True, True, True, True]:
        return True
    else:
        return False
 
def possible_choice(state):
    i = 0
    for bool in state[0]:
        if bool == False:
            case:
                i = 0:
                    
     
def backtracking(state):
    if is_solution(state):
        return state
    for choice in possible_choice(state):
        
    
    
    
if __name__ == "__main__":
    list = [list_num()]
    # Definisco la lista state come una lista di liste: la prima lista ha True o False nella posizione equivalente alla quadrupla usata 
    # e la seconda tiene traccia delle scelte fatte 
    state = [[False, False, False, False, False, False], [0, 0, 0, 0, 0, 0], list]
    solution = backtracking(state)[1]
    
    