import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    words_list = patients['conditions'].str.split()

    # Check if any word in the list starts with "DIAB1"
    mask = words_list.apply(lambda words: any(word.startswith('DIAB1') for word in words if pd.notna(word)))
    
    # Return the filtered DataFrame
    return patients.loc[mask]

    
