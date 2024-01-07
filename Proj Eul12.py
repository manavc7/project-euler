import math

factor_list = []
def triangles(n):
	return ((n+1)*(n)/2);


for k in range(7,700000):
    factor_list = []
    factor_list.append(1)
    factor_list.append(triangles(k))
    for j in range(1,int(math.sqrt(triangles(k)))+1):
        if (not triangles(k)%j):
            factor_list.append(j)
            factor_list.append(triangles(k)/j)
    if len(factor_list) > 500:
        print(triangles(k))
        break
    else:
        factor_list.clear()

print("end")