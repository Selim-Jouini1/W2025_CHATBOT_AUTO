import pandas as pd
import re

def load_and_clean_data(filepath):
    # Load CSV file into a DataFrame
    df = pd.read_csv(filepath)

    # Clean data: Remove special characters, handle km/mi conversion, etc.
    df = clean_car_type(df)
    df = clean_km(df)
    df = clean_price(df)
    # df['CleanedCarType'] = df['CarType'].apply(clean_car_type)

    return df

def clean_car_type(df):
    # Remove extra digits at the end of car types (e.g., BMW1 becomes BMW)
    df['CarType'] = df['CarType'].apply(lambda x: re.sub(r'\d+$', '', str(x)).strip())
    return df

def clean_km_value(val):
    # If the value is empty or NaN, return None or a default value like 0
    if not val or pd.isna(val):
        return None  # or return 0 if you prefer
    
    # Clean the value: remove 'km', 'mi', and any special characters
    val = str(val).replace('km', '').replace('mi', '').replace(' ', '').replace(' ', '').replace(',', '').strip()

    # If the value contains 'mi' (miles), convert it to kilometers
    if 'mi' in val:
        try:
            val = int(val)
            val = val * 1.60934  # Convert miles to kilometers
        except ValueError:
            return None  # Return None for invalid values
    else:
        try:
            val = int(val)
        except ValueError:
            return None  # Return None for invalid values
    
    return val

def clean_km(df):
    df['Kilometrage'] = df['Kilometrage'].apply(clean_km_value)
    return df

def clean_price(df):
    # Clean price column: Remove currency symbols and special characters
    def clean_price_value(val):
        val = str(val).replace('$', '').replace(' ', '').replace(' ', '').replace(',', '').strip()
        return float(val)
    
    df['Price'] = df['Price'].apply(clean_price_value)
    return df

# def clean_car_type(car_type):
#     if isinstance(car_type, str):  # Check if car_type is a string
#         return re.sub(r'\d+$', '', car_type)  # Removes trailing digits from CarType
#     return car_type

def get_car_problems(brand, model, year):
    # Load the CSV data
    df = pd.read_csv("data/cars.csv")
    
    # Filter the rows based on the extracted entities (CarBrand, CarModel, Year)
    filtered_data = df[(df["CarType"].str.lower() == brand.lower()) &
                        (df["CarModel"].str.lower() == model.lower()) &
                        (df["Year"] == int(year))]
    
    if not filtered_data.empty:
        # Assuming 'Problems' column contains the problems for the car
        problems = filtered_data["Problems"].iloc[0]
        return problems
    else:
        return "Sorry, I don't have information about that car's problems."