
primes = []
for i in range(20000):
    c = 0
    for j in range(1,i):
        if i%j==0:
            c += 1
    if c==1:
        primes.append(i)
prime_sum = sum(primes)
print(prime_sum)