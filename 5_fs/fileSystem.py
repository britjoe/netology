import json

purch_dict = dict()
with open('purchase_log.txt', 'r', encoding='UTF-8') as log:
    headers_log = list(json.loads(log.readline().strip()).keys())
    for line in log:
        line = line.strip()
        purch_dict[json.loads(line)[headers_log[0]]] = json.loads(line)[headers_log[1]]

with open('visit_log.csv', 'r', encoding='UTF-8') as visit:
    with open('funnel.csv', 'w', encoding='UTF-8') as fun:
        for line in visit:
            line = line.strip().split(',')
            purchase = purch_dict.get(line[0])
            if purchase:
                line.append(purchase)
                fun.write(', '.join(line) + '\n')
