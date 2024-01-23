import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if employee.empty or department.empty:
        return pd.DataFrame(columns=['Department','Employee', 'Salary'])
    merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))

    high = merged.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])

    high = high.reset_index(drop=True)

    res = high[['name_department', 'name_employee', 'salary']]

    res.columns = ['Department', 'Employee', 'Salary']

    return res

    
