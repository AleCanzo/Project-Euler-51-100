def search_perm(x, l, list_perm):
    x_list = list(map(int, str(x)))
    for y in l:
        y_list = list(map(int, str(y)))
        if y != x and sorted(x_list) == sorted(y_list) and y not in list_perm:
            list_perm.append(y)
    return list_perm
            
        
if __name__ == "__main__":
    
    l = []
    for x in range(300, 10000):
        y = pow(x, 3)
        l.append(y)
        
    for x in l:
        list_perm = search_perm(x, l, [x])
        if len(list_perm) not in [0,1,2]:
            print(list_perm)