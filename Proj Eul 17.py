def total_letters(limit):  
    numbers_1 = ["one","two","three","four",'five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    numbers_2 = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    numbers_3 = ['onehundred','twohundred','threehundred','fourhundred','fivehundred','sixhundred','sevenhundred','eighthundred','ninehundred']
    num_list = []

    for i in range(19):
        num_list.append(numbers_1[i])
    
    
    for i in range(8):
        num_list.append(numbers_2[i])
        for k in range(9):
            num_list.append(numbers_2[i]+numbers_1[k])


    
    for i in range(9):
        for k in range(19):
            num_list.append(numbers_3[i]+'and'+numbers_1[k])
        
    for i in range(9):
        num_list.append(numbers_3[i])
        for k in range(8):
            num_list.append(numbers_3[i]+'and'+numbers_2[k])
            for j in range(9):
                num_list.append(numbers_3[i]+'and'+numbers_2[k]+numbers_1[j])

    num_list.append('onethousand')       

    total_length = 0
    for i in range(limit):
        total_length += len(num_list[i])

    return total_length

print(total_letters(1000))

