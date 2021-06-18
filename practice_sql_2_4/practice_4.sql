-- Apply transactions for potential customer table
-- Insert operation
BEGIN;
	INSERT INTO potential_customer
	VALUES  (15, 'test15@gmail.com', 'name_15', 'surname_15', 'second_name_15', 'test_city_15'),
			(16, 'test16@gmail.com', 'name_16', 'surname_16', 'second_name_16', 'test_city_16'),
			(17, 'test17@gmail.com', 'name_17', 'surname_17', 'second_name_17', 'test_city_17');
COMMIT;

-- Delete operation
BEGIN;
	DELETE FROM potential_customer WHERE id = 15;
	SAVEPOINT delete_by_id;
	DELETE FROM potential_customer WHERE email LIKE '%16%';
	SAVEPOINT delete_by_email;
	DELETE FROM potential_customer WHERE city = 'test_city_17';
ROLLBACK TO delete_by_email;

ROLLBACK TO delete_by_id;

COMMIT;

-- Update operation
BEGIN;
	UPDATE potential_customer
	SET surname = 'Petrov'
	WHERE id = 17;
	SAVEPOINT update_by_id;

	UPDATE potential_customer
	SET name = 'Nikolay'
	WHERE surname = 'P%';

ROLLBACK TO update_by_id;

COMMIT;

-- Apply transactions for order status table
BEGIN;
	INSERT INTO order_status
	VALUES (6, 'New');
	UPDATE order_status
	SET status_name = 'Mistaken';
	DELETE FROM order_status
	WHERE order_status_id = 6;

ROLLBACK;

-- Apply transactions for order status table
BEGIN;
	INSERT INTO categories
	VALUES (77, 'Category 77', 'Category 56 description'),
		(100, 'Category 99', 'Category 99 description');

	SAVEPOINT add_category;

	DELETE FROM categories
	WHERE category_id = 77;

	SAVEPOINT delete_category;

	UPDATE categories
	SET category_title = 'New_category'
	WHERE category_description LIKE '%99%';

ROLLBACK TO delete_category;

ROLLBACK TO add_category;

ROLLBACK;
