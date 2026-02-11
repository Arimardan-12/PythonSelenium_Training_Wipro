import pandas as pd

file_name = "sales_data.xlsx"
sheet_name = "2025"
output_file = "sales_summary.xlsx"


df = pd.read_excel(file_name, sheet_name=sheet_name)

print("Original Data:")
print(df)


df["Total"] = df["Quantity"] * df["Price"]

print("\nData After Adding Total Column:")
print(df)


df.to_excel(output_file, index=False)

print(f"\nFile saved successfully as '{output_file}' using Pandas.")
