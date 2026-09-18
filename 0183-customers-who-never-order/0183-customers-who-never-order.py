import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    never_ordered = customers[~customers['id'].isin(orders['customerId'])]
    result = never_ordered[['name']].rename(columns={'name': 'Customers'})
    return result