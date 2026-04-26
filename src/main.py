from data_utils import find_by_name, filter_by_value, count_items

students = [
    {"name": "Игорь", "city": "Екатеринбург", "age": 31},
    {"name": "Олеся", "city": "Москва", "age": 27},
    {"name": "Лера", "city": "Мариуполь", "age": 18},
    {"name": "Ярослав", "city": "Нижний Новгород", "age": 23}
]

print(find_by_name(students, "Игорь"))
print(filter_by_value(students, "city", "Москва"))
print(count_items(students))

from file_utils import save_text, load_text, append_text, count_lines

save_text("project_note.txt", "Это первая строка проекта.")
append_text("project_note.txt", "Это вторая строка проекта.")

print(load_text("project_note.txt"))
print("Количество строк:", count_lines("project_note.txt"))

from csv_utils import save_csv, load_csv, count_csv_rows, sum_column

products = [
    ["title", "price", "count"],
    ["Телевизор", 50000, 3],
    ["Акустика", 10000, 5]
]

save_csv("products.csv", products)

print(load_csv("products.csv"))
print("Количество строк:", count_csv_rows("products.csv"))
print("Сумма столбца price:", sum_column("products.csv", 1))

from json_utils import save_json, load_json, dict_to_json_text

config = {
    "model": "ASUS",
    "temperature": 1.5,
    "max_tokens": 300
}

save_json("config.json", config)

print(load_json("config.json"))
print(dict_to_json_text(config))

from text_utils import normalize_text
from data_utils import count_items
from file_utils import save_text, load_text
from json_utils import save_json, load_json

text = "   Мой первая программа на Python   "
tasks = ["изучить строки", "изучить файлы", "изучить json"]

clean_text = normalize_text(text)
task_count = count_items(tasks)

save_text("project_note.txt", clean_text)
loaded_text = load_text("project_note.txt")

config = {
    "project_name": "my_first_project",
    "task_count": task_count
}

save_json("project_config.json", config)
loaded_config = load_json("project_config.json")

print("Очищенный текст:", clean_text)
print("Прочитанный текст из файла:", loaded_text)
print("Количество задач:", task_count)
print("Загруженный JSON:", loaded_config)

from user_menu import show_menu, run_choice

show_menu()
choice = input("Введите номер действия: ")
run_choice(choice)