import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if employee['salary'].unique().shape[0] < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        distinct_employee_salaries = employee['salary'].unique()
        sorted_salaries = np.sort(distinct_employee_salaries)[::-1]
        # sorted_employee_salary = employee['salary'].unique().sort_values(by='salary', ascending=False)
        second_salary = sorted_salaries[1]
        return pd.DataFrame({'SecondHighestSalary':[second_salary]})
