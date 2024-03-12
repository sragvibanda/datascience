"""
2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

"""

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

min_price_mean = df['Min.Price'].mean()
max_price_mean = df['Max.Price'].mean()

df_replaced = df.copy()  # Create a copy to keep the original DataFrame unchanged
df_replaced['Min.Price'] = df_replaced['Min.Price'].fillna(min_price_mean)
df_replaced['Max.Price'] = df_replaced['Max.Price'].fillna(max_price_mean)

print(df_replaced.head())
