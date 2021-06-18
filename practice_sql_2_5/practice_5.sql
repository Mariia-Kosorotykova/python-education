-- Wrong optimization
-- PLanning 0.121, Execution 35.31, cost 31.75, actual 15.85
EXPLAIN(ANALYZE)
SELECT order_id
FROM orders
WHERE total > 500;

-- PLanning 0.46, Execution 60.05, cost 31.75, actual 37.89
CREATE INDEX idx_order_total ON orders(total);

DROP INDEX idx_order_total;

-- Example1
-- PLanning 1.134, Execution 464.889, cost 214.5, actual 464.7
EXPLAIN(ANALYZE)
SELECT first_name, last_name
FROM users
JOIN carts ON user_id = cart_id
LEFT JOIN orders ON carts.cart_id = orders.carts_cart_id
WHERE orders.carts_cart_id IS NULL
ORDER BY first_name, last_name
LIMIT 5;

-- PLanning 1.337, Execution 255.113, cost 214.5, actual 254.8
CREATE INDEX idx_users_name ON users(first_name, last_name);

DROP INDEX idx_users_name;

-- Example2
-- PLanning 0.114, Execution 0.638, cost 31.75, actual 0.566
EXPLAIN(ANALYZE)
SELECT * FROM orders
WHERE total = 500;

-- PLanning 0.278, Execution 0.178, cost 8.29, actual 0.045
CREATE INDEX idx_order_total ON orders(total);

-- PLanning 0.138, Execution 0.138, cost 8.29, actual 0.052
SET enable_seqscan TO OFF;


DROP INDEX idx_order_total;
SET enable_seqscan TO ON;

-- Example3
-- PLanning 0.33, Execution 288.941, cost 195.71, actual 288.616
EXPLAIN(ANALYZE)
SELECT category_title, COUNT(*)
FROM categories c
JOIN products p ON p.category_id = c.category_id
GROUP BY category_title
ORDER BY COUNT(*) DESC;

-- PLanning 0.476, Execution 267.92, cost 179.86, actual 267.120
CREATE INDEX idx_categories_category_title ON categories(category_title);

DROP INDEX idx_categories_category_title;
