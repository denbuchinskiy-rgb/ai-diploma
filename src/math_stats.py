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

# Импортируем numpy.
# Он нужен для работы с массивами и случайными числами.
import numpy as np

# TODO: создайте генератор случайных чисел.
# Подсказка: np.random.default_rng(42)
rng = np.random.default_rng(56)

# TODO: создайте 50 наблюдений нормального распределения.
# loc=10.0, scale=2.0, size=50
data = rng.normal(loc=15.0, scale=5.0, size=100)

# TODO: посчитайте размер выборки.
# Подсказка: len(data)
n = len(data)

# Печатаем размер выборки.
print("Размер выборки n =", n)

# Печатаем первые 5 значений.
print("Первые 5 значений:", data[:5])

# Определяем функцию mean.
# values — список или массив чисел.
def mean(values) -> float:

    # Если данных нет, среднее посчитать нельзя.
    if len(values) == 0:
        raise ValueError("mean: empty values")

    # TODO: посчитайте сумму всех значений.
    total = sum(values)

    # TODO: посчитайте количество значений.
    count = len(values)

    # TODO: разделите сумму на количество.
    result = total / count

    # Возвращаем результат как float.
    return float(result)


# TODO: посчитайте среднее по нашей выборке.
m = mean(data)

# Печатаем среднее.
print("Среднее =", round(m, 3))

# Определяем функцию выборочной дисперсии.
def variance_sample(values) -> float:

    # TODO: посчитайте количество значений.
    n = len(values)

    # Для дисперсии нужно минимум 2 значения.
    if n < 2:
        raise ValueError("variance_sample: need at least 2 values")

    # TODO: посчитайте среднее.
    m = mean(values)

    # TODO: посчитайте сумму квадратов отклонений от среднего.
    # Подсказка: sum((x - m) ** 2 for x in values)
    squared_deviation_sum = sum((x - m) ** 2 for x in values)

    # TODO: разделите на n - 1.
    result = squared_deviation_sum / (n - 1)

    # Возвращаем результат как float.
    return float(result)


# Определяем функцию выборочного стандартного отклонения.
def std_sample(values) -> float:

    # TODO: сначала посчитайте выборочную дисперсию.
    variance = variance_sample(values)

    # TODO: стандартное отклонение — квадратный корень из дисперсии.
    result = variance ** 0.5

    # Возвращаем результат.
    return result


# TODO: посчитайте стандартное отклонение по нашей выборке.
s = std_sample(data)

# Печатаем результат.
print("Стандартное отклонение =", round(s, 3))

# Определяем функцию стандартной ошибки среднего.
def sem(values) -> float:

    # TODO: посчитайте количество значений.
    n = len(values)

    # Если данных нет, SEM посчитать нельзя.
    if n <= 0:
        raise ValueError("sem: empty values")

    # TODO: посчитайте выборочное стандартное отклонение.
    s = std_sample(values)

    # TODO: посчитайте корень из n.
    sqrt_n = n ** 0.5

    # TODO: разделите стандартное отклонение на корень из n.
    result = s / sqrt_n

    # Возвращаем результат.
    return result


# TODO: посчитайте SEM по нашей выборке.
sem_val = sem(data)

# Печатаем SEM.
print("SEM =", round(sem_val, 4))

# Определяем функцию приближённого CI для среднего.
def ci_mean_normal_approx(values, z: float = 1.96):

    # TODO: посчитайте среднее.
    m = mean(values)

    # TODO: посчитайте стандартную ошибку среднего.
    se = sem(values)

    # TODO: посчитайте нижнюю границу интервала.
    low = m - z * se

    # TODO: посчитайте верхнюю границу интервала.
    high = m + z *se

    # Возвращаем границы интервала.
    return low, high


# TODO: постройте 95% CI для нашей выборки.
ci_norm = ci_mean_normal_approx(data)

# Распаковываем границы интервала.
ci_low_norm, ci_high_norm = ci_norm

# Печатаем результат.
print("Normal approx CI =", (round(ci_low_norm, 3), round(ci_high_norm, 3)))

# Определяем функцию bootstrap-средних.
def bootstrap_means(values, n_boot: int = 2000, seed: int = 0):

    # TODO: создайте генератор случайных чисел.
    rng = np.random.default_rng(seed)

    # TODO: преобразуйте values в numpy-массив.
    values = np.asarray(values)

    # TODO: посчитайте размер исходной выборки.
    n = len(values)

    # Если данных нет, bootstrap невозможен.
    if n == 0:
        raise ValueError("bootstrap_means: empty values")

    # Создаём пустой список для средних.
    means = []

    # Запускаем цикл n_boot раз.
    for _ in range(n_boot):

        # TODO: случайно выберите n индексов от 0 до n-1.
        idx = rng.integers(0, n, size=n)

        # TODO: возьмите элементы по выбранным индексам.
        sample_b = values[idx]

        # TODO: посчитайте среднее bootstrap-выборки.
        sample_mean = mean(sample_b)

        # TODO: добавьте среднее в список.
        means.append(sample_mean)

    # Возвращаем список средних.
    return means


# TODO: создайте 2000 bootstrap-средних.
boot_means = bootstrap_means(data, n_boot=2000, seed=1)

# Печатаем количество средних и первое значение.
print("Количество bootstrap-средних:", len(boot_means))
print("Первое bootstrap-среднее:", round(boot_means[0], 3))

# Определяем функцию bootstrap CI для среднего.
def bootstrap_ci_mean(values, n_boot: int = 2000, alpha: float = 0.05, seed: int = 0):

    # TODO: получите много bootstrap-средних.
    means = bootstrap_means(values, n_boot=n_boot, seed=seed)

    # TODO: посчитайте нижний квантиль alpha / 2.
    low = float(np.quantile(means, alpha / 2))

    # TODO: посчитайте верхний квантиль 1 - alpha / 2.
    high = float(np.quantile(means, 1 - alpha / 2))

    # Возвращаем границы интервала.
    return low, high


# TODO: постройте bootstrap CI.
ci_boot = bootstrap_ci_mean(data, n_boot=2000, alpha=0.05, seed=1)

# Распаковываем границы.
ci_low_boot, ci_high_boot = ci_boot

# Печатаем результат.
print("Bootstrap CI =", (round(ci_low_boot, 3), round(ci_high_boot, 3)))

# Импортируем matplotlib для графиков.
import matplotlib.pyplot as plt

# TODO: сохраните среднее исходной выборки.
m_hat = mean(data)

# Создаём график размером 8 на 4.
plt.figure(figsize=(8, 4))

# TODO: постройте гистограмму bootstrap-средних.
plt.hist(boot_means, bins=30)

# TODO: добавьте вертикальную линию исходного среднего.
plt.axvline(m_hat, linestyle="--", label="mean")

# TODO: добавьте вертикальную линию нижней границы CI.
plt.axvline(ci_low_boot, linestyle="--", label="CI low")

# TODO: добавьте вертикальную линию верхней границы CI.
plt.axvline(ci_high_boot, linestyle="--", label="CI high")

# Добавляем заголовок.
plt.title("Bootstrap-средние и 95% доверительный интервал")

# Подписываем ось X.
plt.xlabel("Среднее bootstrap-выборки")

# Подписываем ось Y.
plt.ylabel("Количество")

# Добавляем легенду.
plt.legend()

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение элементов.
plt.tight_layout()

# Показываем график.
plt.show()

# Печатаем значения.
print("mean =", round(m_hat, 3))
print("bootstrap CI =", (round(ci_low_boot, 3), round(ci_high_boot, 3)))

# TODO: создайте новый генератор случайных чисел.
rng2 = np.random.default_rng(12)

# TODO: создайте маленькую выборку из 20 значений.
data20 = rng2.normal(15.0, 2.0, 50)

# TODO: создайте большую выборку из 200 значений.
data200 = rng2.normal(15.0, 2.0, 250)

# TODO: постройте bootstrap CI для маленькой выборки.
ci20 = bootstrap_ci_mean(data20, n_boot=1500, seed=2)

# TODO: постройте bootstrap CI для большой выборки.
ci200 = bootstrap_ci_mean(data200, n_boot=1500, seed=2)

# TODO: посчитайте ширину CI для n=20.
width20 = ci20[1] - ci20[0]

# TODO: посчитайте ширину CI для n=200.
width200 = ci200[1] - ci200[0]

# Создаём график.
plt.figure(figsize=(6, 4))

# TODO: постройте столбчатую диаграмму ширин.
plt.bar(["n=50", "n=250"], [width20, width200])

# Добавляем заголовок.
plt.title("Чем больше данных, тем уже CI")

# Подписываем ось Y.
plt.ylabel("Ширина доверительного интервала")

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение.
plt.tight_layout()

# Показываем график.
plt.show()

# Печатаем ширины интервалов.
print("width n=20  =", round(width20, 3))
print("width n=200 =", round(width200, 3))

# Импортируем numpy.
# Эта библиотека нужна для массивов и случайных чисел.
import numpy as np

# TODO: создайте генератор случайных чисел.
# Подсказка: np.random.default_rng(1)
rng = np.random.default_rng(5)

# Задаём количество наблюдений.
n = 250

# TODO: создайте признак x.
# Подсказка: rng.normal(0.0, 1.0, n)
x = rng.normal(0.0, 1.0, n)

# TODO: создайте шум.
# Подсказка: rng.normal(0.0, 0.7, n)
noise = rng.normal(0.0, 0.7, n)

# Задаём коэффициент связи между x и y.
a = 3.0

# TODO: создайте y по формуле y = a * x + noise.
y = a * x + noise

# Печатаем размеры массивов.
print("len(x) =", len(x))
print("len(y) =", len(y))

# Печатаем первые значения, чтобы увидеть данные.
print("x[0] =", round(float(x[0]), 3))
print("y[0] =", round(float(y[0]), 3))

# Определяем функцию mean.
# values — это список или массив чисел.
def mean(values) -> float:

    # Если данных нет, среднее посчитать нельзя.
    if len(values) == 0:
        raise ValueError("mean: empty")

    # TODO: посчитайте сумму всех значений.
    total = sum(values)

    # TODO: посчитайте количество значений.
    count = len(values)

    # TODO: разделите сумму на количество.
    result = total / count

    # Возвращаем результат как float.
    return float(result)


# TODO: посчитайте среднее x.
mx = mean(x)

# TODO: посчитайте среднее y.
my = mean(y)

# Печатаем результаты.
print("mean(x) =", round(mx, 3))
print("mean(y) =", round(my, 3))

# Определяем функцию выборочной дисперсии.
def variance_sample(values) -> float:

    # TODO: посчитайте количество значений.
    n = len(values)

    # Для выборочной дисперсии нужно минимум 2 значения.
    if n < 2:
        raise ValueError("variance_sample: need >= 2")

    # TODO: посчитайте среднее.
    m = mean(values)

    # TODO: посчитайте сумму квадратов отклонений.
    # Подсказка: sum((v - m) ** 2 for v in values)
    squared_deviation_sum = sum((v - m) ** 2 for v in values)

    # TODO: разделите на n - 1.
    result = squared_deviation_sum / (n - 1)

    # Возвращаем результат как float.
    return float(result)


# Определяем функцию стандартного отклонения.
def std_sample(values) -> float:

    # TODO: сначала посчитайте дисперсию.
    variance = variance_sample(values)

    # TODO: стандартное отклонение — квадратный корень из дисперсии.
    result = variance ** 0.5

    # Возвращаем результат.
    return result


# TODO: посчитайте стандартное отклонение x.
sx = std_sample(x)

# TODO: посчитайте стандартное отклонение y.
sy = std_sample(y)

# Печатаем результаты.
print("std(x) =", round(sx, 3))
print("std(y) =", round(sy, 3))

# Определяем функцию выборочной ковариации.
def cov_sample(x_values, y_values) -> float:

    # Проверяем, что массивы имеют одинаковую длину.
    if len(x_values) != len(y_values):
        raise ValueError("cov_sample: lengths differ")

    # TODO: посчитайте количество пар.
    n = len(x_values)

    # Для ковариации нужно минимум 2 пары.
    if n < 2:
        raise ValueError("cov_sample: need >= 2")

    # TODO: посчитайте среднее x.
    mx = mean(x_values)

    # TODO: посчитайте среднее y.
    my = mean(y_values)

    # Создаём переменную для суммы произведений отклонений.
    deviation_product_sum = 0.0

    # zip(x_values, y_values) даёт пары xi, yi.
    for xi, yi in zip(x_values, y_values):

        # TODO: посчитайте произведение отклонений и добавьте к сумме.
        deviation_product_sum += (xi - mx) * (yi - my)

    # TODO: разделите на n - 1.
    result = deviation_product_sum / (n - 1)

    # Возвращаем результат.
    return result


# TODO: посчитайте ковариацию x и y.
cov_xy = cov_sample(x, y)

# Печатаем результат.
print("cov(x, y) =", round(cov_xy, 3))

# Определяем функцию корреляции Пирсона.
def corr_pearson(x_values, y_values) -> float:

    # TODO: посчитайте стандартное отклонение x.
    sx = std_sample(x_values)

    # TODO: посчитайте стандартное отклонение y.
    sy = std_sample(y_values)

    # Если одно из стандартных отклонений равно 0,
    # корреляция не определена.
    if sx == 0 or sy == 0:
        raise ValueError("corr_pearson: std is zero")

    # TODO: посчитайте ковариацию.
    covariance = cov_sample(x_values, y_values)

    # TODO: разделите ковариацию на произведение стандартных отклонений.
    result = covariance / (sx * sy)

    # Возвращаем корреляцию.
    return result


# TODO: посчитайте корреляцию между x и y.
r_xy = corr_pearson(x, y)

# Печатаем результат.
print("corr(x, y) =", round(r_xy, 3))

# Импортируем matplotlib для графиков.
import matplotlib.pyplot as plt

# Создаём график размером 7 на 5.
plt.figure(figsize=(7, 5))

# TODO: постройте scatter plot.
# Подсказка: plt.scatter(x, y)
plt.scatter(x, y)

# Добавляем заголовок.
plt.title("Положительная связь: y = 2*x + noise")

# Подписываем ось X.
plt.xlabel("x")

# Подписываем ось Y.
plt.ylabel("y")

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение элементов.
plt.tight_layout()

# Показываем график.
plt.show()

# Печатаем корреляцию.
print("corr r =", round(r_xy, 3))

# TODO: создайте новый шум для второго примера.
# Подсказка: rng.normal(0.0, 0.7, n)
noise2 = rng.normal(0.3, 0.5, n)

# TODO: создайте y2 с отрицательной связью.
# Подсказка: -1.5 * x + noise2
y2 = -1.5 * x + noise2

# TODO: посчитайте корреляцию между x и y2.
r_xy2 = corr_pearson(x, y2)

# Печатаем результат.
print("corr(x, y2) =", round(r_xy2, 3))

# Создаём график размером 7 на 5.
plt.figure(figsize=(7, 5))

# TODO: постройте scatter plot для отрицательной связи.
plt.scatter(x, y2)

# Добавляем заголовок.
plt.title("Отрицательная связь: y2 = -1.5*x + noise")

# Подписываем ось X.
plt.xlabel("x")

# Подписываем ось Y.
plt.ylabel("y2")

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение.
plt.tight_layout()

# Показываем график.
plt.show()

# Печатаем корреляцию.
print("corr r =", round(r_xy2, 3))

# Список уровней шума.
noise_scales = [0.5, 0.7, 1.1, 2.1, 6.0]

# Здесь будем хранить модули корреляций.
rs = []

# Запускаем цикл по всем уровням шума.
for noise_scale in noise_scales:

    # TODO: создайте шум с текущим уровнем разброса.
    current_noise = rng.normal(0.5, noise_scale, n)

    # TODO: создайте y3 с тем же правилом y = 2*x + noise.
    y3 = 3.0 * x + current_noise

    # TODO: посчитайте корреляцию.
    r = corr_pearson(x, y3)

    # TODO: добавьте модуль корреляции в список.
    rs.append(abs(r))

# Создаём график размером 7 на 4.
plt.figure(figsize=(7, 4))

# TODO: постройте столбчатую диаграмму.
plt.bar([str(v) for v in noise_scales], rs)

# Корреляция по модулю находится от 0 до 1.
plt.ylim(0, 1)

# Добавляем заголовок.
plt.title("Чем больше шум, тем слабее корреляция")

# Подписываем ось X.
plt.xlabel("Уровень шума")

# Подписываем ось Y.
plt.ylabel("|corr(x, y)|")

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение.
plt.tight_layout()

# Показываем график.
plt.show()

# Печатаем таблицу результатов.
result_table = list(zip(noise_scales, [round(v, 3) for v in rs]))
print(result_table)

# Импортируем numpy.
# Он нужен для числовых массивов и случайных чисел.
import numpy as np

# TODO: создайте генератор случайных чисел.
# Подсказка: np.random.default_rng(42)
rng = np.random.default_rng(42)

# Задаём количество точек.
n = 150

# TODO: создайте x: 80 чисел от 0 до 10.
# Подсказка: np.linspace(0, 10, n)
x = np.linspace(0, 15, n)

# TODO: создайте случайный шум.
# Подсказка: rng.normal(0, 2, n)
noise = rng.normal(0, 5, n)

# TODO: создайте y по правилу y = 3*x + 5 + noise.
y = 3 * x + 5 + noise

# Печатаем первые значения.
print("x[:5] =", x[:5])
print("y[:5] =", y[:5])

# Импортируем matplotlib для графиков.
import matplotlib.pyplot as plt

# Создаём график размером 7 на 5.
plt.figure(figsize=(7, 5))

# TODO: постройте scatter plot.
# Подсказка: plt.scatter(x, y)
plt.scatter(x, y)

# Добавляем заголовок.
plt.title("Данные для линейной регрессии")

# Подписываем ось X.
plt.xlabel("x")

# Подписываем ось Y.
plt.ylabel("y")

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение элементов.
plt.tight_layout()

# Показываем график.
plt.show()

# Функция среднего значения.
def mean(values) -> float:

    # Если данных нет, среднее посчитать нельзя.
    if len(values) == 0:
        raise ValueError("mean: empty values")

    # TODO: суммируйте значения и разделите на количество.
    return float(sum(values) / len(values))


# Функция дисперсии.
def variance_population(values) -> float:

    # TODO: посчитайте среднее.
    m = mean(values)

    # TODO: посчитайте средний квадрат отклонения от среднего.
    result = sum((v - m) ** 2 for v in values) / len(values)

    # Возвращаем дисперсию.
    return float(result)


# Функция ковариации.
def cov_population(x_values, y_values) -> float:

    # Проверяем, что массивы одинаковой длины.
    if len(x_values) != len(y_values):
        raise ValueError("x and y must have the same length")

    # TODO: посчитайте среднее x.
    mx = mean(x_values)

    # TODO: посчитайте среднее y.
    my = mean(y_values)

    # TODO: посчитайте среднее произведение отклонений.
    result = sum((xi - mx) * (yi - my)
    for xi, yi in zip(x_values, y_values)) / len(x_values)

    # Возвращаем ковариацию.
    return float(result)


# TODO: посчитайте дисперсию x.
var_x = variance_population(x)

# TODO: посчитайте ковариацию x и y.
cov_xy = cov_population(x, y)

# Печатаем результаты.
print("var(x) =", round(var_x, 3))
print("cov(x, y) =", round(cov_xy, 3))

# Функция обучения простой линейной регрессии.
def fit_linear_regression_1d(x_values, y_values):

    # TODO: посчитайте дисперсию x.
    var_x = variance_population(x_values)

    # Если все x одинаковые, линию построить нельзя.
    if var_x == 0:
        raise ValueError("variance of x is zero")

    # TODO: посчитайте ковариацию x и y.
    cov_xy = cov_population(x_values, y_values)

    # TODO: посчитайте наклон линии.
    a = cov_xy / var_x

    # TODO: посчитайте свободный коэффициент.
    b = mean(y_values) - a * mean(x_values)

    # Возвращаем коэффициенты.
    return float(a), float(b)


# TODO: обучите модель.
a_hat, b_hat = fit_linear_regression_1d(x, y)

# Печатаем коэффициенты.
print("a_hat =", round(a_hat, 3))
print("b_hat =", round(b_hat, 3))

# Функция прогноза по линейной модели.
def predict_linear_1d(x_values, a, b):

    # Преобразуем x_values в numpy-массив.
    x_values = np.asarray(x_values)

    # Считаем прогноз по формуле y_hat = a*x + b.
    y_hat = a * x_values + b

    # Возвращаем прогноз.
    return y_hat


# Делаем прогноз для всех x.
y_hat = predict_linear_1d(x, a_hat, b_hat)

# Печатаем первые 5 прогнозов.
print("y_hat[:5] =", y_hat[:5])

# Функция MSE.
def mse(y_true, y_pred) -> float:

    # TODO: преобразуйте y_true в numpy-массив.
    y_true = np.asarray(y_true)

    # TODO: преобразуйте y_pred в numpy-массив.
    y_pred = np.asarray(y_pred)

    # Проверяем, что длины совпадают.
    if len(y_true) != len(y_pred):
        raise ValueError("mse: lengths differ")

    # TODO: посчитайте ошибки.
    errors = y_true - y_pred

    # TODO: посчитайте квадраты ошибок.
    squared_errors = errors ** 2

    # TODO: посчитайте среднее квадратов ошибок.
    result = np.mean(squared_errors)

    # Возвращаем MSE.
    return float(result)


# TODO: посчитайте MSE нашей модели.
model_mse = mse(y, y_hat)

# Печатаем MSE.
print("model MSE =", round(model_mse, 3))

# Создаём график размером 8 на 5.
plt.figure(figsize=(8, 5))

# TODO: нарисуйте исходные точки.
plt.scatter(x, y, label="data")

# TODO: нарисуйте линию регрессии.
plt.plot(x, y_hat, label="linear regression")

# Добавляем заголовок.
plt.title("Линейная регрессия 1D")

# Подписываем ось X.
plt.xlabel("x")

# Подписываем ось Y.
plt.ylabel("y")

# Добавляем легенду.
plt.legend()

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение.
plt.tight_layout()

# Показываем график.
plt.show()

# TODO: посчитайте остатки модели.
residuals = y - y_hat

# TODO: посчитайте средний остаток.
residual_mean = mean(residuals)

# Печатаем первые 5 остатков.
print("residuals[:5] =", residuals[:5])

# Печатаем средний остаток.
print("mean residual =", round(residual_mean, 6))

# Создаём график размером 8 на 4.
plt.figure(figsize=(8, 4))

# TODO: постройте точки остатков.
plt.scatter(x, residuals)

# TODO: нарисуйте горизонтальную линию на уровне 0.
plt.axhline(0, linestyle="--")

# Добавляем заголовок.
plt.title("График остатков")

# Подписываем ось X.
plt.xlabel("x")

# Подписываем ось Y.
plt.ylabel("residual = y - y_hat")

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение.
plt.tight_layout()

# Показываем график.
plt.show()

# Импортируем numpy.
# Он нужен для массивов и случайных чисел.
import numpy as np

# TODO: создайте генератор случайных чисел.
# Подсказка: np.random.default_rng(123)
rng = np.random.default_rng(123)

# Задаём размер группы A.
nA = 100

# Задаём размер группы B.
nB = 100

# TODO: создайте группу A.
# Подсказка: rng.normal(50.0, 10.0, nA)
A = rng.normal(60.0, 15.0, nA)

# TODO: создайте группу B.
# Подсказка: rng.normal(54.0, 10.0, nB)
B = rng.normal(64.0, 15.0, nB)

# Печатаем первые значения.
print("A[:5] =", A[:5])
print("B[:5] =", B[:5])

# Функция среднего значения.
def mean(values) -> float:

    # Если список пустой, среднее посчитать нельзя.
    if len(values) == 0:
        raise ValueError("mean: empty")

    # TODO: суммируйте значения и разделите на количество.
    result = sum(values) / len(values)

    # Возвращаем результат как float.
    return float(result)


# TODO: посчитайте среднее группы A.
mean_A = mean(A)

# TODO: посчитайте среднее группы B.
mean_B = mean(B)

# TODO: посчитайте наблюдаемую разницу средних.
diff_obs = mean_B - mean_A

# Печатаем результаты.
print("mean(A) =", round(mean_A, 3))
print("mean(B) =", round(mean_B, 3))
print("diff_obs = mean(B) - mean(A) =", round(diff_obs, 3))

# TODO: соедините группы A и B в один общий массив.
# Подсказка: np.concatenate([A, B])
pool = np.concatenate([A, B])

# TODO: перемешайте общий массив.
# Подсказка: rng.permutation(pool)
perm = rng.permutation(pool)

# TODO: первые nA значений назначьте в случайную группу A.
A_perm = perm[:nA]

# TODO: остальные значения назначьте в случайную группу B.
B_perm = perm[nA:]

# TODO: посчитайте разницу средних после одной перестановки.
diff_perm = mean(B_perm) - mean(A_perm)

# Печатаем результат.
print("diff_perm =", round(diff_perm, 3))

# Функция перестановочного теста для разницы средних.
def permutation_test_diff_means(A, B, n_perm: int = 2000, seed: int = 0):

    # TODO: создайте генератор случайных чисел.
    rng = np.random.default_rng(seed)

    # TODO: преобразуйте A в numpy-массив.
    A = np.asarray(A)

    # TODO: преобразуйте B в numpy-массив.
    B = np.asarray(B)

    # TODO: сохраните размер группы A.
    nA = len(A)

    # TODO: сохраните размер группы B.
    nB = len(B)

    # Проверяем, что группы не пустые.
    if nA == 0 or nB == 0:
        raise ValueError("permutation_test: empty group")

    # TODO: соедините группы в общий массив.
    pool = np.concatenate([A,B])

    # Создаём пустой список для случайных разниц.
    diffs = []

    # Делаем n_perm перестановок.
    for _ in range(n_perm):

        # TODO: перемешайте общий массив.
        perm = rng.permutation(pool)

        # TODO: первые nA значений идут в переставленную группу A.
        A_perm = perm[:nA]

        # TODO: остальные значения идут в переставленную группу B.
        B_perm = perm[nA:]

        # TODO: посчитайте случайную разницу средних.
        diff = mean(B_perm) - mean(A_perm)

        # TODO: добавьте её в список.
        diffs.append(diff)

    # Возвращаем список случайных разниц.
    return diffs


# TODO: запустите 2000 перестановок.
diffs = permutation_test_diff_means(A, B, n_perm=2000, seed=1)

# Печатаем количество разниц и первую разницу.
print("len(diffs) =", len(diffs))
print("diffs[0] =", round(diffs[0], 3))

# Функция расчёта двустороннего p-value.
def p_value_two_sided(diff_obs: float, diffs_perm) -> float:

    # Преобразуем diffs_perm в список.
    diffs_perm = list(diffs_perm)

    # Если список пустой, p-value считать нельзя.
    if len(diffs_perm) == 0:
        raise ValueError("p_value_two_sided: empty diffs")

    # TODO: посчитайте, сколько случайных разниц не меньше наблюдаемой по модулю.
    # Подсказка: abs(d) >= abs(diff_obs)
    count = sum(1 for d in diffs_perm if abs(d) >= abs(diff_obs))

    # TODO: разделите количество таких случаев на общее количество перестановок.
    result = count / len(diffs_perm)

    # Возвращаем p-value.
    return result


# TODO: посчитайте p-value для нашего наблюдаемого diff_obs.
p_val = p_value_two_sided(diff_obs, diffs)

# Печатаем результат.
print("diff_obs =", round(diff_obs, 3))
print("p_value =", round(p_val, 5))

# Импортируем matplotlib для графиков.
import matplotlib.pyplot as plt

# Создаём график размером 8 на 4.
plt.figure(figsize=(8, 4))

# TODO: постройте гистограмму перестановочных разниц.
plt.hist(diffs, bins=30)

# TODO: нарисуйте линию наблюдаемой разницы.
plt.axvline(diff_obs, linestyle="--", label="-diff_obs")

# TODO: нарисуйте линию противоположной разницы для двустороннего теста.
plt.axvline(-diff_obs, linestyle="--", label="-diff_obs")

# Добавляем заголовок.
plt.title("Перестановочное распределение при H0")

# Подписываем ось X.
plt.xlabel("diff = mean(B) - mean(A)")

# Подписываем ось Y.
plt.ylabel("Количество")

# Добавляем легенду.
plt.legend()

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение.
plt.tight_layout()

# Показываем график.
plt.show()

# Печатаем результаты.
print("diff_obs =", round(diff_obs, 3))
print("p_value =", round(p_val, 4))

# Функция принятия решения.
def decision(p_value: float, alpha: float = 0.05) -> str:

    # Проверяем корректность p_value.
    if p_value < 0 or p_value > 1:
        raise ValueError("p_value must be from 0 to 1")

    # Проверяем корректность alpha.
    if alpha <= 0 or alpha >= 1:
        raise ValueError("alpha must be from 0 to 1")

    # TODO: если p-value меньше alpha, верните текст о значимости.
    if p_value < alpha:
        return "значимо: отклоняем H0"

    # Иначе мы не доказали эффект.
    return "не значимо: не отклоняем H0"


# TODO: получите решение.
test_decision = decision(p_val, alpha=0.05)

# Печатаем решение.
print(test_decision)

# Функция выборочного стандартного отклонения.
def std_sample(values) -> float:

    # Преобразуем values в список.
    values = list(values)

    # TODO: посчитайте количество значений.
    n = len(values)

    # Для стандартного отклонения нужно минимум 2 значения.
    if n < 2:
        raise ValueError("std_sample: need >= 2")

    # TODO: посчитайте среднее.
    m = mean(values)

    # TODO: посчитайте выборочную дисперсию.
    variance = sum((v - m) ** 2 for v in values) / (n - 1)

    # TODO: верните квадратный корень из дисперсии.
    return float(variance * 0.5)


# Функция Cohen's d.
def cohens_d(A, B) -> float:

    # Преобразуем группы в списки.
    A = list(A)
    B = list(B)

    # TODO: посчитайте стандартное отклонение группы A.
    sA = std_sample(A)

    # TODO: посчитайте стандартное отклонение группы B.
    sB = std_sample(B)

    # TODO: посчитайте pooled standard deviation.
    pooled = ((sA ** 2 + sB ** 2)/ 2) ** 0.5

    # Если pooled = 0, d считать нельзя.
    if pooled == 0:
        raise ValueError("cohens_d: pooled std is 0")

    # TODO: посчитайте Cohen's d.
    d = (mean(B) - mean(A)) / pooled

    # Возвращаем результат.
    return float(d)


# TODO: посчитайте размер эффекта.
d = cohens_d(A, B)

# Печатаем результат.
print("Cohen's d =", round(d, 3))

# Функция симуляции A/B-теста и расчёта p-value.
def ab_sim_pvalue(n: int, seed: int) -> float:

    # TODO: создайте генератор случайных чисел.
    rng = np.random.default_rng(seed)

    # TODO: создайте группу A.
    A_sim = rng.normal(55.0, 15.0, n)

    # TODO: создайте группу B.
    B_sim = rng.normal(60.0, 15.0, n)

    # TODO: посчитайте наблюдаемую разницу.
    diff_obs_sim = mean(B_sim) - mean(A_sim)

    # TODO: постройте перестановочное распределение.
    diffs_sim = permutation_test_diff_means(A_sim, B_sim, n_perm=1200, seed=seed + 1)

    # TODO: посчитайте p-value.
    p = p_value_two_sided(diff_obs_sim, diffs_sim)

    # Возвращаем p-value.
    return p


# Размеры выборок для сравнения.
ns = [30, 60, 150]

# TODO: посчитайте p-value для каждого размера выборки.
pvals = [ab_sim_pvalue(n, seed=10 + n) for n in ns]

# Создаём график.
plt.figure(figsize=(10, 8))

# TODO: постройте столбчатую диаграмму.
plt.bar([str(n) for n in ns], pvals)

# p-value находится от 0 до 1.
plt.ylim(0, 1)

# Добавляем заголовок.
plt.title("p-value обычно уменьшается при росте размера выборки")

# Подписываем ось X.
plt.xlabel("Размер группы n")

# Подписываем ось Y.
plt.ylabel("p-value")

# Добавляем сетку.
plt.grid(True)

# Улучшаем расположение.
plt.tight_layout()

# Показываем график.
plt.show()

# Печатаем результаты.
print(list(zip(ns, [round(p, 4) for p in pvals])))

# Импортируем numpy.
# Он нужен для работы с числовыми массивами.
import numpy as np

# Создаём первый вектор a.
# dtype=float означает, что числа будут вещественными.
a = np.array([1.5, 2.5, 3.5], dtype=float)

# Создаём второй вектор b.
b = np.array([2.5, 1.5, 0.5], dtype=float)

# Печатаем векторы.
print("a =", a)
print("b =", b)

# Печатаем форму векторов.
print("a.shape =", a.shape)
print("b.shape =", b.shape)

# Определяем функцию dot.
def dot(u, v) -> float:

    # Преобразуем u в список.
    u = list(u)

    # Преобразуем v в список.
    v = list(v)

    # Проверяем, что длины векторов совпадают.
    if len(u) != len(v):
        raise ValueError("dot: length mismatch")

    # Перемножаем пары элементов и суммируем результаты.
    result = sum(ui * vi for ui, vi in zip(u, v))

    # Возвращаем результат как float.
    return float(result)


# Считаем скалярное произведение a и b.
ab = dot(a, b)

# Печатаем результат.
print("dot(a, b) =", ab)

# Определяем функцию длины вектора.
def norm2(u) -> float:

    # Преобразуем u в список.
    u = list(u)

    # Считаем сумму квадратов элементов.
    squares_sum = sum(ui * ui for ui in u)

    # Берём квадратный корень.
    result = squares_sum ** 0.5

    # Возвращаем результат.
    return float(result)


# Считаем длину вектора a.
na = norm2(a)

# Считаем длину вектора b.
nb = norm2(b)

# Печатаем результаты.
print("norm2(a) =", round(na, 3))
print("norm2(b) =", round(nb, 3))

# Определяем функцию cosine similarity.
def cosine_similarity(u, v) -> float:

    # Считаем скалярное произведение.
    d = dot(u, v)

    # Считаем длину первого вектора.
    nu = norm2(u)

    # Считаем длину второго вектора.
    nv = norm2(v)

    # Если длина одного из векторов равна 0,
    # cosine similarity считать нельзя.
    if nu == 0 or nv == 0:
        raise ValueError("cosine_similarity: zero norm")

    # Делим dot на произведение длин.
    result = d / (nu * nv)

    # Возвращаем результат.
    return float(result)


# Считаем похожесть a и b.
cos_ab = cosine_similarity(a, b)

# Печатаем результат.
print("cosine_similarity(a, b) =", round(cos_ab, 3))

# Создаём матрицу X.
# В ней 5 строк и 3 столбца.
X = np.array([
    [0.1, 0.0, 0.2],
    [0.0, 0.2, 0.1],
    [0.2, 0.0, 0.1],
    [0.0, 0.1, 0.2],
    [0.1, 0.2, 0.0],
], dtype=float)

# Создаём вектор весов w.
w = np.array([0.5, -1.0, 2.0], dtype=float)

# Печатаем размеры.
print("X.shape =", X.shape)
print("w.shape =", w.shape)

# Определяем функцию умножения матрицы на вектор.
def matvec(X, w):

    # Преобразуем X в numpy-массив.
    X = np.asarray(X)

    # Преобразуем w в numpy-массив.
    w = np.asarray(w)

    # Проверяем, что X — двумерная матрица.
    if X.ndim != 2:
        raise ValueError("matvec: X must be 2D")

    # Проверяем, что w — одномерный вектор.
    if w.ndim != 1:
        raise ValueError("matvec: w must be 1D")

    # Проверяем совместимость размеров.
    # Для того чтобы можно было умножить матрицу на вектор (или две матрицы),
    # количество столбцов первой матрицы (в нашем случае X)
    # должно быть равно количеству строк второй матрицы
    # (в нашем случае вектор w рассматривается как матрица
    # с w.shape[0] строками и 1 столбцом).
    if X.shape[1] != w.shape[0]:
        raise ValueError("matvec: shape mismatch")

    # Для каждой строки row считаем dot(row, w).
    result = np.array([dot(row, w) for row in X], dtype=float)

    # Возвращаем массив score.
    return result


# Считаем y_hat вручную через нашу функцию.
y_hat_manual = matvec(X, w)

# Считаем y_hat через встроенный оператор @.
y_hat_np = X @ w

# Печатаем оба результата.
print("manual =", y_hat_manual)
print("numpy  =", y_hat_np)

# Считаем разность двух результатов.
difference_vector = y_hat_manual - y_hat_np

# Берём модуль каждой разности.
abs_difference = np.abs(difference_vector)

# Находим максимальную абсолютную разницу.
diff = float(np.max(abs_difference))

# Печатаем результат.
print("max|diff| =", diff)

# Импортируем matplotlib для графиков.
import matplotlib.pyplot as plt

# Берём первые две координаты вектора a.
a2 = a[:2]

# Берём первые две координаты вектора b.
b2 = b[:2]

# Создаём график размером 6 на 6.
plt.figure(figsize=(6, 6))

# Рисуем горизонтальную ось.
plt.axhline(0)

# Рисуем вертикальную ось.
plt.axvline(0)

# Рисуем вектор a как стрелку из точки (0, 0).
plt.quiver(0, 0, a2[0], a2[1], angles="xy", scale_units="xy", scale=1)

# Рисуем вектор b как стрелку из точки (0, 0).
plt.quiver(0, 0, b2[0], b2[1], angles="xy", scale_units="xy", scale=1)

# Подписываем вектор a.
plt.text(a2[0], a2[1], "a")

# Подписываем вектор b.
plt.text(b2[0], b2[1], "b")

# Ограничиваем область графика.
plt.xlim(-1, 3)
plt.ylim(-1, 3)

# Добавляем заголовок.
plt.title("Векторы a и b в 2D")

# Добавляем сетку.
plt.grid(True)

# Делаем одинаковый масштаб по осям.
plt.axis("equal")

# Показываем график.
plt.show()

# Создаём маленькую базу векторов.
E = np.array([
    [0.1, 0.0, 0.2],
    [0.0, 0.2, 0.1],
    [0.2, 0.0, 0.1],
    [0.0, 0.1, 0.2],
    [0.1, 0.2, 0.0],
], dtype=float)

# Создаём вектор запроса q.
q = np.array([1.0, 0.2, 0.1], dtype=float)

# Считаем похожесть q с каждой строкой E.
sims = [cosine_similarity(q, row) for row in E]

# Находим индекс самого похожего вектора.
# Строка best_idx = int(np.argmax(sims)) используется для нахождения индекса элемента
# с максимальным значением в списке sims.

#Давайте разберем по частям:

#sims: это список (или массив numpy), который содержит значения cosine similarity
#между вектором запроса q и каждым из векторов в базе E. То есть, каждое число
#в sims показывает, насколько похож запрос на соответствующий вектор из базы.

#np.argmax(sims): это функция из библиотеки NumPy, которая возвращает индекс первого
# вхождения максимального значения в массиве sims.
#Например, если sims = [0.976, 0.195, 0.098], то np.argmax(sims) вернет 0,
# потому что 0.976 (максимальное значение) находится по индексу 0.
#int(...): это функция, которая преобразует результат
# (индекс, который np.argmax возвращает как тип numpy.int64)
# в стандартный питоновский тип int.
#Таким образом, вся строка best_idx = int(np.argmax(sims)) находит индекс того вектора
# из базы E, который имеет наибольшую похожесть (наибольший cosine similarity)
# с вектором запроса q. Этот индекс best_idx затем можно использовать, чтобы получить сам лучший вектор или соответствующий ему документ.

best_idx = int(np.argmax(sims))

# Находим лучшую похожесть.
best_score = float(sims[best_idx])

# Печатаем все похожести.
print("sims =", [round(s, 3) for s in sims])

# Печатаем лучший результат.
print("best_idx =", best_idx)
print("best_score =", round(best_score, 3))

# Импортируем numpy.
# Сокращённое имя np принято использовать почти во всех проектах.
import numpy as np

# TODO: создайте первый вектор v1.
# Подсказка: np.array([2.0, 1.0])
v1 = np.array([2.5, 1.5])

# TODO: создайте второй вектор v2.
# Подсказка: np.array([1.0, 3.0])
v2 = np.array([1.5, 3.5])

# Печатаем первый вектор.
print("v1 =", v1)

# Печатаем второй вектор.
print("v2 =", v2)

# TODO: возьмите первую координату вектора v1.
x1 = v1[0]

# TODO: возьмите вторую координату вектора v1.
y1 = v2[1]

# Печатаем координаты.
print("x1 =", x1)
print("y1 =", y1)

# Определяем функцию длины двумерного вектора.
def vector_length_2d(v) -> float:

    # Проверяем, что у вектора две координаты.
    if len(v) != 2:
        raise ValueError("vector_length_2d: нужен вектор длины 2")

    # TODO: возьмите первую координату.
    x = v[0]

    # TODO: возьмите вторую координату.
    y = v[1]

    # TODO: посчитайте сумму квадратов координат.
    squares_sum = x ** 2 + y ** 2

    # TODO: возьмите квадратный корень.
    length = squares_sum ** 0.5

    # Возвращаем длину как float.
    return float(length)


# TODO: посчитайте длину v1.
len_v1_manual = vector_length_2d(v1)

# TODO: посчитайте длину v2.
len_v2_manual = vector_length_2d(v2)

# Печатаем результаты.
print("Длина v1 вручную =", round(len_v1_manual, 3))
print("Длина v2 вручную =", round(len_v2_manual, 3))

# TODO: посчитайте длину v1 через NumPy.
len_v1_np = np.linalg.norm(v1)

# TODO: посчитайте длину v2 через NumPy.
len_v2_np = np.linalg.norm(v2)

# Печатаем результаты.
print("Длина v1 через NumPy =", round(len_v1_np, 3))
print("Длина v2 через NumPy =", round(len_v2_np, 3))

# TODO: сложите векторы.
v_sum = v1 + v2

# Печатаем результат.
print("v1 + v2 =", v_sum)

# Создаём ожидаемый ответ.
expected_sum = np.array([3.0, 4.0])

# Задаём число, на которое умножаем вектор.
k = 2.0

# TODO: умножьте вектор на число.
v_scaled = k * v1

# TODO: посчитайте длину нового вектора.
len_scaled = np.linalg.norm(v_scaled)

# Печатаем результат.
print("2 * v1 =", v_scaled)
print("Длина 2*v1 =", round(len_scaled, 3))

# Определяем функцию скалярного произведения для 2D-векторов.
def dot_2d(a, b) -> float:

    # Проверяем длину первого вектора.
    if len(a) != 2:
        raise ValueError("dot_2d: первый вектор должен иметь длину 2")

    # Проверяем длину второго вектора.
    if len(b) != 2:
        raise ValueError("dot_2d: второй вектор должен иметь длину 2")

    # TODO: перемножьте первые координаты.
    first_product = a[0] * b[0]

    # TODO: перемножьте вторые координаты.
    second_product = a[1] * b[1]

    # TODO: сложите произведения.
    result = first_product + second_product

    # Возвращаем результат.
    return float(result)


# TODO: посчитайте скалярное произведение вручную.
dot_manual = dot_2d(v1, v2)

# Печатаем результат.
print("dot_2d(v1, v2) =", dot_manual)

# TODO: посчитайте скалярное произведение через NumPy.
dot_np = np.dot(v1, v2)

# Печатаем результат.
print("np.dot(v1, v2) =", dot_np)

# Импортируем matplotlib для графиков.
import matplotlib.pyplot as plt

# Создаём график.
plt.figure(figsize=(6, 6))

# Рисуем горизонтальную ось.
plt.axhline(0)

# Рисуем вертикальную ось.
plt.axvline(0)

# TODO: нарисуйте вектор v1 как стрелку из точки (0, 0).
plt.quiver(0, 0, v1[0], v1[1], angles="xy", scale_units="xy", scale=1)

# TODO: нарисуйте вектор v2 как стрелку из точки (0, 0).
plt.quiver(0, 0, v2[0], v2[1], angles="xy", scale_units="xy", scale=1)

# TODO: нарисуйте сумму векторов.
plt.quiver(0, 0, v_sum[0], v_sum[1], angles="xy", scale_units="xy", scale=1)

# Подписываем v1.
plt.text(v1[0], v1[1], "v1")

# Подписываем v2.
plt.text(v2[0], v2[1], "v2")

# Подписываем v1 + v2.
plt.text(v_sum[0], v_sum[1], "v1+v2")

# Задаём границы по оси X.
plt.xlim(-1, 5)

# Задаём границы по оси Y.
plt.ylim(-1, 5)

# Делаем одинаковый масштаб по осям.
plt.axis("equal")

# Добавляем заголовок.
plt.title("Векторы v1, v2 и их сумма")

# Добавляем сетку.
plt.grid(True)

# Показываем график.
plt.show()
