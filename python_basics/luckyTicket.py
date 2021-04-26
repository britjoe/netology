number = input()
sum1 = 0
sum2 = 0
for i in range(len(number)):
    if i < 3:
        sum1 += int(number[i])
    else:
        sum2 += int(number[i])

if sum1 == sum2:
    print('Счастливый билет')
else:
    print('Неасчастливый билет')
