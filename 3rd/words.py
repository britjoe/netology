queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

analyse_dict = dict()

for i in queries:
    if analyse_dict.get(len(i.split())) is None:
        analyse_dict[len(i.split())] = 1
    else:
        analyse_dict[len(i.split())] += 1

analyse_dict_sorted = dict(sorted(analyse_dict.items(), key=lambda item: item[1]))

total_words_quantity = len(queries)
for i in analyse_dict_sorted:
    result = round((analyse_dict_sorted[i] / total_words_quantity) * 100, 2)
    print(f'Поисковых запросов, содержащих {i} слов(а): {result}%')


