from math import factorial as fact

def sum_fact(n):
    n_str = str(n)
    sum = 0
    for i in range(len(n_str)):
        sum += fact(int(n_str[i]))
    return sum

if __name__ == "__main__":
    c = 0
    for n in range(2,1_000_001):
        l = []
        l.append(n)
        x = n
        while True:
            y = sum_fact(x)
            if y not in l:
                l.append(y)
                x = y
            else:
                if len(l) == 60:
                    c += 1
                break
    print(c)
        