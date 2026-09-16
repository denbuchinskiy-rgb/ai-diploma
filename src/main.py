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