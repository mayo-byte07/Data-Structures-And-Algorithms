import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    condition = (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M'))
    employees.loc[condition, 'bonus'] = employees['salary']
    result = employees[['employee_id', 'bonus']].sort_values(by='employee_id')
    return result