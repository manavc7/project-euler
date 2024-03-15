def digit_sum(n):
    num = str((2**n))
    list_num = list(map(lambda x: int(x), list(num)))
    return sum(list_num)

print(digit_sum(1000))
