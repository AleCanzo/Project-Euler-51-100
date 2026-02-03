import math

print(sum(sum(int(c) for c in str(math.isqrt(i * 100**100))[ : 100]) for i in range(100) if math.isqrt(i)**2 != i))
