def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [i for i in range(2, limit + 1) if primes[i]]

def sum_of_primes_below(limit):
    primes = sieve_of_eratosthenes(limit)
    return sum(primes)

# Find the sum of all primes below two million
result = sum_of_primes_below(2000000)
print(result)
