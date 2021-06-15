import re


def car_number_check(car_num):
    pattern = r'^([АВЕКМНОРСТУХABEKMHOPCTYX]{1}\d{3}[АВЕКМНОРСТУХABEKMHOPCTYX]{2})(\d{2,3})$'
    result = re.findall(pattern, car_num)
    return result


def delete_dublicates(string):
    pattern = r'(?!\S)(\s\w+)(?=\s)\1+'
    result = re.sub(pattern, r'\1', string)
    return result


def make_acronym(string):
    pattern = r"(?<!\S)\w"
    result = ''.join(re.findall(pattern, string)).upper()
    return result


def count_domains(list_of_emails):
    domains = list(map(lambda item: re.search(r'(?!@)\w+\.\w+', item).group(), list_of_emails))
    domains_count = dict()
    for i in set(domains):
        domains_count[i] = domains.count(i)
    return domains_count


car_num = 'АБ22ВВ193'
car_num_checked = car_number_check(car_num)

if car_num_checked:
    print(f"Номер {car_num_checked[0][0]} валиден. Регион: {car_num_checked[0][1]}")
else:
    print("Номер не валиден")

some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные ' \
              'повторы слов из из из из заданной строки строки при помощи регулярных выражений. '

print(delete_dublicates(some_string))

print(make_acronym('Python is cool'))

emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']
dict_of_domains = count_domains(emails)
for i in dict_of_domains:
    print(f'{i}: {dict_of_domains[i]}')
