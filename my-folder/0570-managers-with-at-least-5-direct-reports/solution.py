import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Group by 'managerId' and count the occurrences
    manager_counts = employee['managerId'].value_counts()

    # Filter managers with at least five direct reports
    managers_with_five_reports = manager_counts[manager_counts >= 5].index

    # Filter employees whose 'id' is in managers_with_five_reports
    result = employee[employee['id'].isin(managers_with_five_reports)][['name']]

    return result

