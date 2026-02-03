import numpy as np

CT = np.loadtxt("0059_cipher.txt", dtype=int, delimiter=",")

def PT(CT, key):
    data = np.copy(CT)
    j = 0
    for i in range(len(data)):
        j = i % 3
        data[i] = data[i] ^ key[j]
    PL = ''.join(chr(n) if chr(n).isprintable() else '.' for n in data)
    
    words = ["the", "and", "that", "this", "is", "of", "to", "in"]
    match = [w for w in words if w in PL.lower()]
    if len(match)>=8:
        print(key,":")
        print(PL.lower())
        sum = 0
        for i in PL:
            sum = sum + ord(i)
        print(sum)
        


for x in range(97, 123):
    for y in range(97, 123):
        for z in range(97, 123):
            key = [x, y, z]
            PT(CT, key)
           




    
     


            
