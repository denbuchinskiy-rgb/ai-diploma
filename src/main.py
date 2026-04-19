from data_utils import find_by_name, filter_by_value, count_items

students = [
    {"name": "Игорь", "city": "Екатеринбург", "age": 31},
    {"name": "Олеся", "city": "Москва", "age": 27},
    {"name": "Ольга", "city": "Казань", "age": 19},
    {"name": "Павел", "city": "Уфа", "age": 22}
]

print(find_by_name(students, "Игорь"))
print(filter_by_value(students, "city", "Казань"))
print(count_items(students))

from file_utils import save_text, load_text, append_text, count_lines

save_text("project_note.txt", "Это первая строка проекта.")
append_text("project_note.txt", "Это вторая строка проекта.")

print(load_text("project_note.txt"))
print("Количество строк:", count_lines("project_note.txt"))