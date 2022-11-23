import operation
import record
import find
import log

def oper():
    print('Информационная база "Студент"')
    choice = input('''Введите:
    "просмотр" - для отображения всей БД
    "поиск" - для поиска информации о студенте
    "запись" - для записи нового студента
    "очистить" - для полной очистки БД ''' + '\n')
    choice = choice.lower()       # перевожу в нижний регистр для избежания некорренктного ввода
    log.action_recording(choice)
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