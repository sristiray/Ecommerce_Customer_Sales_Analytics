import pandas as pd

df = pd.read_csv("data/ecommerce_sales.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("=== EDA SUMMARY ===")

print("\n1. Total Revenue:", df["Total_Amount"].sum())

print("2. Total Orders:", df["Order_ID"].nunique())

print("3. Total Customers:", df["Customer_ID"].nunique())

print("4. Total Units Sold:", df["Quantity"].sum())

print("5. Average Order Value:", round(df["Total_Amount"].mean(), 2))

print("\n=== TOP CATEGORIES ===")
print(
    df.groupby("Category")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== TOP 10 PRODUCTS ===")
print(
    df.groupby("Product")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n=== CITY-WISE REVENUE ===")
print(
    df.groupby("City")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== EDA COMPLETE ===")