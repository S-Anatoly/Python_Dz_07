import operation


def record_pheople():
    name = input('Введите имя - ')
    surname = input('Введите фамилию - ')
    phone = input('Введите телефон - ')
    discreption = input('Введите описание - ')
    operation.record_file(name, surname, phone, discreption)
    print('Данные записаны!')

    choice = input('Записать еще человека? (Да/Нет) - ')
    choice = choice.lower()
    if choice == 'да':
        record_pheople()
    else:
        exit()
