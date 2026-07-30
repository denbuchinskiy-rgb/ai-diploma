"""Векторы, матрицы, cosine similarity из занятий 9 и 11."""

from __future__ import annotations

import numpy as np


def dot(u, v) -> float:
    """Скалярное произведение."""
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    if u.shape != v.shape:
        raise ValueError("dot: shape mismatch")
    return float(np.sum(u * v))


def norm2(u) -> float:
    """Длина вектора."""
    u = np.asarray(u, dtype=float)
    return float(np.sqrt(np.sum(u * u)))


def cosine_similarity(u, v) -> float:
    """Cosine similarity."""
    nu = norm2(u)
    nv = norm2(v)
    if nu == 0 or nv == 0:
        raise ValueError("cosine_similarity: zero vector")
    return float(dot(u, v) / (nu * nv))


def matvec(X, w):
    """Умножение матрицы на вектор через dot по строкам."""
    X = np.asarray(X, dtype=float)
    w = np.asarray(w, dtype=float)
    if X.ndim != 2:
        raise ValueError("matvec: X must be 2D")
    if w.ndim != 1:
        raise ValueError("matvec: w must be 1D")
    if X.shape[1] != w.shape[0]:
        raise ValueError("matvec: shape mismatch")
    return np.array([dot(row, w) for row in X], dtype=float)


def vector_length_2d(v) -> float:
    """Длина двумерного вектора из занятия 11."""
    v = np.asarray(v, dtype=float)
    if len(v) != 2:
        raise ValueError("vector_length_2d: need vector length 2")
    return float((v[0] ** 2 + v[1] ** 2) ** 0.5)


def dot_2d(a, b) -> float:
    """Скалярное произведение двумерных векторов."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if len(a) != 2 or len(b) != 2:
        raise ValueError("dot_2d: need vectors length 2")
    return float(a[0] * b[0] + a[1] * b[1])
