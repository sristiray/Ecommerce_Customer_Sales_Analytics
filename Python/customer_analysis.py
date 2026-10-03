import sqlite3

conn = sqlite3.connect("ecommerce.db")

query = """
SELECT
    CASE
        WHEN order_count = 1 THEN 'New Customer'
        ELSE 'Repeat Customer'
    END AS Customer_Type,
    COUNT(*) AS Number_of_Customers
FROM (
    SELECT
        Customer_ID,
        COUNT(DISTINCT Order_ID) AS order_count
    FROM sales
    GROUP BY Customer_ID
)
GROUP BY Customer_Type;
"""

print("=== NEW VS REPEAT CUSTOMERS ===")

for row in conn.execute(query):
    print(row[0], ":", row[1])

conn.close()