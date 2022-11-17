import csv


def record_file(name, surname, phone, description):
    names = [{'Имя': name, 'Фамилия': surname, 'Телефон': phone, 'Описание': description}]
    with open('phonebook.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(names[0].keys()), delimiter=';')
        writer.writeheader()
        for i in names:
            writer.writerow(i)


def show(surname):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';', quotechar='"')
        for i in reader:
            if surname == i[1]:
                print(i)


def all_data():
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i in reader:
            print(i)



def clear_file():
    with open('phonebook.csv', 'w'):
        print('Данные удалены!')
