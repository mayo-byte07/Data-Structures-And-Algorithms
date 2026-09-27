import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicates = person[person.duplicated(subset=['email'])]
    result = duplicates[['email']].drop_duplicates().rename(columns={'email': 'Email'})
    
    return result