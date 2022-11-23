import csv
import pandas as pd


def record_file(id, name, surname, phone, faculty):
    names = [{'ID': id, 'Имя': name, 'Фамилия': surname, 'Телефон': phone, 'Факультет': faculty}]
    df = pd.DataFrame(names, columns=['ID', 'Имя', 'Фамилия', 'Телефон', 'Факультет'])
    df.to_csv("phonebook.csv", mode='a', index=False, header=False)


def show(id):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        for i in reader:
            if id == i[0]:
                print(i)


def all_data():
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i in reader:
            print(i)


def clear_file():
    df = pd.DataFrame(columns=['ID', 'Имя', 'Фамилия', 'Телефон', 'Факультет'])
    df.to_csv("phonebook.csv", index=False)
    print('Данные удалены!')
