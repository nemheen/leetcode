import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = [0]*(employees.shape[0])
    mask = (employees['employee_id']%2==1) & (~employees['name'].str.startswith('M'))
    employees.loc[mask, 'bonus'] = employees.loc[mask, 'salary']
    employees = employees.sort_values(['employee_id'])
    return employees[['employee_id', 'bonus']]

