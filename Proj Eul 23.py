def divisor_sum(num):
    divisors = []
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors)

abundant_nums = [i for i in range(1, 28124) if i < divisor_sum(i)]

sum_list = [0] * 28124

for i in range(len(abundant_nums)):
    for j in range(i, len(abundant_nums)):
        if abundant_nums[i] + abundant_nums[j] < 28124:
            sum_list[abundant_nums[i] + abundant_nums[j]] = 1

not_sum_list = [i for i in range(1, 28124) if sum_list[i] == 0]

result = sum(not_sum_list)
print(result)