import math

file = "0099_base_exp.txt"

with open(file, "r") as f:
    powers = []
    bases = []
    i = 0
    for line in f:
        line.strip()
        x, y = line.split(",")
        bases.append(int(x.strip()))
        powers.append(int(y.strip()))

max = 0
for n in range(len(bases)):
    x = powers[n]*math.log(bases[n])
    if x > max:
        max = x
        max_line = n + 1
        
print(max, max_line)


