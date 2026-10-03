# 🛒 E-Commerce Customer & Sales Analytics

An interactive E-Commerce Analytics Dashboard built using Python, Pandas, SQL, Machine Learning and Streamlit.

The project analyzes customer behavior, sales performance, products, categories, cities and payment methods, while also providing AI-based business insights and sales prediction.

---

## 📌 Project Overview

This project is designed to analyze e-commerce sales data and convert raw transaction data into meaningful business insights.

The dashboard provides:

- Sales performance analysis
- Customer analysis
- Product and category analysis
- Location-wise revenue analysis
- Payment method analysis
- Monthly sales trends
- Customer segmentation
- Anomaly detection
- AI-based business insights
- Next-month sales prediction
- Interactive filters

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- SQL
- SQLite
- Scikit-learn
- Streamlit
- Matplotlib
- Git & GitHub

---

## 📊 Dataset

The dataset contains **500 e-commerce transactions**.

### Main Features

- Order ID
- Order Date
- Customer ID
- Customer Name
- Product
- Category
- Quantity
- Unit Price
- Total Amount
- City
- Payment Method

---

## 🚀 Key Features

### 📈 Sales Analytics

- Total Revenue
- Total Orders
- Total Customers
- Units Sold
- Average Order Value
- Monthly Sales Trend

### 📦 Product & Category Analysis

- Category-wise Revenue
- Top 10 Products
- Low-performing Products
- Product performance analysis

### 👥 Customer Analytics

- Customer spending analysis
- New vs Repeat Customers
- Customer Segmentation

### 📍 Location Analysis

- City-wise Revenue
- Highest-revenue cities

### 💳 Payment Analysis

- Payment method distribution
- Revenue by payment method

### 🤖 AI & Machine Learning Features

#### Business Insights
Automatically identifies:

- Highest-revenue category
- Highest-revenue city
- Highest-revenue product

#### Sales Prediction
Uses **Linear Regression** to estimate next-month revenue based on historical monthly sales.

#### Customer Segmentation
Customers are grouped into:

- High Value
- Medium Value
- Low Value

based on total spending.

#### Anomaly Detection
Identifies unusually high-value transactions using a statistical threshold based on mean and standard deviation.

---

## 🎛️ Interactive Streamlit Dashboard

The dashboard includes:

- Category filter
- City filter
- KPI cards
- Sales charts
- Product analysis
- AI business insights
- Sales prediction
- Customer segmentation
- Anomaly detection
- Filtered data table

---

## 📁 Project Structure

```text
Ecommerce_Customer_Sales_Analytics/
│
├── data/
│   └── ecommerce_sales.csv
│
├── sql/
│
├── python/
│   ├── import_data.py
│   ├── customer_analysis.py
│   ├── location_analysis.py
│   ├── payment_analysis.py
│   ├── low_performing_products.py
│   ├── final_sql_analysis.py
│   ├── pandas_analysis.py
│   ├── visualization.py
│   ├── ai_insights.py
│   ├── sales_prediction.py
│   ├── customer_segmentation.py
│   ├── anomaly_detection.py
│   └── ai_data_assistant.py
│
├── dashboard/
│   └── app.py
│
├── ecommerce.db
└── README.md