'''
# Write your MySQL query statement below
WITH customer_orders AS (
    SELECT customer_number, COUNT(*) AS order_count
    FROM Orders
    GROUP BY customer_number
)
SELECT customer_number
FROM customer_orders
WHERE order_count = (
    SELECT MAX(order_count)
    FROM customer_orders
);
'''
