import sqlite3

conn = sqlite3.connect("ecommerce.db")

query = """
SELECT
    ROUND(SUM(Total_Amount), 2) AS Total_Revenue,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Total_Customers,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(AVG(Total_Amount), 2) AS Average_Order_Value
FROM sales;
"""

result = conn.execute(query).fetchone()

print("=== FINAL BUSINESS SUMMARY ===")
print("Total Revenue:", result[0])
print("Total Orders:", result[1])
print("Total Customers:", result[2])
print("Total Units Sold:", result[3])
print("Average Order Value:", result[4])

conn.close()