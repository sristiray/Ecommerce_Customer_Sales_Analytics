import pandas as pd

df = pd.read_csv("data/ecommerce_sales.csv")

# Customer-wise analysis
customer_data = df.groupby("Customer_ID").agg(
    Total_Spending=("Total_Amount", "sum"),
    Total_Orders=("Order_ID", "nunique"),
    Total_Quantity=("Quantity", "sum")
).reset_index()

# Customer segmentation
def segment_customer(row):
    if row["Total_Spending"] >= 100000:
        return "High Value"
    elif row["Total_Spending"] >= 50000:
        return "Medium Value"
    else:
        return "Low Value"

customer_data["Segment"] = customer_data.apply(
    segment_customer, axis=1
)

print("=== CUSTOMER SEGMENTATION ===")

print("\nSegment Summary:")
print(customer_data["Segment"].value_counts())

print("\nSample Customer Segments:")
print(customer_data.head(10))

print("\n=== SEGMENTATION COMPLETE ===")