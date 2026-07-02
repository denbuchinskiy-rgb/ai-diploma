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
# TODO: импортируйте pandas как pd
import pandas as pd
# TODO: импортируйте matplotlib.pyplot как plt
import matplotlib.pyplot as plt
# TODO: выведите сообщение
print("Библиотеки подключены")

# TODO: напишите функцию loss_function(x)
def loss_function(x):
  return (x - 4) ** 2 + 1
# TODO: задайте x0 = 4
x0 = 4
# TODO: посчитайте minimum_value
minimum_value = loss_function(x0)
# TODO: выведите x0 и minimum_value
print("Минимум находится при x =", x0)
print("Минимальное значение loss =", minimum_value)

# TODO: создайте x через np.linspace()
x = np.linspace(-3, 10, 350)
# TODO: создайте loss = loss_function(x)
loss = loss_function(x)
# TODO: постройте график
plt.figure(figsize=(10, 8))
plt.plot(x, loss, label="loss(x) = (x - 4)² + 1")
# TODO: отметьте минимум x=4, y=1
plt.scatter([4], [1], label="минимум")
# TODO: добавьте title, xlabel, ylabel, legend, grid
plt.title("Функция ошибки модели")
plt.xlabel("x")
plt.ylabel("loss")
plt.legend()
plt.grid(True)
# TODO: show()
plt.show()

# TODO: напишите функцию loss_derivative(x)
def loss_derivative(x):
    return 2 * (x - 4)
# TODO: создайте список points
points = [-1.5, 0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
# TODO: посчитайте derivative_values
derivative_values = [loss_derivative(point) for point in points]
# TODO: создайте DataFrame со столбцами x, loss(x), loss'(x)
table = pd.DataFrame({
    "x": points,
    "loss(x)": [loss_function(point) for point in points],
    "loss'(x)": derivative_values
})
# TODO: покажите таблицу
table

# TODO: создайте пустой список analysis
analysis = []
# TODO: для каждой точки из points посчитайте derivative
for point in points:
  derivative = loss_derivative(point)
# TODO: если derivative < 0, статус = loss убывает
  if derivative < 0:
       status = "loss убывает"
# TODO: если derivative > 0, статус = loss растёт
  elif derivative > 0:
       status = "loss растёт"
# TODO: если derivative == 0, статус = минимум
  else:
       status = "критическая точка / минимум"
# TODO: добавьте словарь в analysis
  analysis.append({
      "x": point,
      "derivative": derivative,
      "status": status
  })
# TODO: выведите analysis
for item in analysis:
  print(item)

x_current = -2
# TODO: задайте learning_rate = 0.2
learning_rate = 0.2
# TODO: задайте steps = 20
steps = 20
# TODO: создайте пустой список history
history = []
# TODO: в цикле сохраните step, x, loss, derivative
for step in range(steps):
    current_loss = loss_function(x_current)
    current_derivative = loss_derivative(x_current)
    history.append({
        "step": step,
        "x": x_current,
        "loss": current_loss,
        "derivative": current_derivative
    })
# TODO: обновите x_current по формуле:
# x_current = x_current - learning_rate * derivative
    x_current = x_current - learning_rate * current_derivative

# TODO: выведите финальное x и финальный loss
print("Финальное x:", x_current)
print("Финальный loss:", loss_function(x_current))

# TODO: создайте history_df = pd.DataFrame(history)
history_df = pd.DataFrame(history)
# TODO: покажите первые 10 строк
history_df.head(10)

# TODO: создайте x и loss для графика функции
x = np.linspace(-5, 10, 350)
loss = loss_function(x)
# TODO: постройте график функции loss
plt.figure(figsize=(10, 8))
plt.plot(x, loss, label="loss(x)")

# TODO: добавьте точки из history_df
plt.scatter(history_df["x"], history_df["loss"], label="шаги оптимизации")
# TODO: отметьте истинный минимум x=4, y=1
plt.scatter([4],[1], label="истинный минимум")
# TODO: добавьте legend и grid
plt.title("Оптимизация функции ошибки")
plt.xlabel("x")
plt.ylabel("loss")
plt.legend()
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте словарь project_report
project_report = {
    "project_name": "Анализ функции ошибки модели",
    "start_x": history_df["x"].iloc[0],
    "final_x": history_df["x"].iloc[-1],
    "start_loss": history_df["loss"].iloc[0],
    "final_loss": history_df["loss"].iloc[-1],
    "steps": steps,
    "minimum_x": 3,
    "minimum_loss": 2
}
# В словаре должны быть:
# project_name
# start_x
# final_x
# start_loss
# final_loss
# steps
# minimum_x
# minimum_loss

# TODO: выведите словарь через for
for key, value in project_report.items():
  print(key, ":", value)

# TODO: создайте список summary из 6 выводов
summary = [
    "Функции помогают описывать зависимости",
    "Графики помогают видеть поведение данных",
    "Структуры данных помогают хранить результаты анализа",
    "Производная показывает направление изменения функции",
    "Оптимизация помогает найти минимум ошибки",
    "Эти идеи являются основой машинного обучения"
]
# TODO: выведите выводы через for
for item in summary:
  print("-", item)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

print("Библиотеки загружены")

data = load_breast_cancer(as_frame=True)

# TODO: создайте DataFrame
df = data.frame.copy()

print("Размер таблицы:", df.shape)
print("Классы:", list(data.target_names))
print(df.head())

# TODO: создайте diagnosis через map:
# 0 -> malignant
# 1 -> benign
df["diagnosis"] = df["target"].map({0:"malignant", 1:"benign"})

class_counts = df["diagnosis"].value_counts()
print(class_counts)

class_counts.plot(kind="bar", figsize=(6, 4))
plt.title("Количество объектов по классам")
plt.xlabel("Класс")
plt.ylabel("Количество")
plt.grid(True)
plt.tight_layout()
plt.show()

feature = "mean texture"

# TODO: посчитайте средний mean radius по diagnosis
mean_by_class = df.groupby("diagnosis")[feature].mean().round(2)

print(mean_by_class)

plt.figure(figsize=(8, 4))
for diagnosis in ["benign", "malignant"]:
    values = df[df["diagnosis"] == diagnosis][feature]
    plt.hist(values, bins=20, alpha=0.6, label=diagnosis)

plt.title("Распределение признака mean radius")
plt.xlabel(feature)
plt.ylabel("Количество")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# TODO: порог = середина между средними benign и malignant
threshold = (mean_by_class["benign"] + mean_by_class["malignant"] / 2)

# TODO: prediction по правилу if
df["prediction"] = df[feature].apply(
    lambda x: "malignant" if x > threshold else "benign"
)

print("Порог:", round(threshold, 2))
print(df[[feature, "diagnosis", "prediction"]].head(10))

assert threshold > 0
assert set(df["prediction"].unique()).issubset({"malignant", "benign"})

# TODO: посчитайте количество верных ответов
correct = (df["diagnosis"] == df["prediction"]).sum()
total = len(df)
accuracy = correct / total

print("Верных ответов:", correct)
print("Всего объектов:", total)
print("Accuracy:", round(accuracy, 3))

# TODO: выберите строки, где diagnosis не равно prediction
mistakes = df[df["diagnosis"] != df["prediction"]]

print("Количество ошибок:", len(mistakes))
print(mistakes[[feature, "diagnosis", "prediction"]].head(10))

report = pd.DataFrame([
    {"metric": "rows", "value": len(df)},
    {"metric": "feature", "value": feature},
    {"metric": "threshold", "value": round(threshold, 3)},
    {"metric": "accuracy", "value": round(accuracy, 3)},
    {"metric": "mistakes", "value": len(mistakes)},
])

report_path = "block03_simple_breast_cancer_report.csv"

# TODO: сохраните отчёт в CSV
report.to_csv(report_path, index=False)

print(report)
print("Файл сохранён:", report_path)

print("\nВывод:")
print("Мы сделали простой ИИ-подобный алгоритм на одном признаке.")
print("Он работает лучше случайного выбора, но ошибается и не является медицинской диагностикой.")
