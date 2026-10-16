# Demand Forecasting Coursework in Python

Author of the original submission: **Aynaz Chabouk**. Fundamentals of Programming, Sharif University of Technology, Fall 2023.

The final submission for the Quera exercise "Demand Forecasting" received **100/100**. Submission 13823550, 28 December 2023. The score was observed in the signed-in course submission history. It applies to the original submission, not to the revised code.

- [Reviewed portfolio version](demand_forecasting.py)
- [Original submitted algorithm](demand_forecasting_original.py)
- [Course problem](https://quera.org/course/assignments/61840/problems/212295) (course access may be required)

The exercise compares a simple moving average over the last N observations with exponential smoothing, then calculates absolute percentage error against a supplied actual value.

## Revision history

The original algorithm is preserved. Only its generated Colab metadata and notebook link were removed. Its smoothing loop repeatedly uses the first observation; it also truncates intermediate values, has inconsistent tie output, and does not validate input.

The portfolio revision was prepared with Codex assistance. It updates the smoothing state for every observation, retains floating-point precision, handles ties in a single branch, and validates the window, alpha and actual value. It follows the mathematical definitions in the exercise; it does not claim compatibility with the historic grader's formatting or inconsistent example error percentage.

## Run

Python 3, standard library only:

```text
python demand_forecasting.py
```

Input: four lines containing the sales history, window size N, smoothing factor alpha and actual demand. Forecasts use Python's round-to-even convention. Error percentages use unrounded forecasts and a positive actual demand.

Independent checks cover a known smoothing recurrence, alpha endpoints, a one-period window, equal-method output, fractional values and invalid inputs. The revised script is a small educational example, not a production forecasting model.
