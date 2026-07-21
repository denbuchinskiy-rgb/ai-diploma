sample = [8, 6, 13, 8, 13, 6, 8, 6, 13, 8]

print("sample:", sample)
print("n =", len(sample))

print("min =", min(sample))
print("max =", max(sample))
print("sorted =", sorted(sample))

def mean(values: list[float]) -> float:
    """Среднее арифметическое. Требует непустой список."""
    # TODO: проверьте пустой список и верните sum(values)/len(values)
    if len(values) == 0:
      raise ValueError("mean: empty list")
    return sum(values) / len(values)

print("mean =", mean(sample))

def median(values: list[float]) -> float:
    """Медиана. Требует непустой список."""
    # TODO: реализуйте медиану через сортировку и проверку чётности n
    if len(values) == 0:
      raise ValueError("median: empty list")
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
       return float(s[mid])
    else:
       return (s[mid - 1] + s[mid]) / 2

print("median =", median(sample))

def variance_sample(values: list[float]) -> float:
    """Выборочная дисперсия (деление на n-1)."""
    # TODO: проверьте n>=2, найдите m=mean(values), верните sum((x-m)**2)/(n-1)
    n = len(values)
    if n < 2:
       raise ValueError("variance_sample: need at least 2 values")
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / (n - 1)

print("variance_sample =", variance_sample(sample))

def std_sample(values: list[float]) -> float:
    """Выборочное стандартное отклонение."""
    # TODO: верните (variance_sample(values))**0.5
    return variance_sample(values) ** 0.5

print("std_sample =", std_sample(sample))

def with_outlier(values: list[float], outlier: float) -> list[float]:
    """Вернуть новую выборку, добавив выброс (не меняем исходный список)."""
    # TODO: верните новый список list(values) + [outlier]
    return list(values) + [outlier]

sample_out = with_outlier(sample, 150)

print("mean(before) =", round(mean(sample), 3), "median(before) =", median(sample))
print("mean(after)  =", round(mean(sample_out), 3), "median(after)  =", median(sample_out))

def trimmed_mean(values: list[float], k: int = 1) -> float:
    """Усечённое среднее: убрать k минимальных и k максимальных."""
    # TODO: проверьте n>0 и 2*k<n, затем core=sorted(values)[k:n-k], return mean(core)
    n = len(values)
    if n == 0:
      raise ValueError("trimmed_mean: empty list")
    if 2 * k >= n:
      raise ValueError("trimmed_mean: k too large")
    s = sorted(values)
    core = s[k:n - k]
    return mean(core)

print("trimmed_mean(before) =", round(trimmed_mean(sample, k=1), 3))
print("trimmed_mean(after)  =", round(trimmed_mean(sample_out, k=1), 3))

def describe(values: list[float]) -> dict:
    """Короткое описание выборки (как мини-отчёт)."""
    # TODO: верните dict с ключами n/min/max/mean/median/std (std только если len>=2)
    return {
        "n": len(values),
        "min": min(values) if values else None,
        "max": max(values) if values else None,
        "mean": mean(values) if values else None,
        "median": median(values) if values else None,
        "std": std_sample(values) if len(values) >= 2 else None
    }

print("describe(sample) =", describe(sample))
print("describe(sample_out) =", describe(sample_out))

import numpy as np
# TODO: сгенерируйте 1000 значений нормального распределения
data = np.random.normal(loc=3, scale=10, size=1000)
len(data)

# TODO: вычислите mean и std
mean = np.mean(data)
std = np.std(data)
mean, std

import matplotlib.pyplot as plt
# TODO: постройте гистограмму data
plt.hist(data, bins=30)
plt.title("Normal Distribution")
plt.show()

# TODO: добавьте выброс 10
data_out = np.append(data, 10)
len(data_out)

# TODO: постройте гистограмму data_out
plt.hist(data_out, bins=30)
plt.title("With Outlier")
plt.show()

# TODO: вычислите медиану
median = np.median(data_out)
median

# TODO: сгенерируйте uniform и постройте гистограмму
uniform = np.random.uniform(-5, 5, 1000)
plt.hist(uniform, bins=30)
plt.title("Uniform Distribution")
plt.show()

# TODO: сравните средние
np.mean(data), np.mean(uniform)

# Создаём список records.
# records — это список наблюдений.
# Одно наблюдение = один пользователь.
records = [
    # Пользователь 1: кликнул и купил.
    {"click": 1, "buy": 1},

    # Пользователь 2: кликнул, но не купил.
    {"click": 1, "buy": 0},

    # Пользователь 3: кликнул и купил.
    {"click": 1, "buy": 1},

    # Пользователь 4: не кликнул и не купил.
    {"click": 0, "buy": 0},

    # Пользователь 5: кликнул, но не купил.
    {"click": 1, "buy": 0},

    # Пользователь 6: не кликнул и не купил.
    {"click": 0, "buy": 0},

    # Пользователь 7: кликнул и купил.
    {"click": 1, "buy": 1},

    # Пользователь 8: не кликнул и не купил.
    {"click": 0, "buy": 0},

    # Пользователь 9: кликнул, но не купил.
    {"click": 1, "buy": 0},

    # Пользователь 10: кликнул и купил.
    {"click": 1, "buy": 1},

    # Пользователь 11: не кликнул и не купил.
    {"click": 0, "buy": 0},

    # Пользователь 12: кликнул, но не купил.
    {"click": 1, "buy": 0},

    {"click": 0, "buy": 0},

    {"click": 1, "buy": 1},
]

# TODO: посчитайте количество записей в списке.
# Подсказка: используйте len(records).
n = len(records)

# Печатаем количество пользователей.
print("n =", n)

# Печатаем первую запись, чтобы увидеть структуру данных.
print("first record:", records[0])

# Проверяем, что в данных 12 пользователей.
assert n == 14

# Проверяем, что первая запись — это словарь.
assert isinstance(records[0], dict)

# Создаём счётчик кликов.
count_click = 0

# Создаём счётчик покупок.
count_buy = 0

# Создаём счётчик случаев, где пользователь и кликнул, и купил.
count_click_and_buy = 0

# Запускаем цикл по всем пользователям.
for r in records:

    # TODO: если пользователь кликнул, увеличьте счётчик кликов.
    if r["click"] == 1:
        count_click += 1

    # TODO: если пользователь купил, увеличьте счётчик покупок.
    if r["buy"] == 1:
        count_buy += 1

    # TODO: если пользователь кликнул и купил одновременно,
    # увеличьте счётчик пересечения событий.
    if r["click"] == 1 and r["buy"] == 1:
        count_click_and_buy += 1

# Печатаем количество кликов.
print("count_click =", count_click)

# Печатаем количество покупок.
print("count_bought =", count_buy)

# Печатаем количество случаев клик + покупка.
print("count_clicked_and_bought =", count_click_and_buy)

# Определяем функцию вероятности события.
def prob_event(count_A: int, n: int) -> float:

    # Если n <= 0, вероятность считать нельзя.
    if n <= 0:
        raise ValueError("prob_event: n must be > 0")

    # Количество события не может быть отрицательным
    # и не может быть больше общего количества наблюдений.
    if count_A < 0 or count_A > n:
        raise ValueError("prob_event: invalid count")

    # TODO: верните вероятность как частоту.
    # Подсказка: count_A / n.
    return count_A / n


# Считаем общее количество записей.
n = len(records)

# TODO: посчитайте вероятность клика.
p_clicked = prob_event(count_click, n)

# TODO: посчитайте вероятность покупки.
p_bought = prob_event(count_buy, n)

# Печатаем результаты.
print("P(clicked) =", p_clicked)
print("P(bought)  =", p_bought)


# Определяем функцию условной вероятности.
def prob_conditional(count_A_and_B: int, count_B: int) -> float:

    # Если событие B ни разу не произошло, условную вероятность считать нельзя.
    if count_B <= 0:
        raise ValueError("prob_conditional: count_B must be > 0")

    # Пересечение событий не может быть отрицательным
    # и не может быть больше количества B.
    if count_A_and_B < 0 or count_A_and_B > count_B:
        raise ValueError("prob_conditional: invalid intersection count")

    # TODO: верните условную вероятность.
    # Подсказка: count_A_and_B / count_B.
    return count_A_and_B / count_B


# TODO: посчитайте вероятность покупки при условии клика.
p_buy_given_click = prob_conditional(
    count_click_and_buy,
    count_click
    )

# Печатаем результат.
print("P(buy | click) =", p_buy_given_click)

# Определяем функцию проверки независимости.
def is_independent_by_counts(p_a: float, p_a_given_b: float, tol: float = 0.05) -> bool:

    # TODO: посчитайте абсолютную разницу между P(A|B) и P(A).
    # Подсказка: abs(p_a_given_b - p_a).
    difference = abs(p_a_given_b - p_a)

    # TODO: верните True, если difference <= tol.
    return difference <= tol


# P(A) = P(bought).
p_a = p_bought

# P(A|B) = P(bought|clicked).
p_a_given_b = p_buy_given_click

# Проверяем независимость с порогом 0.05.
independent = is_independent_by_counts(p_a, p_a_given_b, tol=0.05)

# Печатаем результаты.
print("P(buy) =", round(p_a, 3))
print("P(buy | click) =", round(p_a_given_b, 3))
print("independent? ->", independent)

def contingency_2x2(recs: list[dict], a_key: str, b_key: str) -> list[list[int]]:

    # Создаём таблицу 2 на 2, заполненную нулями.
    table = [[0, 0], [0, 0]]

    # Проходим по всем записям.
    for r in recs:

        # Берём значение первого признака: 0 или 1.
        a = int(r[a_key])

        # Берём значение второго признака: 0 или 1.
        b = int(r[b_key])

        # Проверяем, что оба значения бинарные.
        if a not in (0, 1) or b not in (0, 1):
            raise ValueError("contingency_2x2: values must be 0/1")

        # TODO: увеличьте нужную ячейку таблицы.
        # Подсказка: table[a][b] += 1.
        table [a][b] += 1

    # Возвращаем таблицу.
    return table


# TODO: постройте таблицу для clicked и bought.
table = contingency_2x2(records, "click", "buy")

# Печатаем таблицу.
print("table 2x2 =", table)

import matplotlib.pyplot as plt

# TODO: посчитайте количество пользователей, у которых clicked = 0.
# Это сумма элементов в первой строке таблицы (clicked=0).
clicked0_total = table[0][0] + table[0][1]

# TODO: посчитайте количество пользователей, у которых clicked = 1.
# Это сумма элементов во второй строке таблицы (clicked=1).
clicked1_total = table[1][0] + table[1][1]

# TODO: посчитайте вероятность покупки при clicked = 0.
# Это отношение числа пользователей, которые купили (table[0][1]),
# к общему числу пользователей, которые не кликнули (clicked0_total).
p_buy_given_click0 = table[0][1] / clicked0_total if clicked0_total else 0.0

# TODO: посчитайте вероятность покупки при clicked = 1.
# Это отношение числа пользователей, которые купили (table[1][1]),
# к общему числу пользователей, которые кликнули (clicked1_total).
p_buy_given_click1 = table[1][1] / clicked1_total if clicked1_total else 0.0

# Подготавливаем подписи столбцов.
labels = ["P(buy|click=0)", "P(buy|click=1)"]

# TODO: подготовьте значения столбцов.
values = [p_buy_given_click0, p_buy_given_click1]

# Создаём график.
plt.figure(figsize=(10, 8))

# TODO: постройте столбчатую диаграмму.
plt.bar(labels, values)

# Вероятность находится от 0 до 1.
plt.ylim(0, 1)

# Добавляем заголовок.
plt.title("Условные вероятности из данных")

# Подписываем ось Y.
plt.ylabel("Вероятность")

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение элементов.
plt.tight_layout()

# Показываем график.
plt.show()

# Печатаем значения.
print("P(buy|click=0) =", round(p_buy_given_click0, 3))
print("P(buy|click=1) =", round(p_buy_given_click1, 3))

# Импортируем numpy для массивов и случайных чисел.
import numpy as np

# Определяем функцию симуляции кликов и покупок.
def simulate_click_buy(n: int, p_click: float, p_buy_click0: float, p_buy_click1: float, seed: int = 42):

    # TODO: создайте генератор случайных чисел.
    # Подсказка: np.random.default_rng(seed)
    rng = np.random.default_rng(seed)

    # TODO: для каждого пользователя случайно решите, кликнул он или нет.
    # Подсказка: rng.random(n) < p_click
    clicked = rng.random(n) < p_click

    # TODO: если пользователь кликнул, возьмите p_buy_click1,
    # иначе возьмите p_buy_click0.
    # Подсказка: np.where(clicked, p_buy_click1, p_buy_click0)
    probs = np.where(clicked, p_buy_click1, p_buy_click0)

    # TODO: для каждого пользователя случайно решите, купил он или нет.
    # Подсказка: rng.random(n) < probs
    bought = rng.random(n) < probs

    # Возвращаем два массива: клики и покупки.
    return clicked, bought


# Запускаем симуляцию на 100000 пользователей.
clicked_sim, bought_sim = simulate_click_buy(
    n=100_000,
    p_click=0.6,
    p_buy_click0=0.05,
    p_buy_click1=0.25,
    seed=1,
)

# TODO: посчитайте, сколько пользователей кликнули.
count_click1 = int(clicked_sim.sum())

# TODO: посчитайте, сколько пользователей кликнули и купили.
count_buy_and_click1 = int((bought_sim & clicked_sim).sum())

# TODO: оцените P(buy|click=1) по симуляции.
p_est = count_buy_and_click1 / count_click1

# Печатаем оценку.
print("simulated P(buy|click=1) ≈", round(p_est, 3))

# Импортируем matplotlib для графиков.
import matplotlib.pyplot as plt

# Импортируем numpy для среднего значения.
import numpy as np

# Определяем функцию оценки P(buy|click=1).
def estimate_p_buy_given_click1(n: int, seed: int) -> float:

    # TODO: запустите симуляцию.
    clicked_sim, bought_sim = simulate_click_buy(
        n=n,
        p_click=0.6,
        p_buy_click0=0.05,
        p_buy_click1=0.25,
        seed=seed,
    )

    # TODO: посчитайте, сколько пользователей кликнули.
    count_click1 = int(clicked_sim.sum())

    # TODO: посчитайте, сколько пользователей кликнули и купили.
    count_buy_and_click1 = int((bought_sim & clicked_sim).sum())

    # TODO: верните оценку условной вероятности.
    return count_buy_and_click1 / count_click1


# TODO: сделайте 30 запусков симуляции с разными seed.
# Подсказка: используйте list comprehension и range(30).
estimates = [
    estimate_p_buy_given_click1(n=20_000, seed=s)
    for s in range(30)
]

# Создаём график.
plt.figure(figsize=(10, 8))

# TODO: постройте гистограмму оценок.
plt.hist(estimates, bins=10)

# Добавляем заголовок.
plt.title("Оценки P(buy|click=1) в 30 симуляциях")

# Подписываем ось X.
plt.xlabel("Оценка вероятности")

# Подписываем ось Y.
plt.ylabel("Количество запусков")

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение.
plt.tight_layout()

# Показываем график.
plt.show()

# TODO: посчитайте среднюю оценку.
mean_estimate = float(np.mean(estimates))

# Печатаем среднюю оценку.
print("mean estimate =", round(mean_estimate, 3))

# Создаём список records.
# records — это список наблюдений.
# Одно наблюдение = один пользователь.
records = [
    # Пользователь 1: кликнул и купил.
    {"click": 1, "buy": 1},

    # Пользователь 2: кликнул, но не купил.
    {"click": 1, "buy": 0},

    # Пользователь 3: кликнул и купил.
    {"click": 1, "buy": 1},

    # Пользователь 4: не кликнул и не купил.
    {"click": 0, "buy": 0},

    # Пользователь 5: кликнул, но не купил.
    {"click": 1, "buy": 0},

    # Пользователь 6: не кликнул и не купил.
    {"click": 0, "buy": 0},

    # Пользователь 7: кликнул и купил.
    {"click": 1, "buy": 1},

    # Пользователь 8: не кликнул и не купил.
    {"click": 0, "buy": 0},

    # Пользователь 9: кликнул, но не купил.
    {"click": 1, "buy": 0},

    # Пользователь 10: кликнул и купил.
    {"click": 1, "buy": 1},

    # Пользователь 11: не кликнул и не купил.
    {"click": 0, "buy": 0},

    # Пользователь 12: кликнул, но не купил.
    {"click": 1, "buy": 0},

    {"click": 0, "buy": 0},

    {"click": 1, "buy": 1},
]

# TODO: посчитайте количество пользователей.
# Подсказка: используйте len(records).
n = len(records)

# Печатаем количество пользователей.
print("Количество пользователей n =", n)

# Определяем функцию build_binary_counts.
# Функция принимает:
# recs  — список записей,
# a_key — название поля для события A,
# b_key — название поля для события B.
def build_binary_counts(recs, a_key, b_key):

    # TODO: посчитайте общее количество записей.
    # Подсказка: используйте len(recs).
    n = len(recs)

    # count_A будет хранить количество случаев, где A = 1.
    count_A = 0

    # count_B будет хранить количество случаев, где B = 1.
    count_B = 0

    # count_A_and_B будет хранить количество случаев, где A = 1 и B = 1 одновременно.
    count_A_and_B = 0

    # Запускаем цикл по всем записям.
    for r in recs:

        # Берём значение события A из текущей записи.
        a = int(r[a_key])

        # Берём значение события B из текущей записи.
        b = int(r[b_key])

        # Проверяем, что A имеет только значения 0 или 1.
        if a not in (0, 1):
            raise ValueError("A должно быть 0 или 1")

        # Проверяем, что B имеет только значения 0 или 1.
        if b not in (0, 1):
            raise ValueError("B должно быть 0 или 1")

        # TODO: если A произошло, увеличьте счётчик A.
        if a == 1:
            count_A += 1

        # TODO: если B произошло, увеличьте счётчик B.
        if b == 1:
            count_B += 1

        # TODO: если A и B произошли одновременно, увеличьте общий счётчик.
        if a == 1 and b == 1:
            count_A_and_B += 1

    # Возвращаем все результаты в одном словаре.
    return {
        "n": n,
        "count_A": count_A,
        "count_B": count_B,
        "count_A_and_B": count_A_and_B,
    }


# В нашем примере:
# A = bought, то есть покупка.
# B = clicked, то есть клик.
counts = build_binary_counts(records, "buy", "click")

# Выводим словарь со счётчиками.
print(counts)

# Определяем функцию для расчёта вероятности по счётчикам.
def prob_from_counts(count, n):

    # Проверяем, что общее количество наблюдений больше нуля.
    if n <= 0:
        raise ValueError("n должно быть больше 0")

    # Проверяем, что количество события не меньше 0.
    if count < 0:
        raise ValueError("count не может быть отрицательным")

    # Проверяем, что количество события не больше общего количества наблюдений.
    if count > n:
        raise ValueError("count не может быть больше n")

    # TODO: верните вероятность как частоту.
    # Подсказка: вероятность = count / n.
    return count / n


# TODO: посчитайте prior: вероятность покупки вообще.
# Это P(A) = P(bought).
prior = prob_from_counts(counts["count_A"], counts["n"])

# TODO: посчитайте evidence: вероятность клика вообще.
# Это P(B) = P(clicked).
evidence = prob_from_counts(counts["count_B"], counts["n"])

# Печатаем результаты.
print("P(buy)  =", prior)
print("P(click) =", evidence)

# Определяем функцию условной вероятности.
def prob_conditional(count_A_and_B, count_A):

    # Проверяем, что событие A хотя бы раз встретилось.
    if count_A <= 0:
        raise ValueError("count_A должно быть больше 0")

    # Проверяем, что пересечение событий не отрицательное.
    if count_A_and_B < 0:
        raise ValueError("count_A_and_B не может быть отрицательным")

    # Проверяем, что пересечение не больше количества A.
    if count_A_and_B > count_A:
        raise ValueError("count_A_and_B не может быть больше count_A")

    # TODO: верните условную вероятность.
    # Подсказка: count_A_and_B / count_A.
    return count_A_and_B / count_A


# TODO: посчитайте likelihood:
# P(B|A) = P(clicked|bought).
likelihood = prob_conditional(
    counts["count_A_and_B"],
    counts['count_A']
)

# Печатаем результат.
print("P(click | buy) =", likelihood)

# Определяем функцию формулы Байеса.
def bayes_posterior(prior, likelihood, evidence):

    # Проверяем prior.
    if prior < 0 or prior > 1:
        raise ValueError("prior должен быть от 0 до 1")

    # Проверяем likelihood.
    if likelihood < 0 or likelihood > 1:
        raise ValueError("likelihood должен быть от 0 до 1")

    # Проверяем evidence.
    if evidence < 0 or evidence > 1:
        raise ValueError("evidence должен быть от 0 до 1")

    # Делить на ноль нельзя.
    if evidence == 0:
        raise ValueError("evidence не должен быть равен 0")

    # TODO: примените формулу Байеса.
    # Подсказка: posterior = likelihood * prior / evidence.
    posterior = likelihood * prior / evidence

    # Возвращаем итоговую вероятность.
    return posterior


# TODO: посчитайте P(bought|clicked) по формуле Байеса.
posterior = bayes_posterior(prior, likelihood, evidence)

# Печатаем результат.
print("P(buy | click) via Bayes =", posterior)

# TODO: посчитайте P(bought|clicked) напрямую из данных.
# Подсказка: count_A_and_B / count_B.
direct = counts["count_A_and_B"] / counts["count_B"]

# Печатаем прямой расчёт.
print("direct =", direct)

# Печатаем расчёт через формулу Байеса.
print("bayes  =", posterior)

# TODO: посчитайте модуль разницы.
# Подсказка: abs(direct - posterior).
difference = abs(direct - posterior)

# Печатаем разницу.
print("diff   =", difference)

# Определяем функцию скоринга вероятности покупки.
def score_buy_probability(recs, clicked_value):

    # Проверяем, что clicked_value равен 0 или 1.
    if clicked_value not in (0, 1):
        raise ValueError("clicked_value должен быть 0 или 1")

    # TODO: отберите только те записи, где clicked имеет нужное значение.
    # Подсказка: используйте list comprehension.
    subset = [r for r in recs if int(r["click"]) == clicked_value]

    # Проверяем, что такая группа не пустая.
    if len(subset) == 0:
        raise ValueError("Нет записей для такого clicked_value")

    # TODO: посчитайте, сколько пользователей в группе купили.
    buy_count = sum(1 for r in subset if int (r["buy"]) == 1)

    # TODO: посчитайте вероятность покупки внутри группы.
    probability_buy = buy_count / len(subset)

    # Возвращаем вероятность.
    return probability_buy


# TODO: посчитайте вероятность покупки среди тех, кто кликнул.
p_buy_click1 = score_buy_probability(records, 1)

# TODO: посчитайте вероятность покупки среди тех, кто не кликнул.
p_buy_click0 = score_buy_probability(records, 0)

# Печатаем результаты.
print("P(buy | click=1) =", p_buy_click1)
print("P(buy | click=0) =", p_buy_click0)

# Импортируем модуль для графиков.
import matplotlib.pyplot as plt

# Список названий столбцов графика.
labels = ["P(buy)", "P(buy | click=1)"]

# TODO: создайте список значений для столбцов.
# Подсказка: нужны prior и p_buy_click1.
values = [prior, p_buy_click1]

# Создаём график размером 7 на 4.
plt.figure(figsize=(7, 4))

# TODO: постройте столбчатую диаграмму.
# Подсказка: plt.bar(labels, values)
plt.bar(labels, values)

# Ограничиваем ось Y от 0 до 1, потому что вероятность не может быть больше 1.
plt.ylim(0, 1)

# Добавляем заголовок графика.
plt.title("Как клик меняет вероятность покупки")

# Подписываем ось Y.
plt.ylabel("Вероятность")

# Добавляем сетку, чтобы легче читать значения.
plt.grid(True)

# Автоматически улучшаем расположение элементов.
plt.tight_layout()

# Показываем график.
plt.show()

# Определяем функцию сглаживания Лапласа.
def laplace_smooth_prob(successes, trials):

    # Проверяем, что количество испытаний не отрицательное.
    if trials < 0:
        raise ValueError("trials не может быть отрицательным")

    # Проверяем, что количество успехов не отрицательное.
    if successes < 0:
        raise ValueError("successes не может быть отрицательным")

    # Проверяем, что успехов не больше, чем испытаний.
    if successes > trials:
        raise ValueError("successes не может быть больше trials")

    # TODO: примените формулу сглаживания Лапласа.
    # Подсказка: (successes + 1) / (trials + 2).
    probability_smooth = (successes + 1) / (trials + 3)

    # Возвращаем сглаженную вероятность.
    return probability_smooth


# TODO: отберите записи, где пользователь не кликнул.
subset_click0 = [r for r in records if int(r["click"]) == 0]

# TODO: посчитайте, сколько пользователей без клика купили.
successes_click0 = sum(1 for r in subset_click0 if int(r["buy"]) == 1)

# Считаем обычную вероятность покупки без клика.
raw_probability_click0 = p_buy_click0

# TODO: посчитайте сглаженную вероятность покупки без клика.
smooth_probability_click0 = laplace_smooth_prob(successes_click0, len(subset_click0))

# Печатаем обычную вероятность.
print("Обычная P(buy | click=0) =", raw_probability_click0)

# Печатаем сглаженную вероятность.
print("Сглаженная P(buy | click=0) =", smooth_probability_click0)


