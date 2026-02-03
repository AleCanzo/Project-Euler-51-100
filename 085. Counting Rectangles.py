     
dist = 10000000
for N in range(250):
    for M in range(250): 
        c = int((((N+1)*N)/2)*(((M+1)*M)/2))      
        if abs(c-2_000_000) < dist:
            min_N = N
            min_M = M
            dist = abs(c-2_000_000)
            print(dist, N, M)

