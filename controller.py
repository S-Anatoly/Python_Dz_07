import operation
import record
import find

def oper():
    choice = input('''Введите:
    "просмотр" - для просмотра всего файла
    "поиск" - для поиска информации
    "запись" - для записи новой информации
    "очистить" - для очистки файла ''' + '\n')
    choice = choice.lower()       # перевожу в нижний регистр для избежания некорренктного ввода

    if choice == "запись":
        record.record_pheople()
    elif choice == "поиск":
        find.find_pheople()
    elif choice == 'очистить':
        operation.clear_file()
    elif choice == 'просмотр':
        operation.all_data()
    else:
        print('Такой команды нет!')