import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")

print("Original Data:")
print(df)

df["Total"] = df["Quantity"] * df["Price"]

print("\nData with Total Column:")
print(df)

daily_sales = df["Total"].to_numpy()

total_sales = np.sum(daily_sales)
average_sales = np.mean(daily_sales)
std_dev_sales = np.std(daily_sales)

print("\nSales Analysis:")
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Standard Deviation of Daily Sales:", std_dev_sales)

product_sales = df.groupby("Product")["Quantity"].sum()

best_product = product_sales.idxmax()
best_quantity = product_sales.max()

print("\nBest-Selling Product:", best_product)
print("Total Quantity Sold:", best_quantity)
