cook_book = {
    'салат': [
        {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
        {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
        {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
        {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
    'пицца': [
        {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
    'лимонад': [
        {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
        {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
        {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}

cnt = int(input('Введите количество порций: '))

temp = []
result = []
for meal, rec in cook_book.items():
    temp = temp + rec

temp_2 = dict()
for product in temp:
    ingridient_name, quantity, measure = product.values()
    if temp_2.get((ingridient_name, measure)) is None:
        temp_2.update({(ingridient_name, measure): quantity})
    else:
        temp_2[(ingridient_name, measure)] += quantity
for item in temp_2:
    print(f'{item[0].capitalize()}: {temp_2.get(item)} {item[1]}')
