import numpy as np

from src.block04_linear_algebra import dot, norm2, cosine_similarity, matvec, vector_length_2d, dot_2d

def test_linear_algebra():
    assert dot([1, 2, 3], [2, 1, 0]) == 4.0
    assert norm2([3, 4]) == 5.0
    assert cosine_similarity([1, 0], [1, 0]) == 1.0
    X = np.array([[1, 2], [3, 4]], dtype=float)
    w = np.array([10, 1], dtype=float)
    assert np.allclose(matvec(X, w), X @ w)
    assert vector_length_2d([3, 4]) == 5.0
    assert dot_2d([2, 1], [1, 3]) == 5.0
