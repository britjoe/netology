print('Введите день:')
day = input().zfill(2)

print('Введите месяц:')
month = input()

zodiac = str()

month_dict = {
    'Январь': '01',
    'Февраль': '02',
    'Март': '03',
    'Апрель': '04',
    'Май': '05',
    'Июнь': '06',
    'Июль': '07',
    'Август': '08',
    'Сентябрь': '09',
    'Октбярь': '10',
    'Ноябрь': '11',
    'Декабрь': '12'
}
date = month_dict.get(month) + day
if date <= '0119':
    zodiac = 'Козерог'
elif date <= '0218':
    zodiac = 'Водолей'
elif date <= '0320':
    zodiac = 'Рыбы'
elif date <= '0419':
    zodiac = 'Овен'
elif date <= '0520':
    zodiac = 'Телец'
elif date <= '0620':
    zodiac = 'Близнецы'
elif date <= '0722':
    zodiac = 'Рак'
elif date <= '0822':
    zodiac = 'Лев'
elif date <= '0922':
    zodiac = 'Дева'
elif date <= '1022':
    zodiac = 'Весы'
elif date <= '1121':
    zodiac = 'Скорпион'
elif date <= '1221':
    zodiac = 'Стрелец'
else:
    zodiac = 'Козерог'
print('Ваш знак зодиака: ' + zodiac)
