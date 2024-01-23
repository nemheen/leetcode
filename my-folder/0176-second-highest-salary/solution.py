import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates()

    second = salaries.nlargest(2).iloc[-1] if len(salaries) >= 2 else None
    if second is None:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
       return pd.DataFrame({'SecondHighestSalary': [second]})


