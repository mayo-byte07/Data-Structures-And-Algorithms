import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Group by player_id and find the minimum event_date
    result = activity.groupby('player_id', as_index=False)['event_date'].min()
    
    # Rename the column to match the expected output
    result = result.rename(columns={'event_date': 'first_login'})
    
    return result