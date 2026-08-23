import pandas as pd
import numpy as np

# Day 3 Morning: Load and Handle Missing Values
data = {
    'product_id': [101, 102, 103, 104, 101], # 101 is a duplicate
    'price': ['£20.50', '£15.00', np.nan, '£12.99', '£20.50'],
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', 'invalid_date', '2023-01-01'],
    'description': ['  New Phone  ', 'Old laptop', 'Tablet', '  charger  ', '  New Phone  ']
}
df = pd.DataFrame(data)

# Handle missing values
df['price'] = df['price'].fillna('£0.00')

# Day 3 Afternoon: Fix Data Types & Standardize Text
df['price'] = df['price'].str.replace('£', '').astype(float)
df['date'] = pd.to_datetime(df['date'], errors='coerce') # 'invalid_date' becomes NaT
df['description'] = df['description'].str.strip().str.lower()
df = df.drop_duplicates()

# Day 4 Morning: Rename and reorder
df = df.rename(columns={'description': 'item_name'})
df = df[['date', 'product_id', 'item_name', 'price']] # Reorder

# Day 4 Afternoon: Export
df.to_csv('cleaned_data.csv', index=False)