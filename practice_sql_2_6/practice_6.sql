-- creation view for order_status table
CREATE VIEW GENERAL_TOTAL_STATUSES AS
SELECT status_name, SUM(total)
FROM order_status JOIN orders
ON order_status_id = order_status_order_status_id
WHERE order_status_id in (1, 4, 5)
GROUP BY status_name;

SELECT * FROM GENERAL_TOTAL_STATUSES;

DROP VIEW GENERAL_TOTAL_STATUSES;


-- creation view for products table
CREATE VIEW WHOLESALE_PRODUCTS AS
SELECT product_title, price
FROM products
WHERE in_stock > 5 AND category_id = 4;

SELECT * FROM WHOLESALE_PRODUCTS
ORDER BY price;

DROP VIEW WHOLESALE_PRODUCTS;


-- creation view for products and categories table
CREATE OR REPLACE VIEW PRODUCTS_CATEGORIES AS
SELECT p.product_title, c.category_title, p.price
FROM products p
JOIN categories c
USING(category_id)
WHERE p.product_description LIKE '%1%';

SELECT * FROM PRODUCTS_CATEGORIES;

DROP VIEW PRODUCTS_CATEGORIES;


-- creation view for order table
CREATE OR REPLACE VIEW ORDERS_STATUSES AS
SELECT order_id, status_name, total, created_at
FROM orders JOIN order_status
ON order_status_order_status_id = order_status_id;

SELECT * FROM ORDERS_STATUSES;

DROP VIEW ORDERS_STATUSES;


-- Create materialized view
CREATE MATERIALIZED VIEW AVG_TOTAL AS
SELECT u.first_name ||' '|| u.last_name as user_name, o.created_at, os.status_name, AVG(o.total)
FROM users u JOIN carts c
ON u.user_id = c.users_user_id
JOIN orders o ON c.cart_id = o.carts_cart_id
JOIN order_status os ON o.order_status_order_status_id = os.order_status_id
WHERE created_at > '2020-01-01'
GROUP BY os.status_name, user_name, o.created_at;

SELECT * FROM AVG_TOTAL;

DROP MATERIALIZED VIEW AVG_TOTAL;
