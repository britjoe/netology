my_list = ['a', 'b', 'c', 'd', 'e', 'f']

my_list.reverse()
prev_val = None
for i in my_list:
    temp_dict = dict()
    result = dict()
    if prev_val is None:
        prev_val = i
    else:
        temp_dict.update({i: prev_val})
        prev_val = temp_dict.copy()
        result.clear()
        result.update({i: temp_dict.get(i)})

print(result)
