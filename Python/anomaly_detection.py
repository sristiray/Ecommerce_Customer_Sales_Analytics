import pandas as pd

df = pd.read_csv("data/ecommerce_sales.csv")

# Calculate statistics
mean_amount = df["Total_Amount"].mean()
std_amount = df["Total_Amount"].std()

# Define anomaly limits
upper_limit = mean_amount + (2 * std_amount)
lower_limit = mean_amount - (2 * std_amount)

# Detect anomalies
anomalies = df[
    (df["Total_Amount"] > upper_limit) |
    (df["Total_Amount"] < lower_limit)
]

print("=== ANOMALY DETECTION ===")

print("\nAverage Transaction Amount:",
      round(mean_amount, 2))

print("Upper Limit:",
      round(upper_limit, 2))

print("Lower Limit:",
      round(lower_limit, 2))

print("\nNumber of Anomalies:",
      len(anomalies))

print("\nAnomalous Transactions:")
print(
    anomalies[
        ["Order_ID", "Product", "Category", "Total_Amount", "City"]
    ].head(10)
)

print("\n=== ANOMALY DETECTION COMPLETE ===")