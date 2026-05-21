def totient(n):
    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n

    return result

if __name__=="__main__":
    sum = 0
    for n in range(2, 1_000_001):
        #print(n)
        sum += totient(n)
        
    print(sum)
