import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    valid_pairs = counts[counts['count'] >= 3]
    return valid_pairs[['actor_id', 'director_id']]