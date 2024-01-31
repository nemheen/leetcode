import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame(columns=['customer_number'])

    n = orders.groupby('customer_number')['order_number'].nunique().idxmax()

    return pd.DataFrame({'customer_number': [n]})
