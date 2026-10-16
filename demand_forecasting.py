"""Demand forecasting coursework: reviewed portfolio edition.

Original coursework: Aynaz Chabouk. Revision prepared with Codex assistance.
The original submission and revision notes are stored alongside this file.
"""
import math
import sys
from typing import Sequence


def forecast(sales: Sequence[float], window: int, alpha: float,
             actual: float) -> tuple[float, float, float, float]:
    """Return moving average, smoothed forecast, and their percentage errors."""
    if not sales or not all(math.isfinite(x) and x >= 0 for x in sales):
        raise ValueError("Sales must be a nonempty sequence of finite nonnegative values.")
    if not 1 <= window <= len(sales):
        raise ValueError("Window must be between 1 and the number of observations.")
    if not math.isfinite(alpha) or not 0 <= alpha <= 1:
        raise ValueError("Alpha must be between 0 and 1.")
    if not math.isfinite(actual) or actual <= 0:
        raise ValueError("Actual demand must be finite and positive.")
    moving_average = sum(sales[-window:]) / window
    smoothed = sum(sales) / len(sales)
    for observation in sales:
        smoothed = alpha * observation + (1 - alpha) * smoothed
    return (moving_average, smoothed,
            abs(moving_average - actual) / actual * 100,
            abs(smoothed - actual) / actual * 100)


def main() -> None:
    sales = [float(value) for value in input().split()]
    window = int(input())
    alpha = float(input())
    actual = float(input())
    moving, smoothed, error1, error2 = forecast(sales, window, alpha, actual)
    print(round(moving))
    print(round(smoothed))
    if math.isclose(error1, error2, rel_tol=1e-12, abs_tol=1e-12):
        print(f"Either method is viable with {error1:.3f} error percentage")
    else:
        method, error = (1, error1) if error1 < error2 else (2, error2)
        print(f"Forecasting method{method} is more optimized with {error:.3f} error percentage")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, EOFError) as exc:
        print(f"Invalid input: {exc}", file=sys.stderr)
        raise SystemExit(2)
