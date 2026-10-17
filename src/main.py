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

from pathlib import Path
import numpy as np

from block04_linear_algebra import dot, norm2, cosine_similarity, matvec, vector_length_2d
from block04_visualization import save_histogram, save_scatter, save_regression_plot, save_vectors_2d

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

def demo_linear_algebra() -> dict:
    u = np.array([1.5, 2.5, 3.5])
    v = np.array([2.5, 1.5, 0.5])
    X = np.array([
        [0.1, 0.0, 0.2],
        [0.0, 0.2, 0.1],
        [0.2, 0.0, 0.1],
        [0.0, 0.1, 0.2],
        [0.1, 0.2, 0.0],
    ])
    w = np.array([0.5, -1.0, 2.0])
    v1 = np.array([2.0, 1.0])
    v2 = np.array([1.0, 3.0])
    v_sum = v1 + v2
    save_vectors_2d({"v1": v1, "v2": v2, "v1+v2": v_sum}, REPORTS_DIR / "vectors.png")
    return {
        "dot": dot(u, v),
        "norm_u": norm2(u),
        "cosine": cosine_similarity(u, v),
        "matvec": matvec(X, w).tolist(),
        "vector_length_2d": vector_length_2d(v1),
    }


def main() -> None:
    report = {
        "linear_algebra": demo_linear_algebra(),
    }

    report_path = REPORTS_DIR / "block04_report.txt"
    with report_path.open("w", encoding="utf-8") as file:
        for section, values in report.items():
            file.write(f"\n## {section}\n")
            for key, value in values.items():
                file.write(f"{key}: {value}\n")

    print("Проект блока 4 выполнен.")
    print("Отчёт сохранён:", report_path)


if __name__ == "__main__":
    main()

client_name = "ООО Жук"
orders_count = 15
check = 1860.5
is_vip = True

print("Название клиента:", client_name, "| тип:", type(client_name).__name__)
print("Количество заказов:", orders_count, "| тип:", type(orders_count).__name__)
print("Цена:", check, "| тип:", type(check).__name__)

price = 3500
quantity = 6
discount_rate = 0.50
bonus = 50

subtotal = price * quantity
discount_amount = subtotal * discount_rate
total = subtotal - discount_amount

print("Цена:", price)
print("Количество:", quantity)
print("Сумма без скидки:", subtotal)
print("Сумма скидки:", discount_amount)
print("Бонусы:", bonus)
print("Итог к оплате:", total)

price_text = "5999.90"
qty_text = "5"

price_num = float(price_text)
qty_num = int(qty_text)

total_sum = price_num * qty_num

print("Исходная цена как текст:", price_text, "| тип:", type(price_text).__name__)
print("Цена после преобразования:", price_num, "| тип:", type(price_num).__name__)
print("Количество после преобразования:", qty_num, "| тип:", type(qty_num).__name__)
print("Итоговая сумма:", total_sum)

products = ["Телевизор", "Колонки", "Саббуфер"]
prices = [50000, 2500, 5000]
quantities = [6, 3, 4]

print("Мини-таблица товаров:")
for i in range(len(products)):
    row_total = prices[i] * quantities[i]
    print(f"{i + 1}. {products[i]} | цена: {prices[i]} | количество: {quantities[i]} | сумма: {row_total}")

print("\nКоличество товаров:", len(products))
print("Максимальная цена:", max(prices))

order = {
    "product": "Телевизор",
    "price": 50000,
    "quantity": 2,
    "discount_rate": 0.50
}

revenue = order["price"] * order["quantity"]
discount = revenue * order["discount_rate"]
final_total = revenue - discount

print("Товар:", order["product"])
print("Выручка без скидки:", revenue)
print("Сумма скидки:", discount)
print("Итог к оплате:", final_total)

client_name = "  Рома Жуков  "
product_code = "AI-COURSE-2026"
city = "Казань"

# TODO:
# 1. Выведите client_name, product_code и city
# 2. Создайте переменные client_name_length и product_code_length
client_name_length = 5
product_code_length = 5

print("Исходное имя клиента:", repr(client_name))
print("Длина строки client_name:", client_name_length)
print("Код продукта:", product_code)
print("Длина кода продукта:", product_code_length)
print("Город:", city)

product_code = "AI-COURSE-2026"

# TODO:
first_symbol = product_code[0]
last_symbol = product_code[-1]
prefix = product_code[0:2]
year_part = product_code[-4:]

print("Первый символ:", first_symbol)
print("Последний символ:", last_symbol)
print("Префикс:", prefix)
print("Год:", year_part)

raw_category = "  Nokia 3310  "

# TODO:
clean_category = raw_category.strip()
lower_category = clean_category.lower()
upper_category = clean_category.upper()
replaced_category = lower_category.replace("-", " ")

print("Исходная строка:", repr(raw_category))
print("После strip():", repr(clean_category))
print("После lower():", lower_category)
print("После upper():", upper_category)
print("После replace():", replaced_category)

first_name = "Роман"
last_name = "Жуков"
department = "IT Lab"

# TODO:
full_name = first_name + " " + last_name
email = first_name.lower() + "." + last_name.lower() + "@example.com"
label = f"{full_name} | отдел: {department}"

print("Полное имя:", full_name)
print("E-mail:", email)
print("Подпись:", label)

raw_product_name = "  консоль-Playstation 5  "
raw_brand = "  wandAVision "
raw_category = "  Приставка "

# TODO:
product_name = raw_product_name.strip().replace("-", " ")
brand = raw_brand.strip().upper()
category = raw_category.strip().lower()
card_label = f"{brand} | {product_name} | категория: {category}"
print("Очищенное название товара:", product_name)
print("Бренд:", brand)
print("Категория:", category)
print("Итоговая карточка:", card_label)

order_amount = 15200
free_delivery_threshold = 11000
discount_percent = 20

# TODO:
# 1. Выведите сумму заказа и порог
# 2. Проверьте, больше ли сумма заказа порога
# 3. Проверьте, равна ли сумма заказа порогу
# 4. Проверьте, не равна ли скидка нулю
# 5. Проверьте, не больше ли скидка 15%

is_more_than_threshold = True
is_equal_to_threshold = False
discount_not_zero = True
discount_not_more_than_15 = True

print("Сумма заказа:", order_amount)
print("Порог бесплатной доставки:", free_delivery_threshold)
print("Сумма заказа больше порога?", is_more_than_threshold)
print("Сумма заказа равна порогу?", is_equal_to_threshold)
print("Скидка не равна нулю?", discount_not_zero)
print("Скидка не больше 15%?", discount_not_more_than_15)

order_amount = 9700
free_delivery_threshold = 20000

# TODO:
# Если сумма заказа больше или равна порогу,
# присвойте delivery_status значение "Бесплатная доставка",
# иначе "Платная доставка"

if order_amount >= free_delivery_threshold:
    delivery_status = "Бесплатная доставка"
else:
    delivery_status = "Платная доставка"
print("Сумма заказа:", order_amount)
print("Статус доставки:", delivery_status)

order_amount = 21500

# TODO:
# 1. Если сумма >= 20000, скидка 15%
# 2. Если сумма >= 10000, скидка 10%
# 3. Если сумма >= 5000, скидка 5%
# 4. Иначе скидки нет

if order_amount >= 20000:
    discount_level = "Скидка 15%"
elif order_amount >= 10000:
    discount_level = "Скидка 10%"
elif order_amount >= 5000:
    discount_level = "Скидка 5%"
else:
    discount_level = "Скидки нет"

print("Сумма заказа:", order_amount)
print("Уровень скидки:", discount_level)

order_amount = 15000
is_new_client = True
has_debt = False
express_delivery = True

# TODO:
# 1. Создайте переменную manual_review
# 2. Ручная проверка нужна, если:
#    - сумма заказа больше 20000 И клиент новый
#      ИЛИ
#    - есть задолженность
#      ИЛИ
#    - заказ срочный
# 3. Также выведите, что клиент без долга через not

manual_review = (order_amount > 20000 and is_new_client) or (has_debt or express_delivery)
client_without_debt = False

print("Сумма заказа:", order_amount)
print("Новый клиент:", is_new_client)
print("Есть задолженность:", has_debt)
print("Срочная доставка:", express_delivery)
print("Нужна ручная проверка?", manual_review)
print("Клиент без долга?", client_without_debt)

request_amount = 25000
documents_ready = True
manager_approved = True
client_blacklisted = False

# TODO:
# Определите request_status по правилам:
# 1. Если клиент в чёрном списке -> "Отклонить заявку"
# 2. Если документы готовы, менеджер одобрил и сумма <= 15000 -> "Одобрить автоматически"
# 3. Если документы готовы, но менеджер не одобрил -> "Отправить менеджеру"
# 4. Иначе -> "Запросить документы"

if client_blacklisted:
    request_status = "Отклонить заявку"
elif documents_ready and manager_approved and request_amount <= 15000:
    request_status = "Одобрить автоматически"
elif documents_ready and not manager_approved:
    request_status = "Отправить менеджеру"
else:
    request_status = "Запросить документы"

print("Сумма заявки:", request_amount)
print("Документы готовы:", documents_ready)
print("Менеджер одобрил:", manager_approved)
print("Клиент в чёрном списке:", client_blacklisted)
print("Итоговый статус:", request_status)

for day in range(2, 8):
    print(f"День {day}: обработка данных запрещена")

sales = [1600, 1300, 563, 2150, 1350]

# TODO:
# 1. Пройдите циклом по списку sales
# 2. Выведите каждую продажу в формате:
#    Продажа за день: ...

for sale in sales:
    print("Продажа за день:", sale)

sales = [1600, 1300, 563, 2150, 1350]
total_sales = 0

# TODO:
# 1. Пройдите циклом по sales
# 2. Накапливайте общую сумму в total_sales

for sale in sales:
    total_sales += sale

print("Общая сумма продаж:", total_sales)

sales = [1600, 1300, 563, 2150, 1350]
threshold = 1700
count_above_threshold = 0

# TODO:
# 1. Пройдите циклом по sales
# 2. Если sale > threshold, увеличьте count_above_threshold на 1

for sale in sales:
    if sale > threshold:
      count_above_threshold += 1

print("Порог:", threshold)
print("Количество продаж выше порога:", count_above_threshold)

sales = [1600, 1300, 563, 2150, 1350, 1800, 1400]
threshold = 1700

total_sales = 0
days_count = 0
days_above_threshold = 0

# TODO:
# 1. Пройдите циклом по sales
# 2. Посчитайте total_sales
# 3. Посчитайте days_count
# 4. Посчитайте days_above_threshold
# 5. После цикла найдите average_sale

for sale in sales:
    total_sales += sale
    days_count += 1
    if sale > threshold:
       days_above_threshold += 1

average_sale = total_sales / days_count

print("Список продаж:", sales)
print("Общая сумма:", total_sales)
print("Количество дней:", days_count)
print("Средняя продажа:", round(average_sale, 2))
print("Дней выше порога:", days_above_threshold)

products = ["Миксер", "Блендер", "Телевизор", "Саббуфер"]

# TODO:
# 1. Выведите весь список products
# 2. Выведите первый товар
# 3. Выведите последний товар
# 4. Выведите количество товаров

first_product = "Миксер"
last_product = "Саббуфер"
products_count = len(products)

print("Список товаров:", products)
print("Первый товар:", first_product)
print("Последний товар:", last_product)
print("Количество товаров:", products_count)

products = ["Миксер", "Блендер", "Телевизор", "Саббуфер"]

# TODO:
# 1. Замените "Мышь" на "Беспроводная мышь"
# 2. Добавьте в список "Гарнитура"

products[1] = "Наушники"
products.append("Техника")

print("Обновлённый список:", products)

order = {
    "product": "Телевизор",
    "price": 80000,
    "quantity": 5,
    "client": "ООО Сумрак"
}

# TODO:
# 1. Выведите весь словарь
# 2. Выведите значение ключа "product"
# 3. Выведите значение ключа "price"
# 4. Выведите список ключей
# 5. Выведите список значений

product_name = order["product"]
product_price = order["price"]
order_keys = list(order.keys())
order_values = list(order.values())

print("Словарь заказа:", order)
print("Товар:", product_name)
print("Цена:", product_price)
print("Ключи словаря:", order_keys)
print("Значения словаря:", order_values)

orders = [
    {"product": "Телевизор", "price": 80000, "quantity": 5},
    {"product": "Миксер", "price": 5000, "quantity": 4},
    {"product": "Блендер", "price": 8000, "quantity": 3},
]

# TODO:
# 1. Пройдите циклом по orders
# 2. Для каждой записи посчитайте total = price * quantity
# 3. Выведите product и total

for row in orders:
    total = row["price"] * row["quantity"]
    print("Товар:", row["product"], "| сумма:", total)

orders = [
    {"product": "Телевизор", "price": 80000, "quantity": 5},
    {"product": "Миксер", "price": 5000, "quantity": 4},
    {"product": "Блендер", "price": 8000, "quantity": 3},
    {"product": "Наушники", "price": 1000, "quantity": 10},
]

total_revenue = 0

# TODO:
# 1. Пройдите циклом по orders
# 2. Для каждой записи посчитайте row_total
# 3. Добавьте row_total в total_revenue

for row in orders:
    row_total = row["price"] * row["quantity"]
    total_revenue += row_total

print("Количество заказов:", len(orders))
print("Общая выручка:", total_revenue)

import pandas as pd
from pathlib import Path

file_path = Path("lesson_08_filter_sort_calc.xlsx")

# TODO:
# 1. Загрузите лист sales_data в DataFrame df
# 2. Выведите размер таблицы
# 3. Выведите список столбцов
# 4. Покажите первые строки таблицы

df = pd.read_excel(file_path, sheet_name="sales_data", header=1)

print("Размер таблицы:", df.shape)
print("\nНазвания столбцов:")
print(list(df.columns))

df.head()

notebooks_df = df[df["category"] == "Электроника"]

print("Количество заказов в категории 'Электроника':", len(notebooks_df))
notebooks_df

moscow_online_df = df[(df['city'] == "Москва") & (df["channel"] == "Интернет-магазин")]

print("Количество заказов из Москвы через онлайн-канал:", len(moscow_online_df))
moscow_online_df

sorted_by_price = df.sort_values(by="price", ascending=False)

print("Первые 5 заказов после сортировки по цене:")
sorted_by_price.head()

df_calc = df.copy()
df_calc["revenue"] = df_calc["quantity"] * df_calc["price"]
big_orders = df_calc[df_calc["revenue"] >= 100000].sort_values(by="revenue", ascending=False)

print("Общая выручка:", df_calc["revenue"].sum())
print("Количество крупных заказов:", len(big_orders))

big_orders

import pandas as pd
from pathlib import Path

file_path = Path("lesson_09_groupby_pivot.xlsx")

# TODO:
# 1. Загрузите лист sales_data в DataFrame df
# 2. Создайте столбец revenue = quantity * price
# 3. Выведите размер таблицы
# 4. Посчитайте количество заказов
# 5. Посчитайте общую, среднюю, максимальную и минимальную выручку
# 6. Покажите первые строки таблицы

df = pd.read_excel(file_path, sheet_name="sales_data", header=1)

df["revenue"] = df["quantity"] * df["price"]

print("Размер таблицы:", df.shape)
print("Количество заказов:", df["order_id"].count())
print("Общая выручка:", int(df["revenue"].sum()))
print("Средняя выручка заказа:", round(df["revenue"].mean(), 2))
print("Максимальная выручка заказа:", int(df["revenue"].max()))
print("Минимальная выручка заказа:", int(df["revenue"].min()))

df.head()

manager_summary = (
    df.groupby("manager", as_index=False)
       .agg(
           total_revenue=("revenue", "sum"),
           orders=("order_id", "count"),
           total_quantity=("quantity", "sum"),
           avg_revenue=("revenue","mean")
       )
)

manager_summary["avg_revenue"] = manager_summary["avg_revenue"].round(2)

manager_summary

month_order = ["Январь", "Февраль", "Март", "Апрель"]
df["month"] = pd.Categorical(df["month"], categories=month_order, ordered=True)
month_category_summary = (
    df.groupby(["month", "category"], as_index=False, observed=True)
    .agg(
        total_revenue=("revenue", "sum"),
        total_quantity=("quantity", "sum"),
        orders=("order_id", "count")
    )
    .sort_values(["month", "total_revenue"], ascending=[True, False])
)

month_category_summary

manager_sorted = manager_summary.sort_values(by="total_revenue", ascending=False)
top_manager = manager_sorted.iloc[0]["manager"]
top_manager_revenue = int(manager_sorted.iloc[0]["total_revenue"])

print("Лидер по выручке:", top_manager)
print("Выручка лидера:", top_manager_revenue)

manager_sorted

pivot = pd.pivot_table(
    df,
    values="revenue",
    index="manager",
    columns="category",
    aggfunc="sum",
    fill_value=0
)
pivot = pivot[["Электроника", "Расходные материалы", "Офисная мебель", "Канцелярия"]]

best_category = pivot.sum(axis=0).idxmax()
best_electronics_manager = pivot["Электроника"].idxmax()

print("Лучшая категория по выручке:", best_category)
print("Сильнейший менеджер в категории 'Ноутбуки':", best_electronics_manager)

pivot

def hello():
    print("Привет! Это первая функция блока 6.")

# TODO: вызовите функцию
hello()

def greet(name):
  message = f"Привет, {name}! Добро пожаловать в блок анализа данных."
# TODO: сформируйте message

# TODO: верните message
  return message
# TODO: вызовите функцию
result = greet("Вася")
# TODO: выведите результат
print(result)

def square(x):
# TODO: верните x * x
    return x * x
# TODO: вызовите функцию для числа 5
result = square(10)
# TODO: выведите результат
print("Квадрат числа:", result)

def calculate_sum(numbers):

# TODO: верните sum(numbers)
    return sum(numbers)
# TODO: создайте список values
values = [6, 7, 8, 9]
# TODO: вызовите функцию
result = calculate_sum(values)
print("Сумма:", result)

def calculate_mean(numbers):
# TODO: верните среднее значение
    return sum(numbers)/len(numbers)
# TODO: создайте список values
values = [40, 50, 60]
mean_value = calculate_mean(values)
# TODO: вызовите функцию
print("Среднее значение:", mean_value)

def find_max(numbers):

# TODO: верните max(numbers)
    return max(numbers)
# TODO: создайте список values
values = [6, 15, 2]
max_value = find_max(values)

# TODO: вызовите функцию
print("Максимум:", max_value)

def calculate_statistics(numbers):
# TODO: внутри создайте словарь statistics
    statistics = {
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers)
    }
# TODO: верните statistics
    return statistics
# TODO: вызовите функцию
stats = calculate_statistics([40, 50, 60])
print(stats)

sales = [130, 160, 210, 180, 310]
# TODO: получите sales_stats
sales_stats = calculate_statistics(sales)
# TODO: выведите результат
print("Статистика продаж:")
print(sales_stats)

calories = [260, 310, 290, 350]
# TODO: получите calories_stats
calories_stats = calculate_statistics(calories)
# TODO: выведите результат
print("Статистика тренировок:")
print(calories_stats)

def generate_report(numbers, title="Отчёт по данным"):
# TODO: получите stats через calculate_statistics
    stats = calculate_statistics(numbers)
# TODO: напечатайте заголовок и статистику
    print("=" * 40)
    print(title)
    print("=" * 40)
    print("Минимум:", stats["min"])
    print("Максимум:", stats["max"])
    print("Среднее:", stats["mean"])
# TODO: верните stats
    return stats
# TODO: вызовите функцию
report = generate_report([50, 60, 70, 80], title="Учебный отчёт")

def greet(name="Студент"):
    return f"Привет, {name}!"

print(greet())
print(greet("Иван"))

def create_user(name, age):
    return {"name": name, "age": age}
user = create_user(age=25, name="Гриша")
print(user)

def calculate_mean(a, b, c):
  return (a+b+c)/3

result = calculate_mean(15, 25, 30)

def calculate_sum(*args):
    return sum(args)
result = calculate_sum(6,7,8,9,10)
print(result)

def print_info(**kwargs):
    return kwargs
info = print_info(name="Вася", city="Екатеринбург")

print(info)

def statistics(*values):
    return {
        "min": min(values),
        "max": max(values),
        "mean": sum(values)/len(values)
    }
stats = statistics(50,60,70,80)

sales = [150, 250, 350, 400]

stats = statistics(*sales)

print(stats)

calories = [300, 400, 380, 420]

stats = statistics(*calories)

def create_report(title="Отчёт", **data):
    print(title)
    for k,v in data.items():
        print(k,":", v)

create_report("Продажи", min=150, max=350)

def analyze_dataset(name, *values):
    stats = statistics(*values)

    return {
        "dataset": name,
        **stats
    }

report = analyze_dataset("sales", 150,250,350)

print(report)

statistics_module = '''
def calculate_mean(values):
    return sum(values)/len(values)
'''
print(statistics_module)

project_structure = [
    "src/main.py",
    "src/statistics_utils.py",
    "src/report_utils.py"
]

print(project_structure)

example = "from statistics_utils import calculate_mean"
print(example)

def calculate_mean(values):
    return sum(values)/len(values)

def create_report(values):
    return {
        "mean": sum(values)/len(values)
    }

def calculate_max(values):
    return max(values)

def analyze(values):
    return {
        "mean": sum(values)/len(values),
        "max": max(values)
    }

print(analyze([15,25,35]))

sales=[150, 250, 200]
result=analyze(sales)

main_example = '''
def main():
  print("DataAnalyzer")

if __name__ == "__main__":
   main()
'''
print(main_example)

final_structure = {
    "src":[
        "main.py",
        "statistics_utils.py",
        "report_utils.py"
    ]
}

print(final_structure)

class Manager:
    pass
# TODO: создайте объект student
manager = Manager()
# TODO: выведите объект и его тип
print(manager)
print(type(manager))

manager = Manager()
# TODO: добавьте student.name
manager.name = "Иванов А.С."
# TODO: добавьте student.age
manager.quantity = 5
# TODO: выведите значения
print("Имя:", manager.name)
print("Кол-во:", manager.quantity)

class ManagerWithInit:

# TODO: добавьте __init__
     def __init__(self, name, quantity):
         self.name = name
         self.quantity = quantity
# TODO: создайте объект
manager = ManagerWithInit("Иванов А.С.", 5)
# TODO: выведите атрибуты
print(manager.name)
print(manager.quantity)

class ManagerProfile:

# TODO: добавьте __init__
     def __init__(self, name, quantity):
         self.name = name
         self.quantity = quantity
# TODO: добавьте метод get_info
     def get_info(self):
         return f"Менеджер: {self.name}, Кол-во: {self.quantity}"
# TODO: создайте объект
manager = ManagerProfile("Иванов А.С.", 5)
# TODO: вызовите get_info
info = manager.get_info()
print(info)

class Product:
# TODO: добавьте __init__
    def __init__(self, name, price, quantity):
       self.name = name
       self.price = price
       self.quantity = quantity
# TODO: добавьте метод get_total_price
    def get_total_price(self):
        return self.price * self.quantity
# TODO: создайте объект product
product = Product("Телевизор LG", 60000, 5)
# TODO: получите total
total = product.get_total_price()
print("Общая стоимость:", total)

products = [
    Product("Телевизор", 60000, 5),
    Product("Колонки", 2000, 10),
    Product("Умные часы", 5000, 6)
]
# TODO: создайте total_sum = 0
total_sum = 0
# TODO: в цикле сложите стоимость товаров
for product in products:
    total_sum += product.get_total_price()
    print(product.name, product.get_total_price())
# TODO: выведите итог
print("Итоговая сумма:", total_sum)

class Dataset:
    # TODO: добавьте __init__
     def __init__(self, name, values):
        self.name = name
        self.values = values
# TODO: добавьте get_size
     def get_size(self):
         return len(self.values)
# TODO: создайте объект dataset
dataset = Dataset("sales", [150, 250, 200, 350])
print("Название:", dataset.name)
print("Размер:", dataset.get_size())

class DatasetAnalyzer:
# TODO: добавьте __init__
      def __init__(self, values):
        self.values = values
# TODO: добавьте get_min
      def get_min(self):
        return min(self.values)
# TODO: добавьте get_max
      def get_max(self):
        return max(self.values)
# TODO: добавьте get_mean
      def get_mean(self):
        return sum(self.values) / len(self.values)
# TODO: создайте объект analyzer
analyzer = DatasetAnalyzer([15, 25, 35, 45])
print("Минимум:", analyzer.get_min())
print("Максимум:", analyzer.get_max())
print("Среднее:", analyzer.get_mean())

# TODO: создайте класс DatasetAnalyzerWithReport
class DatasetAnalyzerWithReport:
# TODO: добавьте __init__
   def __init__(self, name, values):
       self.name = name
       self.values = values
# TODO: добавьте методы get_min, get_max, get_mean
   def get_min(self):
       return min(self.values)
   def get_max(self):
       return max(self.values)
   def get_mean(self):
       return sum(self.values) / len(self.values)
# TODO: добавьте get_report
   def get_report(self):
       return {
           "dataset": self.name,
           "min": self.get_min(),
           "max": self.get_max(),
           "mean": self.get_mean()
       }
# TODO: создайте объект
analyzer = DatasetAnalyzerWithReport("calories", [300, 350, 480, 520])
# TODO: получите report
report = analyzer.get_report()
print(report)

sales_analyzer = DatasetAnalyzerWithReport(
    "sales",
     [140, 160, 250, 180, 350]
)
# TODO: получите sales_report
sales_report = sales_analyzer.get_report()
# TODO: напечатайте отчёт
print("=" * 40)
print("Отчёт по датасету:", sales_report["dataset"])
print("=" * 40)
print("Минимум:", sales_report["min"])
print("Максимум:", sales_report["max"])
print("Среднее:", sales_report["mean"])

# TODO: выполните задание ячейки 1
class Dataset:
  def __init__(self, surname, quantity):
      self.surname = surname
      self.quantity = quantity

dataset = Dataset("sales", [6,10,12])


# TODO: выполните задание ячейки 2
class Analyzer:
  def __init__(self, quantity):
    self.quantity = quantity

  def mean(self):
      return sum(self.quantity)/len(self.quantity)

a = Analyzer([14, 20, 26])


# TODO: выполните задание ячейки 3
class Report:
     def __init__(self, surname):
         self.surname = surname
report = Report("Иванов")

# TODO: выполните задание ячейки 4
dataset = Dataset("sales",[150, 250, 350])
analyzer = Analyzer(dataset.quantity)

# TODO: выполните задание ячейки 5
class Analyzer:
    def __init__(self, quantity):
      self.quantity = quantity
    def minimum(self):
      return min(self.quantity)
    def maximum(self):
      return max(self.quantity)
a=Analyzer([15,25,35])

# TODO: выполните задание ячейки 6
class Analyzer:
  def __init__(self, quantity):
      self.quantity = quantity
  def report(self):
      return {
          "min": min(self.quantity),
          "max": max(self.quantity)
      }
r = Analyzer([15,25,35]).report()

# TODO: выполните задание ячейки 7
class DatasetAnalyzer:
  def __init__(self,dataset):
    self.dataset = dataset

  def report(self):
      return {
          "dataset": self.dataset.surname,
          "count": len(self.dataset.quantity)
      }
da = DatasetAnalyzer(dataset)

# TODO: выполните задание ячейки 8
sales = Dataset("sales", [160, 180, 220])
da = DatasetAnalyzer(sales)
print(da.report())

# TODO: выполните задание ячейки 9
training = Dataset("training",[280, 350, 240, 370])
da = DatasetAnalyzer(training)

# TODO: выполните задание ячейки 10
project = {
    "Dataset":"хранение данных",
    "Analyzer":"анализ данных",
    "Report":"формирование отчета"
}

print(project)

import numpy as np
# TODO: выведите сообщение
print("Numpy подключён")
# TODO: выведите версию NumPy
print("Версия Numpy:", np.__version__)

# TODO: создайте values_list
quantity_list = [6, 15, 24, 35, 41]
# TODO: создайте values_array = np.array(values_list)
quantity_array = np.array(quantity_list)
# TODO: выведите массив и тип
print(quantity_list)
print(type(quantity_array))
# TODO: выведите размер
print("Размер:", quantity_array.size)

# TODO: создайте values
quantity = np.array([15, 25, 35])
# TODO: создайте double_values
double_quantity = quantity * 2

# TODO: создайте plus_values
plus_quantity = quantity + 10
# TODO: выведите результаты
print("Исходные:", quantity)
print("Умножение на 2:", double_quantity)
print("Плюс 10:", plus_quantity)

# TODO: создайте sales
sales = np.array([130, 160, 210, 180, 320])
# TODO: найдите min_value
min_value = np.min(sales)
# TODO: найдите max_value
max_value = np.max(sales)
# TODO: найдите mean_value
mean_value = np.mean(sales)
# TODO: найдите sum_value
sum_value = np.sum(sales)
# TODO: выведите результаты
print("Минимум:", min_value)
print("Максимум:", max_value)
print("Среднее:", mean_value)
print("Сумма:", sum_value)

# TODO: создайте sales
sales = np.array([130, 160, 210, 180, 320])
# TODO: создайте high_sales
high_sales = sales[sales > 180]
# TODO: выведите high_sales
print("Продажи больше 180:", high_sales)

# TODO: создайте values
values = np.array([6, 11, 16, 24, 27, 32])
# TODO: получите first_value
first_value = values[0]
# TODO: получите last_value
last_value = values[-1]
# TODO: получите middle_values
middle_values = values[2:5]
# TODO: выведите результаты
print("Первый:", first_value)
print("Последний:", last_value)
print("Срез:", middle_values)

# TODO: создайте table
table = np.array([
    [15, 25, 35],
    [45, 55, 65],
    [75, 85, 95]
])
# TODO: выведите table и table.shape
print(table)
print("Форма:", table.shape)
# TODO: создайте row_sums
row_sums = np.sum(table, axis=1)
column_sums = np.sum(table, axis=0)
# TODO: создайте column_sums
print("Суммы по строках:", row_sums)
print("Суммы по столбцам:", column_sums)

# TODO: создайте values
values = np.array([150, 250, 350, 450, 550])
# TODO: создайте normalized
normalized = (values - np.min(values)) / (np.max(values) - np.min(values))
# TODO: выведите normalized
print("Исходные:", values)
print("Нормализованные:", normalized)

# TODO: создайте функцию analyze_array(values)
def analyze_array(values):
# TODO: внутри создайте array = np.array(values)
    array = np.array(values)
# TODO: верните словарь min, max, mean, sum
    return {
        "min": np.min(array),
        "max": np.max(array),
        "mean": np.mean(array),
        "sum": np.sum(array)
    }
# TODO: вызовите функцию
result = analyze_array([15, 25, 35, 45])
print(result)

# TODO: создайте calories
calories = np.array([270, 320, 300, 340, 420, 240, 370])
# TODO: получите stats
stats = analyze_array(calories)
# TODO: создайте high_load
high_load = calories[calories > 300]
# TODO: создайте normalized_calories
normalized_calories = (calories - calories.min()) / (calories.max() - calories.min())
# TODO: выведите результаты
print("Статистика:", stats)
print("Высокая нагрузка:", high_load)
print("Нормализованные данные:", normalized_calories)

# TODO: импортируйте pandas как pd
import pandas as pd
# TODO: импортируйте matplotlib.pyplot как plt
import matplotlib.pyplot as plt
from IPython.display import display
# TODO: выведите сообщение и версию Pandas
print("Pandas подключён")
print("Версия Pandas:", pd.__version__)

# TODO: создайте sales
sales = [140, 170, 220, 190, 350]
# TODO: создайте sales_series
sales_series = pd.Series(sales)
# TODO: выведите sales_series
print(sales_series)
# TODO: посчитайте среднее
print("Среднее:", sales_series.mean())

# TODO: создайте data
data = {
    "product": ["Телевизор", "Тв-приставка", "Саббуфер"],
    "price": [60000, 1000, 3500],
    "quantity": [3, 10, 8]
}
# TODO: создайте df_products
df_products = pd.DataFrame(data)
# TODO: покажите df_products
display(df_products)
# TODO: выведите shape
print("Размер:", df_products.shape)

# TODO: создайте колонку total
df_products["total"] = df_products["price"] * df_products["quantity"]
# TODO: покажите df_products
display(df_products)

# TODO: создайте url
from google.colab import drive
from pathlib import Path
drive.mount('/content/drive')
file_path = Path("/content/drive/MyDrive/Базы/sales_data.xlsx")
df = pd.read_excel(file_path, sheet_name="sales_data", header=0)
# TODO: загрузите df

# TODO: покажите df.head()
display(df.head())

# TODO: выведите df.shape
print("Размер таблицы:", df.shape)
print()
# TODO: выведите df.columns.tolist()
print("Колонки:")
print(df.columns.tolist())
print()
# TODO: вызовите df.info()
print("Типы данных:")
df.info()
print()
# TODO: выведите df.isna().sum()
print("Пропуски:")
print(df.isna().sum())

# TODO: создайте house_values
price_values = df["price"]
# TODO: создайте selected_df
selected_df = df [["quantity", "price", "category"]]
# TODO: выведите первые строки
print("Первые значение стоимости товара:")
print(price_values.head())
print()
print("Выбранные колонки:")
display(selected_df.head())

# TODO: создайте rich_areas
rich_areas = df[df["quantity"] > 5]
# TODO: создайте expensive_areas
expensive_areas = df[df["price"] > 5000]
# TODO: выведите количество строк
print("Кол-во товаров больше 5:", len(rich_areas))
print("Цена товара больше 5000:", len(expensive_areas))
# TODO: покажите rich_areas.head()
display(rich_areas.head())

# TODO: создайте stats
stats = df.describe()
# TODO: покажите stats
display(stats)
# TODO: создайте group_report
group_report = (
    df.groupby("category")["price"]
    .mean()
    .sort_values(ascending=False)
)
# TODO: выведите group_report
print("Средняя стоимость товара в зависимости от категорий:")
print(group_report)

# TODO: создайте report
report = {
    "rows": len(df),
    "columns": df.shape[1],
    "mean_price": df["price"].mean(),
    "max_price": df["price"].max(),
    "mean_quantity": df["quantity"].mean()
}
# TODO: выведите report
for key, value in report.items():
    print(key, ":", value)
# TODO: постройте bar chart
plt.figure(figsize=(8, 5))
group_report.plot(kind="bar")
plt.title("Средняя стоимость товара в зависимости от категорий")
plt.xlabel("Категория товара")
plt.ylabel("Средняя стоимость товара")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
# TODO: создайте conclusions
conclusions = [
    "Pandas позволяет удобно загружать и анализировать таблицы.",
    "DataFrame похож на таблицу Excel.",
    "Фильтрация помогает выбирать нужные строки.",
    "Группировка помогает строить отчёты.",
    "Pandas является основой подготовки данных для ML."
]
# TODO: выведите conclusions
for item in conclusions:
    print("-", item)

# TODO: выполните задание ячейки 1
import pandas as pd
from pathlib import Path
from google.colab import drive

drive.mount('/content/drive')

file_path = Path("/content/drive/MyDrive/Базы/sales_data.xlsx")
df = pd.read_excel(file_path, sheet_name="sales_data", header=0)

print(df.shape)

# TODO: выполните задание ячейки 2
print(df.shape)
print(df.columns.tolist())

df.info()

missing = df.isna().sum()

print(missing)

rows_with_nan = df[df.isna().any(axis=1)]

display(rows_with_nan.head())

# TODO: выполните задание ячейки 5
df_dropna = df.dropna()

print(df.shape)
print(df_dropna.shape)

# TODO: выполните задание ячейки 6
df_fillna = df.copy()
mean_quantity = df_fillna["quantity"].mean()
df_fillna["quantity"] = df_fillna["quantity"].fillna(mean_quantity)
print(df_fillna["quantity"].isna().sum())

# TODO: выполните задание ячейки 7
duplicates_df = pd.concat([df.head(5), df.head(5)])
print(duplicates_df.shape)

# TODO: выполните задание ячейки 8
duplicates_count = duplicates_df.duplicated().sum()
clean_df = duplicates_df.drop_duplicates()
print("Дубликатов:", duplicates_count)
print("После очистки:", clean_df.shape)

# TODO: выполните задание ячейки 9
prepared_df = df_fillna[
    [
        "category",
        "price",
        "quantity"
    ]
]
display(prepared_df.head())

# TODO: выполните задание ячейки 10
report = {
    "rows_before": len(df),
    "rows_after_dropna": len(df_dropna),
    "missing_before": int(df.isna().sum().sum()),
    "missing_after_fillna": int(df_fillna.isna().sum().sum()),
    "duplicates_removed": int(duplicates_count)
}

for k,v in report.items():
    print(k,":", v)

import pandas as pd

df = pd.DataFrame({
    "quantity":[8,9,10,11],
    "price":[80,90,100,110]
})

display(df)

X = df[["quantity"]]
y = df["price"]

print(X)
print(y)

import matplotlib.pyplot as plt

plt.scatter(df["quantity"], df ["price"])
plt.xlabel("Количество")
plt.ylabel("Цена")
plt.show()

# TODO: выполните задание ячейки 4
model_name = "Linear Regression"

print(model_name)

# TODO: выполните задание ячейки 5
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[90]])
print(prediction)

score = model.score(X,y)
print(score)

preds = model.predict([[75],[85],[95]])
print(preds)

pipeline = [
"данные",
"подготовка",
"обучение",
"прогноз"
]

print(pipeline)

report = {
    "rows": len(df),
    "algorithm":"LinearRegression",
    "score": score
}

print(report)

# TODO: выполните самостоятельно задание ячейки 1
import pandas as pd
from pathlib import Path
from google.colab import drive

drive.mount('/content/drive')

file_path = Path("/content/drive/MyDrive/Базы/sales_data.xlsx")
df = pd.read_excel(file_path, sheet_name="sales_data", header=0)

print(df.shape)

# TODO: выполните самостоятельно задание ячейки 2
display(df.head())

print(df.columns.tolist())

# TODO: выполните самостоятельно задание ячейки 3
X = df[["price","number","discount"]]
y = df["quantity"]

print(X.shape)
print(y.shape)

# TODO: выполните самостоятельно задание ячейки 4
data = df[["price","number","discount","quantity"]].dropna()
print(data.shape)

# TODO: выполните самостоятельно задание ячейки 5
from sklearn.model_selection import train_test_split

X = data[["price","number","discount"]]
y = data["quantity"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

print(X_train.shape)
print(X_test.shape)

# TODO: выполните самостоятельно задание ячейки 6
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(X_train_scaled[:3])

# TODO: выполните самостоятельно задание ячейки 7
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train_scaled, y_train)

# TODO: выполните самостоятельно задание ячейки 8
train_score = model.score(X_train_scaled,y_train)
test_score = model.score(X_test_scaled,y_test)

print("Train:",train_score)
print("Test:",test_score)

# TODO: выполните самостоятельно задание ячейки 9
difference = train_score - test_score

print("Разница:", difference)

# TODO: выполните самостоятельно задание ячейки 10
report = {
    "rows": len(data),
    "features": len(X.columns),
    "train_score": round(train_score,3),
    "test_score": round(test_score,3)
}

print(report)

# TODO: выполните самостоятельно задание ячейки 1
import pandas as pd
from pathlib import Path
from google.colab import drive

drive.mount('/content/drive')

file_path = Path("/content/drive/MyDrive/Базы/sales_data.xlsx")
df = pd.read_excel(file_path, sheet_name="sales_data", header=0)

print(df.shape)

# TODO: выполните самостоятельно задание ячейки 2
data=df[["price", "quantity", "discount", "number"]].dropna()

X=data[["price", "quantity", "discount"]]
y=data["number"]

# TODO: выполните самостоятельно задание ячейки 3
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

# TODO: выполните самостоятельно задание ячейки 4
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

# TODO: выполните самостоятельно задание ячейки 5
from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(X_train_scaled, y_train)

# TODO: выполните самостоятельно задание ячейки 6
for name,coef in zip(X.columns,model.coef_):
  print(name, round(coef, 2))

print("Intercept:", round(model.intercept_,2))

# TODO: выполните самостоятельно задание ячейки 7
predictions=model.predict(X_test_scaled)

print(predictions[:5])

# TODO: выполните самостоятельно задание ячейки 8
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score
import numpy as np

mae=mean_absolute_error(y_test,predictions)
mse=mean_squared_error(y_test,predictions)
rmse=np.sqrt(mse)
r2=r2_score(y_test,predictions)

print("MAE",mae)
print("MSE",mse)
print("RMSE",rmse)
print("R2",r2)

# TODO: выполните самостоятельно задание ячейки 9
import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))
plt.scatter(y_test,predictions,alpha=0.3)
plt.xlabel("Факт")
plt.ylabel("Прогноз")
plt.title("Линейная регрессия")
plt.show()

# TODO: выполните самостоятельно задание ячейки 10
report={
    "rows":len(data),
    "features":len(X.columns),
    "MAE":round(mae,2),
    "RMSE":round(rmse,2),
    "R2":round(r2,3)
}

print(report)

# TODO: выполните самостоятельно задание ячейки 1
import pandas as pd
from pathlib import Path
from google.colab import drive

drive.mount('/content/drive')

file_path = Path("/content/drive/MyDrive/Базы/sales_data.xlsx")
df = pd.read_excel(file_path, sheet_name="sales_data", header=0)

print(df.shape)

# TODO: выполните самостоятельно задание ячейки 2
display(df.head())
print(df.columns.tolist())

# TODO: выполните самостоятельно задание ячейки 3
data=df[[
    "number",
    "quantity",
    "price",
    "discount"
]].dropna()

X=data.drop(columns=["quantity"])
y=data["quantity"]

# TODO: выполните самостоятельно задание ячейки 4
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
    )

# TODO: выполните самостоятельно задание ячейки 5
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

# TODO: выполните самостоятельно задание ячейки 6
from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(X_train_scaled,y_train)

# TODO: выполните самостоятельно задание ячейки 7
importance=pd.DataFrame({
    "feature":X.columns,
    "coefficient":model.coef_
})

importance=importance.sort_values(
    by="coefficient",
    ascending=False
)

display(importance)

# TODO: выполните самостоятельно задание ячейки 8
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

pred=model.predict(X_test_scaled)

mae=mean_absolute_error(y_test,pred)
rmse=np.sqrt(mean_squared_error(y_test,pred))
r2=r2_score(y_test,pred)

print(mae,rmse,r2)

# TODO: выполните самостоятельно задание ячейки 9
import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))
plt.scatter(y_test,pred,alpha=0.3)
plt.xlabel("Факт")
plt.ylabel("Прогноз")
plt.title("Недвижимость: факт и прогноз")
plt.show()

# TODO: выполните самостоятельно задание ячейки 10
report={
    "rows":len(data),
    "features":len(X.columns),
    "MAE":round(mae,2),
    "RMSE":round(rmse,2),
    "R2":round(r2,3),
    "best_feature":importance.iloc[0]["feature"]
}

print(report)

from sklearn.datasets import load_breast_cancer
import pandas as pd

data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

print(X.shape)
print(y.shape)

display(X.head())

print("Классы:", y.unique())

class_counts = y.value_counts()

print(class_counts)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=55
)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=6000)

model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)

print(predictions[:12])

probabilities = model.predict_proba(X_test_scaled)

print(probabilities[:10])

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)

report = {
    "rows": len(X),
    "features": X.shape[1],
    "accuracy": round(accuracy, 3),
    "precision": round(precision, 3),
    "recall": round(recall, 3),
    "f1": round(f1, 3)
}

print(report)

# TODO: импортируйте pandas как pd
import pandas as pd
# TODO: импортируйте matplotlib.pyplot как plt
import matplotlib.pyplot as plt
# TODO: импортируйте load_breast_cancer
from sklearn.datasets import load_breast_cancer
# TODO: импортируйте train_test_split
from sklearn.model_selection import train_test_split
# TODO: импортируйте StandardScaler
from sklearn.preprocessing import StandardScaler
# TODO: импортируйте LogisticRegression
from sklearn.linear_model import LogisticRegression
# TODO: импортируйте метрики:
# accuracy_score, precision_score, recall_score, f1_score,
# confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

print("Библиотеки подключены")

# TODO: загрузите data = load_breast_cancer()
import pandas as pd
from pathlib import Path
from google.colab import drive

drive.mount('/content/drive')

file_path = Path("/content/drive/MyDrive/Базы/sales_data.xlsx")
data = pd.read_excel(file_path, sheet_name="sales_data", header=0)
# TODO: создайте X как DataFrame
X = data
# TODO: создайте y как Series
y = data['category']
# TODO: выведите размеры и классы
print("Размер X:", X.shape)
print("Размер y:", y.shape)
print("Классы:", y.unique())


# TODO: создайте class_counts
class_counts = y.value_counts().sort_index()
# TODO: выведите class_counts
print("Распределение классов:")
print(class_counts)
# TODO: постройте bar chart
plt.figure(figsize=(8, 10))
class_counts.plot(kind="bar")
plt.title("Распределение классов")
plt.xlabel("Класс")
plt.ylabel("Количество объектов")
plt.grid(True)
plt.show()


# TODO: выполните train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=55,
    stratify=y
)
# TODO: выведите размеры train и test
print("Train:", X_train.shape)
print("Test:", X_test.shape)

X_train_numeric = X_train.select_dtypes(include=['number'])
X_test_numeric = X_test.select_dtypes(include=['number'])
# TODO: создайте scaler
scaler = StandardScaler()
# TODO: создайте X_train_scaled
X_train_scaled = scaler.fit_transform(X_train_numeric)
# TODO: создайте X_test_scaled
X_test_scaled = scaler.transform(X_test_numeric)
# TODO: создайте model
model = LogisticRegression(max_iter=7000)
# TODO: обучите model
model.fit(X_train_scaled, y_train)
print("Модель обучена")

# TODO: создайте y_pred
# Прогноз нужно делать на тестовых данных, потому что сравниваем с y_test
y_pred = model.predict(X_test_numeric)

# TODO: создайте y_proba
# predict_proba возвращает таблицу вероятностей:
# столбец 0 — вероятность класса 0
# столбец 1 — вероятность класса 1
y_pred = model.predict(X_test_numeric)

y_proba = model.predict_proba(X_test_numeric)

comparison = pd.DataFrame({
    "fact": y_test.values,
    "prediction": y_pred,
    "probability_class_1": y_proba[:, 1]
})

display(comparison.head(10))

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Обучаем модель
model.fit(X_train_scaled, y_train)

# Делаем прогноз на тестовых данных
y_pred = model.predict(X_test_scaled)

# Смотрим, какие классы есть в факте и прогнозе
print("Классы в y_test:", sorted(set(y_test)))
print("Классы в y_pred:", sorted(set(y_pred)))

# Accuracy работает и для бинарной, и для многоклассовой классификации
accuracy = accuracy_score(y_test, y_pred)

# Для многоклассовой классификации нужно указать average
precision = precision_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

metrics_report = {
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1": f1
}

for key, value in metrics_report.items():
    print(key, ":", round(value, 4))

# TODO: создайте cm = confusion_matrix(...)
from sklearn.metrics import classification_report
cm = confusion_matrix(y_test, y_pred)

# TODO: выведите cm
print("Confusion Matrix:")
print(cm)
# TODO: получите tn, fp, fn, tp
n_classes = cm.shape[0]

for i in range(n_classes):
    tp = cm[i, i]
    fn = cm[i, :].sum() - tp
    fp = cm[:, i].sum() - tp
    tn = cm.sum() - tp - fn - fp

print("TN:", tn)
print("FP:", fp)
print("FN:", fn)
print("TP:", tp)

# TODO: создайте disp
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay
class_names = sorted(data['category'].unique())
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=class_names
)# TODO: вызовите disp.plot()
disp.plot()
# TODO: добавьте title и show()
plt.title("Матрица ошибок")
plt.show()
# TODO: выведите classification_report
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))

# TODO: создайте final_report
final_report = {
    "rows": len(X),
    "features": X.shape[1],
    "accuracy": round(accuracy, 4),
    "precision": round(precision, 4),
    "recall": round(recall, 4),
    "f1": round(f1, 4),
    "tn": int(tn),
    "fp": int(fp),
    "fn": int(fn),
    "tp": int(tp)
}
# TODO: выведите final_report
print("Итоговый отчёт:")
for key, value in final_report.items():
    print(key, ":", value)
# TODO: создайте conclusions из 5 выводов
conclusions = [
    "Accuracy показывает общую долю правильных ответов.",
    "Precision показывает точность положительных предсказаний.",
    "Recall показывает, сколько положительных объектов модель нашла.",
    "F1-score помогает оценить баланс Precision и Recall.",
    "Confusion Matrix помогает увидеть конкретные типы ошибок модели."
]
# TODO: выведите conclusions
print()
print("Выводы:")
for item in conclusions:
  print("-", item)
# TODO: выведите GitHub-команды
print()
print("Github:")
print("git add .")
print('git commit -m "feat: complete classification metrics lesson"')
print("git push -u origin feature/block7-lesson06-classification-metrics")

# TODO: выполните самостоятельно задание ячейки 1
from sklearn.datasets import load_breast_cancer
import pandas as pd

data=load_breast_cancer()

X=pd.DataFrame(data.data, columns=data.feature_names)
y=pd.Series(data.target)

print(X.shape)

# TODO: выполните самостоятельно задание ячейки 2
display(X.head())
print(data.target_names)

# TODO: выполните самостоятельно задание ячейки 3
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=55,stratify=y
)

# TODO: выполните самостоятельно задание ячейки 4
from sklearn.tree import DecisionTreeClassifier

tree=DecisionTreeClassifier(random_state=55)

tree.fit(X_train,y_train)

# TODO: выполните самостоятельно задание ячейки 5
pred=tree.predict(X_test)

print(pred[:10])

# TODO: выполните самостоятельно задание ячейки 6
from sklearn.metrics import accuracy_score

accuracy=accuracy_score(y_test,pred)

print("Accuracy:",accuracy)

# TODO: выполните самостоятельно задание ячейки 7
depth=tree.get_depth()
leaves=tree.get_n_leaves()

print("Depth:",depth)
print("Leaves:",leaves)

# TODO: выполните самостоятельно задание ячейки 8
importance=pd.DataFrame({
    "feature":X.columns,
    "importance":tree.feature_importances_
})

importance=importance.sort_values(
    by="importance",
    ascending=False
)

display(importance.head(10))

# TODO: выполните самостоятельно задание ячейки 9
small_tree=DecisionTreeClassifier(
    max_depth=3,
    random_state=55
)

small_tree.fit(X_train,y_train)

small_pred=small_tree.predict(X_test)

small_accuracy=accuracy_score(y_test,small_pred)

print("Полное дерево:",accuracy)
print("Ограниченное дерево:",small_accuracy)

# TODO: выполните самостоятельно задание ячейки 10
report={
    "rows":len(X),
    "features":X.shape[1],
    "accuracy":round(accuracy,3),
    "depth":depth,
    "best_feature":importance.iloc[0]["feature"]
}

print(report)

# TODO: выполните самостоятельно задание ячейки 1
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

print("Библиотеки подключены")

# TODO: выполните самостоятельно задание ячейки 2
from pathlib import Path
from google.colab import drive

drive.mount('/content/drive')

file_path = Path("/content/drive/MyDrive/Базы/sales_data.xlsx")
data = pd.read_excel(file_path, sheet_name="sales_data", header=0)
X = data
y = data['category']

print("Размер X:", X.shape)
print("Размер y:", y.shape)
print("Классы:", y.unique())

display(X.head())

# TODO: выполните самостоятельно задание ячейки 3
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=55,
    stratify=y
)

print("Train:", X_train.shape)
print("Test:", X_test.shape)

# TODO: выполните самостоятельно задание ячейки 4
useless_columns = ['manager', 'city', 'category', 'product']

X_train_numeric = X_train.drop(columns=useless_columns)
X_test_numeric = X_test.drop(columns=useless_columns)

tree_model = DecisionTreeClassifier(
    max_depth=3,
    random_state=55
)

tree_model.fit(X_train_numeric, y_train)

tree_pred = tree_model.predict(X_test_numeric)

tree_accuracy = accuracy_score(y_test, tree_pred)

print("Decision Tree Accuracy:", tree_accuracy)

# TODO: выполните самостоятельно задание ячейки 5
useless_columns = ['manager', 'city', 'category', 'product']

X_train_numeric = X_train.drop(columns=useless_columns)
X_test_numeric = X_test.drop(columns=useless_columns)

forest_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=55
)

forest_model.fit(X_train_numeric, y_train)

forest_pred = forest_model.predict(X_test_numeric)

forest_accuracy = accuracy_score(y_test, forest_pred)

print("Random Forest Accuracy:", forest_accuracy)

# TODO: выполните самостоятельно задание ячейки 6
def calculate_metrics(y_true, y_pred):
  return {
      'accuracy': accuracy_score(y_true, y_pred),
      'precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
      'recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
      'f1': f1_score(y_true, y_pred, average='weighted', zero_division=0)
  }

tree_metrics = calculate_metrics(y_test, tree_pred)
forest_metrics = calculate_metrics(y_test, forest_pred)

metrics_df = pd.DataFrame([
    {"model": "Decision Tree", **tree_metrics},
    {"model": "Random Forest", **forest_metrics}
])

display(metrics_df)

# TODO: выполните самостоятельно задание ячейки 7
feature_importance = pd.DataFrame({
    "feature": [f'feature_{i}' for i in range(len(forest_model.feature_importances_))],
    "importance": forest_model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="importance",
    ascending=False
)

display(feature_importance.head(10))

# TODO: выполните самостоятельно задание ячейки 8
top_features = feature_importance.head(10).sort_values("importance")

plt.figure(figsize=(10, 8))
plt.barh(top_features["feature"], top_features["importance"])
plt.title("TOP-10 важных признаков Random Forest")
plt.xlabel("Важность")
plt.ylabel("Признак")
plt.grid(True)
plt.show()

# TODO: выполните самостоятельно задание ячейки 9
estimators_list = [10, 15, 25, 55, 125, 160]
scores = []

for n in estimators_list:
    model = RandomForestClassifier(
        n_estimators=n,
        max_depth=5,
        random_state=55
    )
    model.fit(X_train_numeric, y_train)
    pred = model.predict(X_test_numeric)
    score = accuracy_score(y_test, pred)
    scores.append(score)
results_df = pd.DataFrame({
    "n_estimators": estimators_list,
    "accuracy": scores
})

display(results_df)

plt.figure(figsize=(10, 8))
plt.plot(results_df["n_estimators"], results_df["accuracy"], marker="o")
plt.title("Accuracy при разном количестве деревьев")
plt.xlabel("Количество деревьев")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()

# TODO: выполните самостоятельно задание ячейки 10
best_model_name = "Random Forest" if forest_accuracy >= tree_accuracy else "Desicion Tree"

final_report = {
    "rows": len(X),
    "features": X.shape[1],
    "best_model": best_model_name,
    "tree_accuracy": round(tree_accuracy, 4),
    "forest_accuracy": round(forest_accuracy, 4),
    "forest_f1": round(forest_metrics["f1"], 4),
    "top_feature": feature_importance.iloc[0]["feature"]
}

print("Итоговый отчёт:")
for key, value in final_report.items():
    print(key, ":", value)

conclusions = [
    "Random Forest объединяет несколько деревьев решений.",
    "Ансамбль часто работает устойчивее, чем одно дерево.",
    "Количество деревьев влияет на качество модели.",
    "Важность признаков помогает объяснять решения модели.",
    "Random Forest хорошо подходит для табличных данных и дипломных ML-проектов."
]

print()
print("Выводы:")
for item in conclusions:
    print("-", item)

import pandas as pd
import numpy as np

np.random.seed(55)

df = pd.DataFrame({
    "income": np.random.randint(25000,125000,350),
    "spending": np.random.randint(1500, 55000,350)
})

display(df.head())

# TODO: выполните самостоятельно задание ячейки 2
import matplotlib.pyplot as plt
plt.figure(figsize=(8,10))
plt.scatter(df["income"],df["spending"],alpha=0.6)
plt.xlabel("Доход")
plt.ylabel("Расходы")
plt.title("Клиенты магазина")
plt.grid(True)
plt.show()

# TODO: выполните самостоятельно задание ячейки 3
X = df[["income", "spending"]]

print(X.shape)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# TODO: выполните самостоятельно задание ячейки 5
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=5,
    random_state=55,
    n_init=15
)

kmeans.fit(X_scaled)

# TODO: выполните самостоятельно задание ячейки 6
clusters = kmeans.labels_

df["cluster"] = clusters

print(df["cluster"].value_counts())

# TODO: выполните самостоятельно задание ячейки 7
plt.figure(figsize=(8,10))
plt.scatter(
    df["income"],
    df["spending"],
    c=df["cluster"]
)

plt.xlabel("Доход")
plt.ylabel("Расходы")
plt.title("Кластеры клиентов")
plt.show()

# TODO: выполните самостоятельно задание ячейки 8
inertia=[]

for k in range(1,15):
  model=KMeans(
      n_clusters=k,
      random_state=55,
      n_init=15
  )
  model.fit(X_scaled)
  inertia.append(model.inertia_)

  # TODO: выполните самостоятельно задание ячейки 9
plt.figure(figsize=(10,8))
plt.plot(range(1,15),inertia,marker="o")
plt.xlabel("Количество кластеров")
plt.ylabel("Inertia")
plt.title("Метод локтя")
plt.grid(True)
plt.show()

# TODO: выполните самостоятельно задание ячейки 10
report = {
    "rows": len(df),
    "clusters": len(df["cluster"].unique()),
    "avg_income": round(df["income"].mean(),2),
    "avg_spending": round(df["spending"].mean(),2)
}

print(report)

# TODO: импортируйте pandas как pd
import pandas as pd
# TODO: импортируйте numpy как np
import numpy as np
# TODO: импортируйте matplotlib.pyplot как plt
import matplotlib.pyplot as plt
# TODO: импортируйте make_blobs
from sklearn.datasets import make_blobs
# TODO: импортируйте StandardScaler
from sklearn.preprocessing import StandardScaler
# TODO: импортируйте KMeans
from sklearn.cluster import KMeans
print("Библиотеки подключены")

# TODO: создайте X_raw, true_labels через make_blobs
from pathlib import Path
from google.colab import drive

drive.mount('/content/drive')

file_path = Path("/content/drive/MyDrive/Базы/sales_data.xlsx")
data = pd.read_excel(file_path, sheet_name="sales_data", header=0)
# TODO: создайте df с колонками annual_income_raw и spending_score_raw
X_raw = data
df = pd.DataFrame(X_raw, columns=["quantity", "price"])
# TODO: покажите df.head()
display(df.head())
print("Размер таблицы:", df.shape)

# TODO: создайте функцию scale_to_range(values, new_min, new_max)
def scale_to_range(values, new_min, new_max):
    old_min = values.min()
    old_max = values.max()
    scaled = (values - old_min) / (old_max - old_min)
    return scaled * (new_max - new_min) + new_min
# TODO: создайте annual_income
df["quantity1"] = scale_to_range(df["quantity"], 20, 120).round(1)
# TODO: создайте spending_score
df["price1"] = scale_to_range(df["price"], 1, 100).round(1)
# TODO: оставьте в df только annual_income и spending_score
df = df[["quantity1", "price1"]]
display(df.head())

# TODO: создайте column_description
column_description = {
    "quantity": "Кол-во товара",
    "price": "Цена товара"
}
# TODO: выведите описание колонок
for column, description in column_description.items():
    print(column, "-", description)
# TODO: покажите df.describe()
print()
print("Статистика:")
display(df.describe())
# TODO: выведите df.isna().sum()
print("Пропуски:")
print(df.isna().sum())

# TODO: создайте figure
plt.figure(figsize=(10,5))
# TODO: постройте scatter annual_income и spending_score
plt.scatter(
    df["quantity1"],
    df["price1"],
    alpha=0.75
)
# TODO: добавьте title, xlabel, ylabel, grid
plt.title("Клиенты: Кол-во и цена товара")
plt.xlabel("Кол-во")
plt.ylabel("Цена")
plt.grid(True)

# TODO: show()
plt.show()

# TODO: создайте features
features = ["quantity1", "price1"]
# TODO: создайте X
X = df[features]
# TODO: создайте scaler
scaler = StandardScaler()
# TODO: создайте X_scaled
X_scaled = scaler.fit_transform(X)
print("Размер X:", X.shape)
print("Размер X_scaled:", X_scaled.shape)

# TODO: создайте inertia
inertia = []
# TODO: создайте k_values
k_values = range(1, 10)
# TODO: в цикле обучите KMeans для разных K
for k in k_values:
    model = KMeans(
        n_clusters=k,
        random_state=55,
        n_init=10
    )
    model.fit(X_scaled)
    inertia.append(model.inertia_)
# TODO: постройте график метода локтя
plt.figure(figsize=(10, 8))
plt.plot(list(k_values), inertia, marker="o")
plt.title("Метод локтя")
plt.xlabel("Количество кластеров K")
plt.ylabel("Inertia")
plt.grid(True)
plt.show()

# TODO: создайте kmeans
kmeans = KMeans(
    n_clusters=5,
    random_state=55,
    n_init=10
)
# TODO: обучите kmeans
kmeans.fit(X_scaled)
# TODO: добавьте df["cluster"]
df["cluster"] = kmeans.labels_
# TODO: выведите value_counts()
print("Количество клиентов в каждом кластере")
print(df["cluster"].value_counts().sort_index())

# TODO: создайте figure
plt.figure(figsize=(10, 8))
# TODO: постройте scatter с c=df["cluster"]
plt.scatter(
    df["quantity1"],
    df["price1"],
    c=df["cluster"],
    alpha=0.8
)
# TODO: добавьте title, xlabel, ylabel, grid
plt.title("Сегменты клиентов по K-Means")
plt.xlabel("Кол-во")
plt.ylabel("Цена")
plt.grid(True)
# TODO: show()
plt.show()

# TODO: создайте cluster_report
cluster_report = (
    df.groupby("cluster")
    .agg(
        quantity_count=("quantity1", "count"),
        avg_income=("quantity1", "mean"),
        avg_price=("price1", "mean")
    )
    .sort_values(by="avg_price", ascending=False)
)
# TODO: покажите cluster_report
display(cluster_report)
# TODO: найдите best_cluster
best_cluster = cluster_report["avg_price"].idxmax()

# TODO: найдите low_cluster
low_cluster = cluster_report["avg_price"].idxmin()
# TODO: создайте final_report
final_report = {
    "rows": len(df),
    "clusters": df["cluster"].nunique(),
    "best_cluster": int(best_cluster),
    "low_spending_cluster": int(low_cluster)
}
print("Итоговый отчёт:")
for key, value in final_report.items():
  print(key, ":", value)
# TODO: создайте conclusions
conclusions = [
   "K-Means нашёл группы клиентов без заранее заданных ответов.",
   "Масштабирование признаков важно для алгоритмов, основанных на расстояниях.",
   "Метод локтя помогает выбирать количество кластеров.",
   "Кластеры нужно интерпретировать как бизнес-сегменты.",
   "Ноутбук стабилен, потому что не зависит от внешнего CSV-файла."
]
print()
print("Выводы:")
for item in conclusions:
    print("-", item)
