def sum_divisors(n):
    list_divisor = []
    for i in range(1,n):
        if n%i==0:
            list_divisor.append(i)
    
    return sum(list_divisor)

def amicable_sum(limit):
    list_amicable = []
    for i in range(1,limit):
        if sum_divisors(sum_divisors(i)) == i and i != sum_divisors(i):
            if i not in list_amicable and sum_divisors(i) not in list_amicable:
                list_amicable.append(i)
                list_amicable.append(sum_divisors(i))
    return sum(list_amicable)

print(amicable_sum(10000))

