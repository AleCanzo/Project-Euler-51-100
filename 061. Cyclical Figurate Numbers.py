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
  
def is_solution(state_dict):
    if state_dict[0:]["state"][0] == [True, True, True, True, True, True]:
        return True
    else:
        return False
 
def possible_choice(state_dict):
    choices = {}
    for bool, i in enumerate(state_dict[0:]["state"][0]):
        if bool == False:
            choices.append(state_dict[i])
    return choices
                    
     
def backtracking(state_dict, list_numbers):
    if is_solution(state_dict):
        return state_dict
    for choice, i in enumerate(possible_choice(state_dict)):
        
        if len(choice) == 6:
            choice[0]["state"][0] = True
            for num in choice[0]["list_num"]:
                choice[0]["state"][1] = num
                result = backtracking(choice)
                if result == True:
                    return result
        
        for m in len(choice):
            for n in choice[m]["list_num"]:
                
            
        return
    
    
    
if __name__ == "__main__":
    list_tri, list_sq, list_pent, list_hex, list_hept, list_oct = list_num()
    #state: (null, 0), (done, numero scelto), (progress, numero scelto), (chosen)
    state_dict = {
        {
            "type": 3,
            "state": [False, 0],
            "list_num": list_tri
        },
        {
            "type": 4,
            "state": [False, 0],
            "list_num": list_sq
        },
        {
            "type": 5,
            "state": [False, 0],
            "list_num": list_pent
        },
        {
            "type": 6,
            "state": [False, 0],
            "list_num": list_hex
        },
        {
            "type": 7,
            "state": [False, 0],
            "list_num": list_hept
        },
        {
            "type": 8,
            "state": [False, 0],
            "list_num": list_oct
        }
    }
    solution = backtracking(state_dict)
    
    