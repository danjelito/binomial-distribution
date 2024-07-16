# Binomial Probability Simulation

This project simulates the binomial probability of success for a given number of shots taken by multiple players. It also calculates the binomial probability using both manual and automatic methods, and visualizes the distribution of successful shots.

## Usage

To run the simulation and plot the histogram, execute the following command:
```sh
python main.py
```

## Functions

### take_shot

```python
def take_shot(p: float) -> int:
    """
    Simulates a single shot with a given probability of success.

    Parameters:
    - p (float): Probability of a successful shot.

    Returns:
    - int: 1 if the shot is successful, 0 otherwise.
    """
```

### take_multiple_shots

```python
def take_multiple_shots(n: int, p: float) -> int:
    """
    Simulates multiple shots and counts the number of successful shots.

    Parameters:
    - n (int): Number of shots to simulate.
    - p (float): Probability of a successful shot.

    Returns:
    - int: Number of successful shots out of the total simulated shots.
    """
```

### percentage_formatter

```python
def percentage_formatter(x, pos):
    """
    Custom formatter for displaying values as percentages.

    Parameters:
    - x: The tick value.
    - pos: The tick position.

    Returns:
    - str: Formatted string representing the percentage.
    """
```

### calculate_binom_proba

```python
def calculate_binom_proba(n: int, k: int, p: float, method: Union["manual", "auto"]) -> float:
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
```

### plot_histogram

```python
def plot_histogram(data):
    """
    Plot a histogram of the given data.

    Parameters:
    - data: The input data for the histogram.
    """
```

## Examples

To simulate 10,000 players taking 10 shots each with a 0.6 chance of success:

```python
if __name__ == "__main__":
    n_players = 10_000
    n = 10  # 10 shots
    p = 0.6  # 0.6 chance of success
    results = []
    for _ in range(n_players):
        results.append(take_multiple_shots(n, p))
    plot_histogram(results)
```

To calculate the probability of exactly 7 successes out of 10 shots with a 0.6 chance of success:

```python
k = 7  # 7 successes
print(calculate_binom_proba(n, k, p, "manual"))
print(calculate_binom_proba(n, k, p, "auto"))
```

## Credits

This project is an implementation inspired by a very good [YouTube video on binomial probability](https://www.youtube.com/embed/6YzrVUVO9M0?si=DaGY1sRIGEN58aD1). Highly recommended to check it.
