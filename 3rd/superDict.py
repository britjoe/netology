my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict = {'a': {'b': {'c': {'d': {'e': 'f'}}}}}

result = dict()

for i in range(len(my_list)-1, -1, -1):
    result[1] = i

print(result)
