width = int(input('Ширина: '))
length = int(input('Длина: '))
height = int(input('Высота: '))
result = 'Стандартная коробка №3'
if width < 15 and length < 15 and height < 15:
    result = 'Коробка №1'
elif width < 50 and length < 50 and height < 50:
    result = 'Коробка №2'
elif length >= 200:
    result = 'Упаковка для лыж'

print(result)
