import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/ecommerce_sales.csv")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Monthly sales
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Amount"]
    .sum()
    .reset_index()
)

monthly_sales["Month_Number"] = np.arange(len(monthly_sales))

X = monthly_sales[["Month_Number"]]
y = monthly_sales["Total_Amount"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next month
next_month = [[len(monthly_sales)]]
prediction = model.predict(next_month)[0]

print("=== SALES PREDICTION ===")
print("Predicted Next Month Revenue: ₹", round(prediction, 2))
print("=== PREDICTION COMPLETE ===")