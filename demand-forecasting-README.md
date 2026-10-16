# Demand Forecasting Coursework in Python

Author of the original submission: **Aynaz Chabouk**. Fundamentals of Programming, Sharif University of Technology, Fall 2023.

The final submission for the Quera exercise "Demand Forecasting" received **100/100**. Submission 13823550, 28 December 2023. The score was observed in the signed-in course submission history. It applies to the original submission, not to the revised code.

- [Reviewed portfolio version](demand_forecasting.py)
- [Original submitted algorithm](demand_forecasting_original.py)
- [Course problem](https://quera.org/course/assignments/61840/problems/212295) (course access may be required)

The exercise compares a simple moving average over the last N observations with exponential smoothing, then calculates absolute percentage error against a supplied actual value.

## Run

Python 3, standard library only:

```text
python demand_forecasting.py
```

Input: four lines containing the sales history, window size N, smoothing factor alpha and actual demand. Forecasts use Python's round-to-even convention. Error percentages use unrounded forecasts and a positive actual demand.

Independent checks cover a known smoothing recurrence, alpha endpoints, a one-period window, equal-method output, fractional values and invalid inputs. The revised script is a small educational example, not a production forecasting model.
