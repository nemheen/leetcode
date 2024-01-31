import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    res = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    res.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return res
