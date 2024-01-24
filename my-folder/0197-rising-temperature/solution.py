import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather['prev_temp'] = weather['temperature'].shift()
    weather['prev_day'] = weather['recordDate'].shift()

    res = weather[(weather['temperature']>weather['prev_temp']) & (weather['recordDate']-weather['prev_day']==pd.Timedelta(days=1))]

    return res[['id']]
