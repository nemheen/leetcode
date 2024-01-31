import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # Define the aggregation functions for each column
    aggregation = {
        'lead_id': 'nunique',
        'partner_id': 'nunique'
    }

    # Apply the aggregation using agg()
    result = daily_sales.groupby(['date_id', 'make_name']).agg(aggregation).reset_index().rename(columns={'lead_id':'unique_leads', 'partner_id':'unique_partners'})


    return result

