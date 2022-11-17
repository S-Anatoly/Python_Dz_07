import operation


def find_pheople():
    surnam = input('Введите фалимию для поиска данных - ')
    print(f'Мы нашли -> ', end='')
    operation.show(surnam)
