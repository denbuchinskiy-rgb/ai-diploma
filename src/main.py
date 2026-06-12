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

from db.connection import get_connection
from db.create_tables import create_projects_table
from db.insert_data import seed_demo_projects
from db.queries import (
get_all_projects,
find_projects_by_status,
get_top_projects
)
from db.reports import (
get_average_score,
get_status_report
)
def print_section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)
def show_all_projects(connection):
    print_section("1. Все проекты")
    projects = get_all_projects(connection)
    for project in projects:
        print(project)
def show_ready_projects(connection):
    print_section("2. Готовые проекты")
    ready_projects = find_projects_by_status(connection, "Зачтено")
    for project in ready_projects:
        print(project)
def show_average_score(connection):
    print_section("3. Средний score")
    avg_score = get_average_score(connection)
    print("Средний score:", round(avg_score, 2))
def show_status_report(connection):
    print_section("4. Отчёт по статусам")
    report = get_status_report(connection)
    for status, count in report:
     print("Статус:", status, "| Количество:", count)
def show_top_projects(connection):
    print_section("5. Топ-3 проекта")
    top_projects = get_top_projects(connection, 3)
    for project in top_projects:
        print(project)

def show_exam_demo(connection):
    print_section("Демонстрация проекта к экзамену")
    show_all_projects(connection)
    show_ready_projects(connection)
    show_average_score(connection)
    show_status_report(connection)
    show_top_projects(connection)
print()
print("Проект успешно запущен и готов к показу на экзамене.")
def main():
    connection = get_connection()
    create_projects_table(connection)
    seed_demo_projects(connection)
    show_exam_demo(connection)
    connection.close()
print()
print("Соединение с базой данных закрыто.")
if __name__ == "__main__":
    main()


# TODO: импортируйте numpy как np
import numpy as np
# TODO: импортируйте matplotlib.pyplot как plt
import matplotlib.pyplot as plt
# TODO: выведите сообщение
print("Библиотеки подключены")

# TODO: создайте массив x через np.array()
x = np.array([-10, -9, -8, -7, -6, 5, 6, 7, 8, 9, 10])
# TODO: создайте y = 2 * x + 1
y = 2 * x + 1
# TODO: выведите x и y
print("x =", x)
print("y =", y)

# TODO: создайте x через np.linspace()
x = np.linspace(-5, 5, 150)
# TODO: создайте y
y = 2 * x + 1
# TODO: plt.plot(...)
plt.figure(figsize=(8,5))
plt.plot(x, y)
# TODO: добавьте title
plt.title("Линейная функция y = 2x + 1")
plt.xlabel("x")
plt.ylabel("y")
# TODO: добавьте grid
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте x
x = np.linspace(-5, 5, 150)
# TODO: создайте y1, y2, y3
y1 = x
y2 = 2 * x
y3 = -x
# TODO: постройте 3 графика
plt.figure(figsize=(8,5))
plt.plot(x, y1, label="y = x")
plt.plot(x, y2, label="y = 2x")
plt.plot(x, y3, label="y = -x")
# TODO: добавьте legend
plt.legend()
plt.grid(True)
plt.title("Сравнение линейных функции")
# TODO: show()
plt.show()

# TODO: создайте функции
x = np.linspace(-5, 5, 150)
y1 = x
y2 = x + 5
y3 = x - 5
# TODO: постройте графики
plt.figure(figsize=(8,5))
plt.plot(x, y1, label="y = x")
plt.plot(x, y2, label="y = x + 5")
plt.plot(x, y3, label="y = x - 5")
# TODO: добавьте legend
plt.legend()
plt.grid(True)
plt.title("Влияние коэффициента b")
# TODO: show()
plt.show()

# TODO: создайте x
x = np.linspace(-5, 5, 150)
# TODO: создайте y = x ** 2
y = x ** 2
# TODO: постройте график
plt.figure(figsize=(8,5))
plt.plot(x, y)
plt.title("Квадратичная функция y = x²")
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте y1, y2, y3
x = np.linspace(-5, 5, 150)
y1 = x ** 2
y2 = 3 * x ** 2
y3 = x ** 2 + 5
# TODO: постройте графики
plt.figure(figsize=(8, 5))
plt.plot(x, y1, label="y = x²")
plt.plot(x, y2, label="y = 3x²")
plt.plot(x, y3, label="y = x² + 5")
# TODO: добавьте legend
plt.grid(True)
plt.title("Изменение квадратичной функции")
# TODO: show()
plt.show()

x = np.linspace(-15, 15, 150)
y = x ** 2
# TODO: найдите минимум
print("Минимум:", np.min(y))

# TODO: найдите максимум
print("Максимум:", np.max(y))

# TODO: создайте словарь metrics
metrics = {
    "epoch": [5, 6, 7, 8, 9],
    "loss": [1.0, 0.9, 0.7, 0.5, 0.4]
}
# TODO: постройте график loss
plt.figure(figsize=(8,5))
plt.plot(metrics["epoch"], metrics["loss"])
# TODO: добавьте title
plt.title("Пример графика обучения модели")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте список summary
summary = [
    "Функции используются в AI",
    "Графики помогают анализировать данные",
    "matplotlib используется для визуализации",
    "Линейные и квадратичные функции — основа дальнейшей математики"
]
# TODO: выведите все выводы
for item in summary:
  print("-", item)