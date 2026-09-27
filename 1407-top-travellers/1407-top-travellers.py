import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = users.merge(rides, left_on='id', right_on='user_id', how='left')
    df['distance'] = df['distance'].fillna(0)
    result = df.groupby(['id_x', 'name'], as_index=False)['distance'].sum()
    result = result.rename(columns={'distance': 'travelled_distance'})
    result = result.sort_values(by=['travelled_distance', 'name'], ascending=[False, True])
    return result[['name', 'travelled_distance']]