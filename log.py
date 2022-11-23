from datetime import datetime as dt

def action_recording(action):
    if action == 'запись': act = 'Запись нового студента'
    elif action == 'поиск': act = 'Поиск студента'
    elif action == 'просмотр': act = 'Просмотр всей БД'
    elif action == 'очистить': act = 'Очистка БД'
    else:
        return
    time = dt.now().strftime('%d/%m/%y - %H:%M')
    with open('log.txt', 'a', encoding='utf-8') as log:
        log.write(f'{act} -> {time}' + '\n')