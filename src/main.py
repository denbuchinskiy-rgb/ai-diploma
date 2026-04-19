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