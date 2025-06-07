import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(students[['id', 'first', 'last', 'age']].values, columns=['student_id', 'first_name', 'last_name', 'age_in_years'])
