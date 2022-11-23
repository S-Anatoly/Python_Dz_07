import operation


def record_pheople():
    id = int(input('Введите ID студента: '))
    name = input('Введите имя студента: ')
    surname = input('Введите фамилию студента: ')
    phone = input('Введите телефон студента: ')
    faculty = input('Введите факультет студента:  ')
    operation.record_file(id, name, surname, phone, faculty)
    print('Данные записаны!')

    choice = input('Записать еще человека? (Да/Нет) - ')
    choice = choice.lower()
    if choice == 'да':
        record_pheople()
    else:
        exit()
