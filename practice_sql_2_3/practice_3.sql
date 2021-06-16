-- Exercise 1
-- Create table Potential customer
CREATE TABLE IF NOT EXISTS Potential_customer (
    id serial PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(255),
    surname VARCHAR(255),
    second_name VARCHAR(255),
    city VARCHAR(255)
);

-- Insert data
INSERT INTO Potential_customer
VALUES (1, 'test1@gmail.com', 'name_1', 'surname_1', 'second_name_1', 'test_city_1'),
    (2, 'test2@gmail.com', 'name_2', 'surname_2', 'second_name_2', 'test_city_2'),
    (3, 'test3@gmail.com', 'name_3', 'surname_3', 'second_name_3', 'test_city_3'),
    (4, 'test4@gmail.com', 'name_4', 'surname_4', 'second_name_4', 'test_city_4'),
    (5, 'test5@gmail.com', 'name_5', 'surname_5', 'second_name_5', 'test_city_5'),
    (6, 'test6@gmail.com', 'name_6', 'surname_6', 'second_name_6', 'test_city_6'),
    (7, 'test7@gmail.com', 'name_7', 'surname_7', 'second_name_7', 'test_city_7'),
    (8, 'test8@gmail.com', 'name_8', 'surname_8', 'second_name_8', 'test_city_8'),
    (9, 'test9@gmail.com', 'name_9', 'surname_9', 'second_name_9', 'test_city_9'),
    (10, 'test10@gmail.com', 'name_10', 'surname_10', 'second_name_10', 'test_city_10'),
    (11, 'test11@gmail.com', 'name_11', 'surname_11', 'second_name_11', 'test_city_11'),
    (12, 'test12@gmail.com', 'name_12', 'surname_12', 'second_name_12', 'test_city_12'),
    (13, 'test13@gmail.com', 'name_13', 'surname_13', 'second_name_13', 'test_city_13'),
    (14, 'test14@gmail.com', 'name_14', 'surname_14', 'second_name_14', 'test_city_14');

-- Print names and email of potential and existing users from city 17
SELECT name, email
FROM Potential_customer
WHERE city = 'city 17'
UNION
SELECT first_name, email
FROM users
WHERE city = 'city 17';

-- Exercise 2
-- Display the names and email addresses of all users sorted by city and name
SELECT first_name, email
FROM users
ORDER BY city, first_name;

-- Exercise 3
-- Display the name of a group of goods, the total quantity for a group of goods in descending order of quantity
SELECT category_title, COUNT(*)
FROM categories c
JOIN products p ON p.category_id = c.category_id
GROUP BY category_title
ORDER BY COUNT(*) DESC;

-- Exercise 4
-- Display products that have never been added to the basket
SELECT product_title FROM products
LEFT JOIN cart_product
ON product_id = products_product_id
WHERE products_product_id IS NULL;

---- Display all products that have not been included in 1 order
SELECT product_id, product_title
FROM products
LEFT JOIN cart_product ON product_id = products_product_id
LEFT JOIN carts ON cart_id = carts_cart_id
LEFT JOIN orders ON cart_id = orders.carts_cart_id
WHERE orders.carts_cart_id IS NULL;

-- Display the top 10 most frequently added products to shopping carts
SELECT product_title, COUNT(products_product_id)
FROM products
JOIN cart_product ON product_id = products_product_id
GROUP BY product_title
ORDER BY COUNT(products_product_id) DESC
LIMIT 10;

-- Display the top 10 products that not only added to baskets, but also placed orders most often
SELECT product_title, COUNT(orders.carts_cart_id)
FROM products
JOIN cart_product ON product_id = products_product_id
JOIN carts ON cart_product.carts_cart_id = cart_id
JOIN orders ON cart_id = orders.carts_cart_id
GROUP BY product_title
ORDER BY COUNT(order_id) DESC LIMIT 10;

-- Display the top 5 users who spent the most money (total in the order)
SELECT user_id, first_name, SUM(orders.total)
FROM users
JOIN carts ON user_id = cart_id
JOIN orders ON cart_id = cart_id
JOIN order_status ON order_status_id = order_status_id
WHERE order_status_id = 4
GROUP BY user_id
ORDER BY SUM(orders.total) DESC LIMIT 5;

-- Display the top 5 users who made the most orders (number of orders)
SELECT user_id, first_name, COUNT(order_id) AS total
FROM users
JOIN carts ON user_id = users_user_id
JOIN orders ON carts_cart_id = cart_id
GROUP BY user_id
ORDER BY total DESC LIMIT 5;

-- Display the top 5 users who have created carts but never made orders
SELECT first_name, last_name
FROM users
JOIN carts ON user_id = cart_id
LEFT JOIN orders ON carts.cart_id = orders.carts_cart_id
WHERE orders.carts_cart_id IS NULL
ORDER BY first_name, last_name
LIMIT 5;
