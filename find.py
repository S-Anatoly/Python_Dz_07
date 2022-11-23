import operation


def find_pheople():
    surnam = input('Введите ID для поиска студента:  ')
    print(f'Мы нашли -> ', end='')
    operation.show(surnam)
