def is_palindrome(n):
    s = list(str(n))
    while len(s)>1:
        if s[0] == s[-1]:
            s.pop(0)
            s.pop(-1)
        else:
            return False
    if len(s) == 1 or len(s) == 0:
        return True

def is_lychrel(n):
    for i in range(50):
        rev_n = int(str(n)[::-1])
        #print("n = {}, rev_n = {}".format(n, rev_n))
        n = n + rev_n
        #print(n) 
        if is_palindrome(n):
            return False
    return True

c = 0
for n in range(10, 10001):
    #print(n,":")
    if is_lychrel(n) == True:
        print(n)
        c += 1
print(c)