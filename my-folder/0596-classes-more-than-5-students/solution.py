import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    k = courses.groupby('class')['student'].nunique().reset_index()
    return k[k['student'] >= 5][['class']]
