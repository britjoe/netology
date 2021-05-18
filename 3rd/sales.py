stats = {'facebook': 55,
         'yandex': 115,
         'vk': 120,
         'google': 120,
         'email': 42,
         'ok': 98}

max_value = 0

for i in stats:
    if max_value < stats[i]:
        max_value = stats[i]

channel_list = []
for channel, values in stats.items():
    if max_value == values:
        channel_list.append(channel)
print(f' Максимальный объем продаж на рекламном канале: {", ".join(channel_list)}')
