import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])
    date_ranges = sales.groupby('product_id')['sale_date'].agg(['min', 'max']).reset_index()
    q1_only = date_ranges[
        (date_ranges['min'] >= '2019-01-01') & 
        (date_ranges['max'] <= '2019-03-31')
    ]
    result = q1_only.merge(product, on='product_id')[['product_id', 'product_name']]
    
    return result