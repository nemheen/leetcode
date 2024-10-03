import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.loc[
        views['author_id'] == views['viewer_id']].rename(columns={
        'author_id': 'id',
    }).sort_values(
        by=['id'],
    )

    return df[['id']].drop_duplicates()
    
