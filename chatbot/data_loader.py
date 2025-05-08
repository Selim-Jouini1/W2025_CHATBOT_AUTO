import pandas as pd
import re

def clean_price(val):
    if isinstance(val, str):
        return float(val.replace('\u202f', '').replace('$', '').replace(' ', '').replace(' ', '').replace(',', '.'))
    return val

def clean_km(val):
    if isinstance(val, str):
        numbers = re.findall(r'\d+', val)
        if numbers:
            return int(''.join(numbers))  
    return None  

def clean_car_type(val):
    if isinstance(val, str):
        return re.sub(r'\d+$', '', val)  
    return val

def load_data(filepath):
    df = pd.read_csv(filepath, low_memory=False)
    df['Price'] = df['Price'].apply(clean_price)
    df['Kilometrage'] = df['Kilometrage'].apply(clean_km)
    df['CarType'] = df['CarType'].apply(clean_car_type)
    return df

