-- Exercise 1
-- Output all users
SELECT * FROM Users;

-- Output all products
SELECT * FROM products;

-- Output all order status
SELECT * FROM order_status;

-- Exercise 2
-- Display orders that have been successfully delivered and paid
SELECT * FROM orders
WHERE order_status_order_status_id = 4;

-- Exercise 3
-- Display products with a price of more than 80.00 and less than or equal to 150.00
SELECT * FROM products
WHERE PRICE > 80.00 AND PRICE <= 150.00;

SELECT * FROM products
WHERE PRICE BETWEEN 80.00 AND 150.00;

-- Display orders completed after 10/01/2020
SELECT * FROM orders
WHERE created_at > '10-01-2020'
ORDER BY created_at;

SELECT * FROM orders
WHERE created_at BETWEEN '10-01-2020' AND
(SELECT MAX(created_at) FROM orders);

-- Display orders received in the first half of 2020
SELECT * FROM orders
WHERE created_at BETWEEN '2020-01-01' AND '2020-06-30'
ORDER BY created_at;

SELECT * FROM orders
WHERE EXTRACT(MONTH FROM created_at) < 7
	AND EXTRACT(YEAR FROM created_at) = 2020;

-- Display products of the following categories Category 7, 11, 18
SELECT * FROM products
WHERE category_id in (7, 11, 18);


SELECT * FROM products JOIN categories
ON products.category_id = categories.category_id
WHERE categories.category_title IN ('Category 7', 'Category 11', 'Category 18');

-- Display unfinished orders as of 12/31/2020
SELECT * FROM orders
WHERE created_at <= '2020-12-31' AND order_status_order_status_id < 4;

SELECT * FROM orders
WHERE created_at <= '2020-12-31' AND order_status_order_status_id
IN (SELECT order_status_id FROM order_status
WHERE status_name != 'Finished' AND status_name != 'Canceled');

-- Display all baskets that were created, but the order was never placed
SELECT * FROM carts LEFT JOIN orders
ON cart_id = carts_cart_id
WHERE carts_cart_id IS NULL;

-- Exercise 4
-- Display the average of all completed trades
SELECT AVG(total) FROM orders
WHERE order_status_order_status_id =
	(SELECT order_status_id FROM order_status
	WHERE status_name = 'Finished');

-- Show the maximum transaction amount for the 3rd quarter of 2020
SELECT MAX(total) FROM orders
WHERE created_at BETWEEN '2020-07-01' AND '2020-09-30'
	AND order_status_order_status_id = 4;
