import sqlite3

conn = sqlite3.connect("ecommerce.db")

print("=== AI DATA ASSISTANT ===")
print("Ask a question about your sales data.")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ").lower()

    if question == "exit":
        print("Assistant: Goodbye!")
        break

    if "revenue" in question:
        query = "SELECT ROUND(SUM(Total_Amount), 2) FROM sales;"
        result = conn.execute(query).fetchone()[0]
        print("Assistant: Total revenue is ₹", result)

    elif "orders" in question:
        query = "SELECT COUNT(DISTINCT Order_ID) FROM sales;"
        result = conn.execute(query).fetchone()[0]
        print("Assistant: Total orders are", result)

    elif "customers" in question:
        query = "SELECT COUNT(DISTINCT Customer_ID) FROM sales;"
        result = conn.execute(query).fetchone()[0]
        print("Assistant: Total customers are", result)

    elif "top product" in question:
        query = """
        SELECT Product, ROUND(SUM(Total_Amount), 2)
        FROM sales
        GROUP BY Product
        ORDER BY SUM(Total_Amount) DESC
        LIMIT 1;
        """
        result = conn.execute(query).fetchone()
        print("Assistant: Top product is", result[0],
              "with revenue ₹", result[1])

    else:
        print("Assistant: I don't understand that question yet.")

conn.close()