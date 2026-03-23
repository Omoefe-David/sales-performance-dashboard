-- Query 1: Total Revenue by Sales Rep
SELECT 
  sales_rep,
  COUNT(order_id) AS total_orders,
  SUM(quantity * unit_price) AS total_revenue
FROM sales_data2
WHERE status = 'Completed'
GROUP BY sales_rep
ORDER BY total_revenue DESC;

-- Query 2: Revenue by Region
SELECT 
  region,
  SUM(quantity * unit_price) AS total_revenue,
  COUNT(order_id) AS total_orders
FROM sales_data2
WHERE status = 'Completed'
GROUP BY region
ORDER BY total_revenue DESC;

-- Query 3: Best Selling Product
SELECT 
  product,
  SUM(quantity) AS units_sold,
  SUM(quantity * unit_price) AS total_revenue
FROM sales_data2
WHERE status = 'Completed'
GROUP BY product
ORDER BY total_revenue DESC;

-- Query 4: Cancellation Rate
SELECT 
  status,
  COUNT(*) AS total,
  ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM sales_data2), 1) AS percentage
FROM sales_data2
GROUP BY status;