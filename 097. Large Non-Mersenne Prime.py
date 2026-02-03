import sys

sys.set_int_max_str_digits(0)
n = 28433 * pow(2, 7830457) + 1
s = str(n)
print(s[len(s)-10:len(s)])