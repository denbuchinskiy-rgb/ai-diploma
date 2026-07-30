"""Графики из занятий 2, 6, 7, 8, 10, 11."""

from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt


def save_histogram(values, title: str, xlabel: str, path: str | Path, bins: int = 20) -> None:
    """Сохранить гистограмму."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(8, 4))
    plt.hist(values, bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Количество")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def save_scatter(x, y, title: str, xlabel: str, ylabel: str, path: str | Path) -> None:
    """Сохранить scatter plot."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(7, 5))
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def save_regression_plot(x, y, y_hat, path: str | Path) -> None:
    """Сохранить точки и линию регрессии."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label="data")
    plt.plot(x, y_hat, label="linear regression")
    plt.title("Линейная регрессия 1D")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def save_vectors_2d(vectors: dict, path: str | Path) -> None:
    """Сохранить рисунок 2D-векторов."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    for label, vector in vectors.items():
        ax.arrow(0, 0, vector[0], vector[1], length_includes_head=True, head_width=0.12, head_length=0.18, linewidth=2)
        ax.text(vector[0] + 0.08, vector[1] + 0.08, label, fontsize=12)
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
