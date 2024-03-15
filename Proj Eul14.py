def collatz_counter(n):
    c = 1
    while n != 1:
        if n%2==0:
            n = n/2
        else: 
            n = (3*n) + 1
        c += 1   
    return c
chains = 0
def find_longest_chain(limit):
    max_length = 0
    starting_num = 0
    for i in range(1,limit):
        current_length = collatz_counter(i)
        if current_length > max_length:
            max_length = current_length
            starting_num = i
    return starting_num, max_length

limit = 1000000

result = find_longest_chain(limit)
print(result[0])