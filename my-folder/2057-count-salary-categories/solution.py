import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    lows = accounts[accounts['income'] < 20000].shape[0]
    avs = accounts[(accounts['income'] <= 50000) & (accounts['income'] >= 20000)].shape[0]
    highs = accounts[accounts['income'] > 50000].shape[0]

    data = {
        'category': ['High Salary', 'Average Salary', 'Low Salary'], 
        'accounts_count': [highs, avs, lows]}
    df = pd.DataFrame(data)
    return df
