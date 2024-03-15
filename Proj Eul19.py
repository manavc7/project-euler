length_months = [31,28,31,30,31,30,31,31,30,31,30,31]
week = 2
c = 0
for i in range(1,101):
    if i%4==0:
        length_months[1] = 29
    else:
        length_months[1] = 28
    for k in range(12):
        week += length_months[k]
        if week%7==0:
            c += 1

print(c)