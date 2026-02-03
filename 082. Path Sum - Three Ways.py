from math import inf

def read_file(f):
    with open(f, 'r') as f:
        l = [[int(num) for num in line.split(',')] for line in f]
    return l

def min_node_weight(UNVISITED, PATH_WEIGHT):
    min = inf
    for v in UNVISITED:
        x , y = v
        if PATH_WEIGHT[x][y] < min:
            min = PATH_WEIGHT[x][y]
            u = v
    return u
        
def node_neighbours(u, N):
    x, y = u
    if x+1 == N:
        if y+1 == N: 
            return [(x-1, y)]
        else:
            return [(x, y+1), (x-1, y)]
    elif y+1 == N:
        if x+1 == N:
            return [(x-1, y)]
        elif x == 0:
            return [(x+1, y)]
        else:
            return [(x+1, y), (x-1, y)]
    else:
        if x != 0:
            return [(x+1, y), (x, y+1), (x-1, y)]
        else:
            return [(x+1, y), (x, y+1)]

def min_path_left_to_right(N, x):
    
    f = "0081_matrix.txt"
    NODE_WEIGHT = read_file(f)
    UNVISITED = []
    PATH_WEIGHT = []
    for i in range(N):
        l = []
        for j in range(N):
            l.append(inf)
            UNVISITED.append((i,j))
        PATH_WEIGHT.append(l)
        
    PATH_WEIGHT[x][0] = NODE_WEIGHT[x][0]
    while len(UNVISITED) != 0:
        u = min_node_weight(UNVISITED, PATH_WEIGHT)
        neighbours = node_neighbours(u, N)
        for v in neighbours:
            vx , vy = v
            ux, uy = u
            d = PATH_WEIGHT[ux][uy] + NODE_WEIGHT[vx][vy]
            if d < PATH_WEIGHT[vx][vy]:
                PATH_WEIGHT[vx][vy] = d
        UNVISITED.remove(u)
    
    min = inf
    for x in range(N):
        if PATH_WEIGHT[x][N-1] < min:
            min = PATH_WEIGHT[x][N-1]
    return min
    
if __name__ =="__main__":
    min = inf
    N = 80
    for x in range(N):
        min_path = min_path_left_to_right(N, x)
        if min_path < min:
            min = min_path
    print(min)
        
        
    