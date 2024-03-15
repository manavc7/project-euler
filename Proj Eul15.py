import math
def lattice_paths(m,n):
    num_paths = math.factorial(m+n)/(math.factorial(m)*math.factorial(n))

    return(num_paths)

print(lattice_paths(20,20))