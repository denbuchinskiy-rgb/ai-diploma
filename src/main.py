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
