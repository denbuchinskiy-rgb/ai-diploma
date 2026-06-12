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

# TODO: импортируйте numpy как np
import numpy as np
# TODO: импортируйте matplotlib.pyplot как plt
import matplotlib.pyplot as plt
# TODO: выведите сообщение
print("Библиотеки подключены")

# TODO: создайте x через np.linspace()
x = np.linspace(-5, 5, 250)
# TODO: создайте y = x ** 2
y = x ** 2
# TODO: постройте график
plt.figure(figsize=(10, 8))
plt.plot(x, y)
# TODO: добавьте title, xlabel, ylabel, grid
plt.title("Степенная функция y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
# TODO: show()
plt.show()


# TODO: создайте x
x = np.linspace(-5, 5, 250)

# TODO: создайте y = x ** 3
y = x ** 3
# TODO: постройте график
plt.figure(figsize=(10, 8))
plt.plot(x, y)
plt.title("Кубическая функция y = x³")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте x от 0 до 25
x = np.linspace(0, 15, 250)

# TODO: создайте y = np.sqrt(x)
y = np.sqrt(x)
# TODO: постройте график
plt.figure(figsize=(10,8))
plt.plot(x,y)
plt.title("Функция корня y = sqrt(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте x
x = np.linspace(-15, 15, 250)
# TODO: создайте y = 2 ** x
y = 2 ** x
# TODO: постройте график
plt.figure(figsize=(10, 8))
plt.plot(x, y)
plt.title("Показательная функция y = 2ˣ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте x от 0.1 до 20
x = np.linspace(0.1, 15, 250)

# TODO: создайте y = np.log(x)
y = np.log(x)
# TODO: постройте график
plt.figure(figsize=(10, 8))
plt.plot(x, y)
plt.title("Логарифмическая функция y = log(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте x от -2*pi до 2*pi
x = np.linspace(-4* np.pi, 4 * np.pi, 450)

# TODO: создайте y = np.sin(x)
y = np.sin(x)
# TODO: постройте график
plt.figure(figsize=(10, 8))
plt.plot(x, y)
plt.title("Функция y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте x от -2*pi до 2*pi
x = np.linspace(-4 * np.pi, 4 * np.pi, 450)
# TODO: создайте y = np.cos(x)
y = np.cos(x)
# TODO: постройте график
plt.figure(figsize=(10, 8))
plt.plot(x, y)
plt.title("Функция y = cos(x)")
plt.xlabel("x")
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте x
x = np.linspace(-4 * np.pi, 4 * np.pi, 450)
# TODO: создайте y_sin и y_cos
y_sin = np.sin(x)
y_cos = np.cos(x)
# TODO: постройте оба графика
plt.figure(figsize=(10, 8))
plt.plot(x, y_sin, label="sin(x)")
plt.plot(x, y_cos, label="cos(x)")
plt.title("Сравнение sin(x) и cos(x)")
plt.xlabel("x")
plt.ylabel("y")
# TODO: добавьте legend
plt.legend()
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте положительный x
x = np.linspace(0.1, 5, 250)
# TODO: создайте y_linear = x
y_linear = x

# TODO: создайте y_square = x ** 2
y_square = x ** 3
# TODO: создайте y_log = np.log(x)
y_log = np.log(x)
# TODO: создайте y_exp = 2 ** x
y_exp = 3 ** x
# TODO: постройте все графики
plt.figure(figsize=(9, 6))
plt.plot(x, y_linear, label="y = x")
plt.plot(x, y_square, label="y = x3")
plt.plot(x, y_log, label="y = log(x)")
plt.plot(x, y_exp, label="y = 3ˣ")
plt.title("Сравнение элементарных функции")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
# TODO: создайте список summary из 4 выводов
summary = [
    "Степенные функции могут быстро расти",
    "Показательная функция растёт очень быстро",
    "Логарифм растёт медленно",
    "Синус и косинус описывают колебания"
]
# TODO: выведите summary
for item in summary:
  print("-", item)

# TODO: создайте список из 6 чисел
scores = [60, 75, 100, 85, 90, 70]
# TODO: выведите список
print("Оценки:", scores)
# TODO: выведите длину списка
print("Количество оценок:", len(scores))

# TODO: используйте sum() и len()
scores = [60, 75, 100, 85, 90, 70]
# TODO: посчитайте average_value
average_score = sum(scores)/ len(scores)
# TODO: выведите результат
print("Средний балл:", average_score)

# TODO: используйте max()
max_score = max(scores)

# TODO: используйте min()
min_score = min(scores)
# TODO: выведите максимум и минимум
print("Максимум:", max_score)
print("Минимум:", min_score)

# TODO: создайте пустой список result
result = []
# TODO: в цикле for выберите числа больше заданного порога
for score in scores:
  if score > 70:
    result.append(score)
# TODO: выведите result
print("Оценки выше 70:", result)

# TODO: создайте словарь для объекта своей темы
candidate = {
    "name": "Василий",
    "city": "Ульяновск",
    "score": 75
}

# TODO: выведите словарь
print(candidate)
# TODO: обратитесь к одному ключу
print("Имя:", candidate["name"])

# TODO: создайте список минимум из 4 словарей
candidates = [
  {"name": "Алексей", "city": "Москва", "score": 92},
  {"name": "Мария", "city": "Санкт-Петербург", "score": 87},
  {"name": "Дмитрий", "city": "Казань", "score": 95},
  {"name": "Ольга", "city": "Новосибирск", "score": 81},
  {"name": "Андрей", "city": "Екатеринбург", "score": 89}
]
# TODO: выведите каждый словарь через for
for candidate in candidates:
  print(candidate)

# TODO: создайте пустой список filtered_items
filtered_items = []
# TODO: в цикле отберите записи по городу, категории, статусу или типу
for candidate in candidates:
  if candidate["city"] == "Санкт-Петербург":
    filtered_items.append(candidate)
# TODO: выведите результат
print("Кандитаты из Санкт-Петербурга:")
for candidate in filtered_items:
    print(candidate)

# TODO: используйте sorted()
candidates = [
  {"name": "Алексей", "city": "Москва", "score": 92},
  {"name": "Мария", "city": "Санкт-Петербург", "score": 87},
  {"name": "Дмитрий", "city": "Казань", "score": 95},
  {"name": "Ольга", "city": "Новосибирск", "score": 81},
  {"name": "Андрей", "city": "Екатеринбург", "score": 89}
]
# TODO: отсортируйте по числовому полю
sorted_candidates = sorted(
    candidates,
    key=lambda item: item["score"],
    reverse=True
)
# TODO: выведите результат
for candidate in sorted_candidates:
  print(candidate)

# TODO: создайте список с повторяющимися значениями
cities = ["Москва", "Санкт-Петербург", "Москва", "Новосибирск","Санкт-Петербург"]
# TODO: преобразуйте его в set
unique_cities = set(cities)
# TODO: выведите уникальные значения
print("Уникальные города:", unique_cities)

# TODO: возьмите список словарей из своей темы
candidates = [
  {"name": "Алексей", "city": "Москва", "score": 92},
  {"name": "Мария", "city": "Санкт-Петербург", "score": 87},
  {"name": "Дмитрий", "city": "Казань", "score": 95},
  {"name": "Ольга", "city": "Новосибирск", "score": 81},
  {"name": "Андрей", "city": "Екатеринбург", "score": 89}
]
# TODO: отфильтруйте записи по условию
city = "Екатеринбург"
filtered = []
for candidate in candidates:
  if candidate["city"] == city:
    filtered.append(candidate)
# TODO: отсортируйте их по числовому показателю
sorted_candidates = sorted(
    filtered,
    key=lambda item: item["score"],
    reverse=True
)
# TODO: выберите лучший результат
best_candidate = sorted_candidates[0]
# TODO: выведите результат
print("Лучший кандидат из города", city)
print(best_candidate)

# TODO: импортируйте numpy как np
import numpy as np
# TODO: импортируйте pandas как pd
import pandas as pd
# TODO: импортируйте matplotlib.pyplot как plt
import matplotlib.pyplot as plt
# TODO: выведите сообщение
print("Библиотеки подключены")

# TODO: создайте список x_values около числа 2
x_values =[1.5, 1.9, 1.99, 2.0, 2.01, 3.01, 3.1, 3.5]
# TODO: создайте список y_values для функции y = 3 * x
y_values = []
for x in x_values:
   y_values.append(3 * x)
# TODO: создайте DataFrame
table = pd.DataFrame({
    "x": x_values,
    "y = 3x": y_values
})
# TODO: покажите таблицу
table

# TODO: создайте x через np.linspace()
x = np.linspace(0, 5, 150)
# TODO: создайте y = 3 * x
y = 3 * x
# TODO: постройте график
plt.figure(figsize=(10, 8))
plt.plot(x, y, label="y = 3x")
# TODO: отметьте точку x=2, y=6
plt.scatter([2], [6], label="точка x=2, y=6")
# TODO: show()
plt.title("Предел на примере y = 3x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

# TODO: создайте left_x около числа 2
left_x = [1.9, 1.99, 1.999]
# TODO: создайте right_x около числа 2
right_x = [2.1, 2.01, 2.001]
# TODO: посчитайте left_y и right_y
left_y = [2 * x for x in left_x]
right_y = [2 * x for x in left_y]
# TODO: создайте DataFrame
table = pd.DataFrame({
    "x слева": left_x,
    "y слева": left_y,
    "x справа": right_x,
    "y справа": right_y
})
# TODO: покажите таблицу
table

# TODO: создайте x_values около числа 3
x_values = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
# TODO: посчитайте y_values = x ** 2
y_values = [x ** 2 for x in x_values]
# TODO: создайте DataFrame
table = pd.DataFrame({
    "x": x_values,
    "y = x²": y_values
})
# TODO: покажите таблицу
table

# TODO: создайте x
x = np.linspace(-2, 6, 250)
# TODO: создайте y = x ** 2
y = x ** 2
# TODO: постройте график
plt.figure(figsize=(10, 8))
plt.plot(x, y, label="y = x²")

# TODO: отметьте точку x=3, y=9
plt.scatter([3],[9], label="x=3, y=9")
# TODO: show()
plt.title("Предел на примере y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

# TODO: создайте x_values около 2, но без самого 2
x_values = [1.5, 1.75, 1.9, 1.95, 2.05, 2.1, 2.25, 2.5]
# TODO: посчитайте y_values для функции
y_values = []
for x in x_values:
    y = (x ** 2 - 4)/(x - 2)
    y_values.append(y)
# TODO: создайте DataFrame
table = pd.DataFrame({
    "x": x_values,
    "y": y_values
})
# TODO: покажите таблицу
table

# TODO: создайте x_left до 2
x_left = np.linspace(-2, 1.99, 100)
# TODO: создайте x_right после 2
x_right = np.linspace(2.01, 4, 100)
# TODO: посчитайте y_left и y_right
y_left = (x_left ** 2 - 1) / (x_left - 1)
y_right = (x_right ** 2 - 1) / (x_right - 1)
# TODO: постройте график
plt.figure(figsize=(8,5))
plt.plot(x_left, y_left)
plt.plot(x_right, y_right)
# TODO: отметьте точку предела x=2, y=4
plt.scatter([2], [3], facecolors='none', edgecolors='black', label="предел = 2")
# TODO: show()
plt.title("Функция не определена в x=1, но предел есть")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

# TODO: создайте список epochs
epochs = [7, 8, 9, 10, 11, 12, 13]
# TODO: создайте список loss, который уменьшается
loss = [1.00, 0.50, 0.25, 0.12, 0.06, 0.03, 0.01]
# TODO: постройте график
plt.figure(figsize=(10, 8))
plt.plot(epochs, loss, marker="o")
# TODO: show()
plt.title("Ошибка модели стремится к 0")
plt.xlabel("Эпоха")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# TODO: создайте список summary из 5 выводов
summary = [
    "Предел показывает, к чему стремится функция",
    "К точке можно приближаться слева и справа",
    "Функция может иметь предел, даже если не определена в точке",
    "Пределы нужны для понимания производной и оптимизации",
    "В AI идея предела связана с уменьшением ошибки модели"
]
# TODO: выведите каждый вывод
for item in summary:
  print("-", item)