import pandas as pd

df = pd.read_csv("laptop_price - dataset.csv")
print("Checking missing data: ")
print(df.isnull().sum(), "\n\n\n")
