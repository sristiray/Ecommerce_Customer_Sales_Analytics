import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="E-Commerce Analytics",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 E-Commerce Customer & Sales Analytics")
st.markdown("### Business Performance + AI Dashboard")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("data/ecommerce_sales.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔎 Filters")

categories = ["All"] + sorted(df["Category"].unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

cities = ["All"] + sorted(df["City"].unique().tolist())
selected_city = st.sidebar.selectbox("Select City", cities)

filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

if selected_city != "All":
    filtered_df = filtered_df[
        filtered_df["City"] == selected_city
    ]

# -----------------------------
# KPI Cards
# -----------------------------
total_revenue = filtered_df["Total_Amount"].sum()
total_orders = filtered_df["Order_ID"].nunique()
total_customers = filtered_df["Customer_ID"].nunique()
total_units = filtered_df["Quantity"].sum()

aov = total_revenue / total_orders if total_orders > 0 else 0

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("💰 Revenue", f"₹{total_revenue:,.0f}")
col2.metric("🛒 Orders", f"{total_orders:,}")
col3.metric("👥 Customers", f"{total_customers:,}")
col4.metric("📦 Units Sold", f"{total_units:,}")
col5.metric("📈 Avg Order Value", f"₹{aov:,.0f}")

st.divider()

# -----------------------------
# Charts
# -----------------------------
st.subheader("📈 Monthly Sales Trend")

monthly_sales = (
    filtered_df
    .groupby(filtered_df["Order_Date"].dt.to_period("M"))["Total_Amount"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

st.line_chart(monthly_sales)

st.subheader("📊 Category-wise Revenue")

category_sales = (
    filtered_df
    .groupby("Category")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_sales)

st.subheader("🏆 Top 10 Products")

top_products = (
    filtered_df
    .groupby("Product")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)

# -----------------------------
# AI BUSINESS INSIGHTS
# -----------------------------
st.divider()
st.header("🤖 AI Business Insights")

if len(filtered_df) > 0:

    best_category = (
        filtered_df.groupby("Category")["Total_Amount"]
        .sum()
        .idxmax()
    )

    best_city = (
        filtered_df.groupby("City")["Total_Amount"]
        .sum()
        .idxmax()
    )

    best_product = (
        filtered_df.groupby("Product")["Total_Amount"]
        .sum()
        .idxmax()
    )

    st.success(
        f"💡 **Business Insight:** {best_category} "
        f"is the highest-revenue category."
    )

    st.info(
        f"📍 **Location Insight:** {best_city} "
        f"generated the highest revenue."
    )

    st.warning(
        f"🏆 **Product Insight:** {best_product} "
        f"is the highest-revenue product."
    )

# -----------------------------
# Sales Prediction
# -----------------------------
st.subheader("🔮 AI Sales Prediction")

monthly = (
    filtered_df
    .groupby(filtered_df["Order_Date"].dt.to_period("M"))["Total_Amount"]
    .sum()
    .reset_index()
)

if len(monthly) >= 2:

    monthly["Month_Number"] = np.arange(len(monthly))

    X = monthly[["Month_Number"]]
    y = monthly["Total_Amount"]

    model = LinearRegression()
    model.fit(X, y)

    next_month = [[len(monthly)]]
    prediction = model.predict(next_month)[0]

    st.metric(
        "Predicted Next Month Revenue",
        f"₹{prediction:,.0f}"
    )

# -----------------------------
# Customer Segmentation
# -----------------------------
st.subheader("👥 Customer Segmentation")

customer_data = filtered_df.groupby("Customer_ID").agg(
    Total_Spending=("Total_Amount", "sum"),
    Total_Orders=("Order_ID", "nunique")
).reset_index()

def segment_customer(row):
    if row["Total_Spending"] >= 100000:
        return "High Value"
    elif row["Total_Spending"] >= 50000:
        return "Medium Value"
    else:
        return "Low Value"

customer_data["Segment"] = customer_data.apply(
    segment_customer,
    axis=1
)

segment_counts = customer_data["Segment"].value_counts()

st.bar_chart(segment_counts)

# -----------------------------
# Anomaly Detection
# -----------------------------
st.subheader("🚨 Anomaly Detection")

mean_amount = filtered_df["Total_Amount"].mean()
std_amount = filtered_df["Total_Amount"].std()

upper_limit = mean_amount + (2 * std_amount)

anomalies = filtered_df[
    filtered_df["Total_Amount"] > upper_limit
]

st.write(
    f"Detected **{len(anomalies)} unusual high-value transactions**."
)

if len(anomalies) > 0:
    st.dataframe(
        anomalies[
            [
                "Order_ID",
                "Product",
                "Category",
                "Total_Amount",
                "City"
            ]
        ].head(10),
        use_container_width=True
    )

# -----------------------------
# Data Preview
# -----------------------------
st.divider()
st.subheader("📋 Filtered Sales Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)