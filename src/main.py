from text_utils import normalize_text, word_count, contains_word
from data_utils import find_by_name, filter_by_value, count_items
from file_utils import save_text, load_text, append_text, count_lines
from csv_utils import save_csv, load_csv, count_csv_rows, sum_column
from json_utils import save_json, load_json, dict_to_json_text


def build_project_report(text, tasks, students):
    clean_text = normalize_text(text)
    words = word_count(clean_text)
    has_python = contains_word(clean_text, "python")
    task_count = count_items(tasks)
    student_count = count_items(students)

    report = {
        "clean_text": clean_text,
        "word_count": words,
        "has_python": has_python,
        "task_count": task_count,
        "student_count": student_count
    }

    return report


def run_project_scenario():
    # 1. Исходные данные проекта
    text = "   Мой первый проект на Python   "

    tasks = [
        "изучить строки",
        "изучить списки словарей",
        "изучить файлы",
        "изучить CSV",
        "изучить JSON",
        "собрать проект"
    ]

    students = [
        {"name": "Игорь", "city": "Екатеринбург", "age": 31},
        {"name": "Олеся", "city": "Казань", "age": 27},
        {"name": "Рамиль", "city": "Санкт-Петербург", "age": 20},
        {"name": "Анастасия", "city": "Пятигорск", "age": 25}
    ]

    # 2. Работа с текстом и данными
    report = build_project_report(text, tasks, students)

    found_student = find_by_name(students, "Игорь")
    ekb_students = filter_by_value(students, "city", "Екатеринбург")

    # 3. Работа с текстовым файлом
    save_text("project_note.txt", report["clean_text"])
    append_text("project_note.txt", "Проект собран из нескольких модулей.")

    loaded_note = load_text("project_note.txt")
    note_lines = count_lines("project_note.txt")

    # 4. Работа с CSV
    rows = [
        ["title", "price", "count"],
        ["Телевизор", 50000, 2],
        ["Системный блок", 60000, 5],
        ["Клавиатура", 3000, 3]
    ]

    save_csv("products.csv", rows)
    loaded_products = load_csv("products.csv")
    product_rows = count_csv_rows("products.csv")
    total_price = sum_column("products.csv", 1)

    # 5. Работа с JSON
    project_config = {
        "project_name": "student_final_project",
        "task_count": report["task_count"],
        "student_count": report["student_count"],
        "note_lines": note_lines,
        "product_rows": product_rows
    }

    save_json("project_config.json", project_config)
    loaded_config = load_json("project_config.json")
    config_text = dict_to_json_text(loaded_config)

    # 6. Вывод результата
    print("=== Финальный учебный проект ===")
    print()
    print("1. Текст:")
    print("Очищенный текст:", report["clean_text"])
    print("Количество слов:", report["word_count"])
    print("Есть слово python:", report["has_python"])
    print()

    print("2. Данные студентов:")
    print("Найден студент Игорь:", found_student)
    print("Студенты из Екатеринбурга:", ekb_students)
    print("Количество студентов:", report["student_count"])
    print()

    print("3. Текстовый файл:")
    print("Содержимое project_note.txt:")
    print(loaded_note)
    print("Количество строк:", note_lines)
    print()

    print("4. CSV:")
    print("Данные products.csv:", loaded_products)
    print("Количество строк в CSV:", product_rows)
    print("Сумма столбца price:", total_price)
    print()

    print("5. JSON:")
    print("Загруженная конфигурация:", loaded_config)
    print("JSON-текст:")
    print(config_text)
    print()

    print("Проект успешно запущен.")


def main():
    run_project_scenario()


if __name__ == "__main__":
    main()

import sqlite3
connection = sqlite3.connect("products_lesson01.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    category TEXT,
    price REAL
)
""")

cursor.execute(
    "INSERT INTO products (title, category, price) VALUES (?, ?, ?)",
    ("Творог", "Молочка", 80)
)
# TODO: добавьте второй товар
cursor.execute(
    "INSERT INTO products (title, category, price) VALUES (?, ?, ?)",
    ("Сосиски", "Мясные продукты", 200)
)
# TODO: добавьте третий товар
cursor.execute(
    "INSERT INTO products (title, category, price) VALUES (?, ?, ?)",
    ("Хлеб", "Хлебобулочные изделия", 40)
)

connection.commit()

cursor.execute("SELECT * FROM products")
# TODO: получите все строки через fetchall()
products = cursor.fetchall()

# TODO: выведите products
print(products)

for product in products:
    print("ID:", product[0], "| Имя:", product[1], "| Категория:", product[2], "| Цена:", product[3])

cursor.execute(
    "SELECT * FROM products WHERE price > ?",
    ("100",)
)
# TODO: получите результат в переменную expensive_products
expen_products = cursor.fetchall()
# TODO: выведите expensive_products
print(expen_products)

connection.close()

import sqlite3
# TODO: создайте connection
connection = sqlite3.connect("tovar_lesson02.db")
# TODO: создайте cursor
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tovars (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT,
 category TEXT,
 price INTEGER,
 count INTEGER
)
""")
# TODO: выполните connection.commit()
connection.commit()

cursor.execute("DELETE FROM tovars")
# TODO: создайте список записей
tovars = [
    ("Ряженка", "Молочные продукты", 60, 10),
    ("Дезодорант", "Уход за собой", 150, 20),
    ("Полотенце", "Бытовые товары", 1000, 15),
    ("Стив Джобс", "Книги", 2500, 5),
    ("Дюшес", "Лимонады", 100, 40),
    ("Молоко", "Молочные продукты", 70, 30),
    ("Лак для волос", "Уход за собой", 200, 15),
    ("Швабра", "Бытовые товары", 500, 10)
]
# TODO: добавьте записи через executemany
cursor.executemany(
    "INSERT INTO tovars (title, category, price, count) VALUES (?, ?, ?, ?)",
    tovars
)
# TODO: выполните commit
connection.commit()

cursor.execute("SELECT * FROM tovars")
# TODO: получите результат через fetchall()
all_tovars = cursor.fetchall()
# TODO: выведите строки через for
for tovar in all_tovars:
  print(tovar)

  cursor.execute("SELECT title, category FROM tovars")
# TODO: получите результат
titles_and_category = cursor.fetchall()
# TODO: выведите результат
for row in titles_and_category:
  print(row)

  cursor.execute(
    "SELECT* FROM tovars WHERE count > ?",
    (10,)
)
# TODO: получите результат
count_tovars = cursor.fetchall()

# TODO: выведите результат
for tovar in count_tovars:
  print(tovar)

cursor.execute("SELECT * FROM tovars WHERE category = ?",
               ("Молочные продукты",)
               )
# TODO: получите результат
milk_tovars = cursor.fetchall()

# TODO: выведите результат
for tovar in milk_tovars:
  print(tovar)

cursor.execute(
    "SELECT * FROM tovars WHERE category = ? AND count > ?",
    ("Молочные продукты", 10)
)
# TODO: вывести результат
filtered_milk = cursor.fetchall()

print("Молочка по кол-ву больше 10:")
for tovar in filtered_milk:
  print(tovar)
# TODO: запрос с OR
cursor.execute(
    "SELECT * FROM tovars WHERE price > ? OR price = ?",
    ("100","100")
)

# TODO: вывести результат
filtered_price = cursor.fetchall()

print("\nЦена больше 100, либо равна 100")
for tovar in filtered_price:
  print(tovar)

cursor.execute(
    "SELECT * FROM tovars ORDER BY count DESC LIMIT 3"
)
# TODO: получите результат
top_count = cursor.fetchall()
# TODO: выведите результат
for tovar in top_count:
  print(tovar)

connection.close()