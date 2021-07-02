-- 1. Creation of the function
-- that sets shipping_total = 0 in the order table if the user's city is x.
-- Using IF clause.
CREATE OR REPLACE FUNCTION set_shipping_total(city_name VARCHAR)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
	IF EXISTS(SELECT 1 FROM users
			  WHERE city = city_name
	) THEN
		UPDATE orders SET shipping_total = 0
		WHERE order_id in (SELECT order_id FROM orders o
						   JOIN carts c ON o.carts_cart_id = c.cart_id
						   JOIN users u ON c.users_user_id = u.user_id
						   WHERE city = city_name);
	ELSE
		RAISE '% not found', city_name;
	END IF;
END;
$$;

BEGIN;
SELECT set_shipping_total('city 100');

SELECT u.city, o.shipping_total
FROM users u
JOIN carts c ON u.user_id = c.users_user_id
JOIN orders o ON c.cart_id = o.carts_cart_id
WHERE city = 'city 100';

ROLLBACK;

-- 2. Stored procedure with loop, transactions and if clause
-- DOESN'T WORK!
CREATE OR REPLACE PROCEDURE decrease_in_price(number_of_category integer, percent integer)
LANGUAGE plpgsql
AS $$
DECLARE
	price_product record;
BEGIN
	IF EXISTS(SELECT 1 FROM products
			WHERE products.category_id = number_of_category
	) THEN
		FOR price_product IN (SELECT price, product_id, in_stock
							 FROM products)
			LOOP
				UPDATE products
				SET price = (price * percent/100) + price
				WHERE product_id = number_of_category;
				IF price_product.in_stock < 10 THEN
					COMMIT;
				ELSE
					ROLLBACK;
				END IF;
			END LOOP;
	ELSE
		RAISE '% not found', number_of_category;
	END IF;
END;
$$;

CALL decrease_in_price(4, 50);

-- 2. Stored procedure with loop, transactions and if clause
-- DOESN'T WORK!
CREATE OR REPLACE PROCEDURE decrease_in_price(number_of_product integer, deducted_amount integer)
LANGUAGE plpgsql
AS $$
DECLARE
    remainig_amount integer;
BEGIN
    UPDATE products
	SET in_stock = in_stock - deducted_amount
	WHERE product_id = number_of_product
    RETURNING in_stock
    INTO remainig_amount;
    IF remainig_amount >= 0 THEN
        COMMIT;
    ELSE
        ROLLBACK;
        RAISE EXCEPTION 'Not enough products in stock';
    END IF;
END;
$$;

CALL decrease_in_price(4, 50);

-- 3.Comparing the price of each product with the AVG price of the products in the product category.
-- Using window function.
SELECT
	category_title,
	product_title,
	price,
	AVG(price) OVER (
		PARTITION BY category_title
	)
FROM products p JOIN categories c
ON p.product_id = c.category_id

-- 4. Triggers and handlers to them.
CREATE OR REPLACE FUNCTION check_in_stock()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
	IF NEW.in_stock <= 0 THEN
		RAISE 'Count of products must be more then 0';
	END IF;
	RETURN NEW;
END;
$$;

CREATE TRIGGER check_products_in_stock
	BEFORE INSERT OR UPDATE
	ON products
	FOR EACH ROW
	EXECUTE PROCEDURE check_in_stock();

BEGIN;

UPDATE products
SET in_stock = -4
WHERE product_id = 50;

UPDATE products
SET in_stock = 4
WHERE product_id = 50;

DROP TRIGGER check_products_in_stock ON products;

ROLLBACK;

-- 4. Triggers and handlers to them.
CREATE OR REPLACE FUNCTION updating_order_time()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
	UPDATE orders
	SET updated_at = now()
	WHERE order_id = NEW.order_id;
	RETURN NEW;
END;
$$;

CREATE TRIGGER change_updating_order_time
	AFTER UPDATE OF total
	ON orders
	FOR EACH ROW
	EXECUTE PROCEDURE updating_order_time();

BEGIN;
UPDATE orders
SET total = 4
WHERE order_id = 50;

DROP TRIGGER change_updating_order_time ON orders;
