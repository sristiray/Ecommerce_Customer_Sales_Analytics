import pandas as pd

df = pd.read_csv("data/ecommerce_sales.csv")

# Basic calculations
total_revenue = df["Total_Amount"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_ID"].nunique()

category_sales = (
    df.groupby("Category")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
)

city_sales = (
    df.groupby("City")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_product = (
    df.groupby("Product")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

print("=== AI BUSINESS INSIGHTS ===")

print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")

print(
    f"\nInsight 1: {category_sales.index[0]} "
    f"is the highest-revenue category."
)

print(
    f"Insight 2: {city_sales.index[0]} "
    f"generated the highest revenue among cities."
)

print(
    f"Insight 3: {top_product} "
    f"is the highest-revenue product."
)

print("\n=== INSIGHT GENERATION COMPLETE ===")