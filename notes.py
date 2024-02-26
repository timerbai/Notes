import json
import datetime

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
notes = load_notes()

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'message': message,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным ID не найдена")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новое тело заметки: ")
            note['title'] = new_title
            note['message'] = new_message
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

def filter_notes_by_date():
    date_str = input("Введите дату для фильтрации заметок (YYYY-MM-DD): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Некорректный формат даты")
        return
    
    filtered_notes = [note for note in notes if datetime.datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S").date() == filter_date]

    if filtered_notes:
        print("Заметки на указанную дату:")
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['message']}")
            print(f"Дата/Время создания или последнего изменения: {note['timestamp']}")
            print()
    else:
        print("Заметки на указанную дату не найдены")

def print_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['message']}")
        print(f"Дата/Время создания или последнего изменения: {note['timestamp']}")
        print()    

while True:
    print("Доступные команды:")
    print("add - добавить заметку")
    print("delete - удалить заметку")
    print("edit - редактировать заметку")
    print("filter - фильтровать заметки по дате")
    print("list - вывести список заметок")
    print("quit - выйти из программы")
    command = input("Введите команду: ")

    if command == "add":
        add_note()
    elif command == "delete":
        delete_note()
    elif command == "edit":
        edit_note()
    elif command == "filter":
        filter_notes_by_date()
    elif command == "list":
        print_notes()
    elif command == "quit":
        break
    else:
        print("Некорректная команда")