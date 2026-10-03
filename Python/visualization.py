import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ecommerce_sales.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# 1. Monthly Revenue
monthly_sales = df.groupby(
    df["Order_Date"].dt.to_period("M")
)["Total_Amount"].sum()

monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Category Revenue
category_sales = df.groupby("Category")["Total_Amount"].sum()

category_sales.plot(kind="bar")
plt.title("Category-wise Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Top 10 Products
top_products = (
    df.groupby("Product")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products.plot(kind="bar")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("=== VISUALIZATION COMPLETE ===")