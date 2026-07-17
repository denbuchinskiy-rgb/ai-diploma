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