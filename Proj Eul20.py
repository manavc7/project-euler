import math 
num = str(math.factorial(100))
list_num = list(map(lambda x: int(x), list(num)))
print(sum(list_num))