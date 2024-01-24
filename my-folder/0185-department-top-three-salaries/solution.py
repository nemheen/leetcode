import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
   
    merged = employee.merge(department, left_on="departmentId", right_on="id", suffixes=['_employee', '_department'])
    ranked = merged[merged.groupby('departmentId').salary.rank(method='dense',ascending=False)<=3]
    
    
    # Reset index to avoid duplicate index values
    ranked = ranked.reset_index(drop=True)

    # Extract the required columns for the final result
    res = ranked[['name_department', 'name_employee', 'salary']]

    # Rename columns
    res.columns = ['Department', 'Employee', 'Salary']
    

    return res


    

