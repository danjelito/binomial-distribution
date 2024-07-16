import random
from math import factorial
from typing import Literal

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from scipy import stats


def take_shot(p: float) -> int:
    """
    Simulates a single shot with a given probability of success.

    Parameters:
    - p (float): Probability of a successful shot.

    Returns:
    - int: 1 if the shot is successful, 0 otherwise.
    """
    return random.choices([1, 0], weights=[p, 1 - p])[0]


def take_multiple_shots(n: int, p: float) -> int:
    """
    Simulates multiple shots and counts the number of successful shots.

    Parameters:
    - n (int): Number of shots to simulate.
    - p (float): Probability of a successful shot.

    Returns:
    - int: Number of successful shots out of the total simulated shots.
    """
    n_success = 0
    for _ in range(n):
        n_success += take_shot(p)
    return n_success


def percentage_formatter(x, pos):
    """
    Custom formatter for displaying values as percentages.

    Parameters:
    - x: The tick value.
    - pos: The tick position.

    Returns:
    - str: Formatted string representing the percentage.
    """
    return f"{x:.0%}"


def calculate_binom_proba(
    n: int, k: int, p: float, method: Literal["manual", "auto"]
) -> float:
    """
    Calculate the binomial probability using either the "manual" or "auto" method.

    Parameters:
    - n (int): Number of trials.
    - k (int): Number of successful trials.
    - p (float): Probability of success in a single trial.
    - method (Union["manual", "auto"]): Method to use for calculation.

    Returns:
    - float: Calculated binomial probability.
    """
    if method == "auto":
        return stats.binom.pmf(k, n, p)
    elif method == "manual":
        binom_coef = factorial(n) / (factorial(k) * factorial(n - k))
        return binom_coef * p**k * (1 - p) ** (n - k)
    else:
        raise ValueError("Invalid method. Use 'auto' or 'manual'.")


def plot_histogram(data):
    """
    Plot a histogram of the given data.

    Parameters:
    - data: The input data for the histogram.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.histplot(data=data, ax=ax, binwidth=1, binrange=(0, 11), stat="density")
    for p in ax.patches:
        ax.annotate(
            format(p.get_height(), ".0%"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 10),
            textcoords="offset points",
        )
    ax.set_title(
        "Distribution of Successful Shots\n10,000 Samples Taking 10 Shots Each"
    )
    ax.set_ylim((0.0, 0.4))
    ax.yaxis.set_major_formatter(FuncFormatter(percentage_formatter))
    ax.set_xlabel("Successful Shots")
    ax.set_ylabel("Percentage")
    plt.show()


if __name__ == "__main__":
    # simulate 10_000 players taking 10 shots each
    n_players = 10_000
    n = 10  # 10 shots
    p = 0.6  # 0.6 chance of success
    results = []
    for _ in range(n_players):
        results.append(take_multiple_shots(n, p))
    plot_histogram(results)

    # probability of exacty 7 successes
    # this should be the same with what is in the plot
    k = 7  # 7 success
    print(calculate_binom_proba(n, k, p, "manual"))
    print(calculate_binom_proba(n, k, p, "auto"))
