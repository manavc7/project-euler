a = 0
b = 0
import math

for i in range(1,500):
    for k in range(1,500):
        product = ((i**2) + (k**2))
        x = (product**0.5)
        if x.is_integer():
            c = x
            a = i
            b = k
            if a+b+c == 1000 and a<b<c:
                print(a*b*c)