year = int(input())
result = "Обычный год"
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = 'Високосный год'
print(result)
