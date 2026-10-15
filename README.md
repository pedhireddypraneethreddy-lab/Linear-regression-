# Study Hours vs Marks Prediction

Beginner-friendly machine learning script that trains a scikit-learn linear regression model on students.csv to predict exam marks from daily study hours. Includes a sample dataset, requirements file, and README so you can clone, run, and learn regression in minutes.

## Setup

```bash
git clone https://github.com/<your-username>/study-hours-marks-prediction.git
cd study-hours-marks-prediction
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

The script reads `students.csv` (columns `Study_Hours` and `Marks`), fits a `LinearRegression` model, and predicts the marks for a student who studies 5 hours. Change the value in `new_data` to try other inputs, or replace the CSV with your own data (keep the column names, or edit them in `main.py`).

## Sample output

```
Predicted Marks: [59.2969697]
```

## Notes

- The sample dataset is small and made up for demonstration, so treat predictions as illustrative.
- Passing a DataFrame with the same column name used in training (`Study_Hours`) avoids scikit-learn's feature-name warning.
