import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:

    all_user = pd.concat([request_accepted['requester_id'], request_accepted['accepter_id']])

    user = all_user.value_counts()

    id = user.idxmax()
    count = user.max()

    return pd.DataFrame({'id': [id], 'num': [count]})

    
