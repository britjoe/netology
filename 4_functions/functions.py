documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

shelves = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def p_get_owner_by_doc(doc_num):
    owner = None
    for i in documents:
        if doc_num == i.get('number'):
            owner = i.get('name')
    return owner


def s_get_shelf_by_doc(doc_num):
    shelf = None
    for i in shelves:
        if doc_num in shelves[i]:
            shelf = i
    return shelf


def l_show_all_docs():
    for i in documents:
        doc_num = i.get('number')
        doc_type = i.get('type')
        doc_owner = p_get_owner_by_doc(doc_num)
        doc_shelf = s_get_shelf_by_doc(doc_num)
        print(f'№: {doc_num}, тип: {doc_type}, владелец: {doc_owner}, полка хранения: {doc_shelf}')


def ads_add_shelf(new_shelf):
    if new_shelf in shelves.keys():
        print(f'Такая полка уже существует. Текущий перечень полок: {", ".join(shelves.keys())}')
    else:
        shelves.update({new_shelf: []})
        print(f'Полка добавлена. Текущий перечень полок: {", ".join(shelves.keys())}')


def ds_delete_shelf(shelf_num):
    if shelves.get(shelf_num):
        print(
            f'На полке есть документы, удалите их перед удалением полки.'
            f'Текущий перечень полок: {", ".join(shelves.keys())}')
    else:
        shelves.pop(shelf_num)
        print('Полка удалена.'
              f'Текущий перечень полок: {", ".join(shelves.keys())}')


def ad_new_doc(doc_num, doc_type, doc_owner, doc_shelf):
    if doc_shelf not in shelves.keys():
        print('Такой полки не существует. Добавьте полку командой as.')
        print('Текущий список документов:')
        l_show_all_docs()
    else:
        documents.append({
            'type': doc_type,
            'number': doc_num,
            'name': doc_owner
        })
        shelves[doc_shelf].append(doc_num)
        print('Документ добавлен. Текущий список документов:')
        l_show_all_docs()


def d_delete_doc(doc_num):
    for i in shelves:
        if doc_num in shelves.get(i):
            shelves.get(i).remove(doc_num)

    doc_for_delete = None
    for i in documents:
        if doc_num == i.get('number'):
            doc_for_delete = i
            documents.remove(doc_for_delete)

    if doc_for_delete is not None:
        print('Документ удален.\nТекущий список документов:')
    else:
        print('Документ не найден в базе.\nТекущий список документов:')
    l_show_all_docs()


def m_move_doc(doc_num, doc_shelf):
    if doc_shelf not in shelves.keys():
        print(f'Такой полки существует. Текущий перечень полок: {", ".join(shelves.keys())}')
    else:
        if p_get_owner_by_doc(doc_num) is None:
            print('Документ не найден в базе.\nТекущий список документов:')
        else:
            old_shelf = s_get_shelf_by_doc(doc_num)
            shelves.get(old_shelf).remove(doc_num)
            shelves.get(doc_shelf).append(doc_num)
            print('Документ перемещен.\nТекущий список документов:')
        l_show_all_docs()


def input_command():
    command = input('Введите команду: ')
    while command != 'q':
        if command == 'p':
            doc_num = input('Введите номер документа: ')
            owner = p_get_owner_by_doc(doc_num)
            if owner is not None:
                print(f'Владелец документа: {owner}\n')
            else:
                print('Документ не найден в базе')
            input_command()
        elif command == 's':
            doc_num = input('Введите номер документа: ')
            shelf = s_get_shelf_by_doc(doc_num)
            if shelf is not None:
                print(f'Документ хранится на полке: {shelf}\n')
            else:
                print('Документ не найден в базе')
            input_command()
        elif command == 'l':
            l_show_all_docs()
            print()
            input_command()
        elif command == 'ads':
            new_shelf = input('Введите номер полки: ')
            ads_add_shelf(new_shelf)
            input_command()
        elif command == 'ds':
            del_shelf = input('Введите номер полки: ')
            ds_delete_shelf(del_shelf)
            input_command()
        elif command == 'ad':
            doc_num = input('Введите номер документа: ')
            doc_type = input('Введите тип документа: ')
            doc_owner = input('Введите владельца документа: ')
            doc_shelf = input('Введите полку для хранения: ')
            ad_new_doc(doc_num, doc_type, doc_owner, doc_shelf)
            input_command()
        elif command == 'd':
            doc_num = input('Введите номер документа: ')
            d_delete_doc(doc_num)
            input_command()
        elif command == 'm':
            doc_num = input('Введите номер документа: ')
            doc_shelf = input('Введите полку для хранения: ')
            m_move_doc(doc_num, doc_shelf)
            input_command()
        else:
            print('Такой команды не существует\n')
            input_command()
    print('Работа завершена\n')
    exit()


input_command()
