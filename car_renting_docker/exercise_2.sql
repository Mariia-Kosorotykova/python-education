-- Planning time: 1.486, Execution time: 159.8
EXPLAIN ANALYZE
SELECT customer_id, city_name, street, house FROM customers
JOIN info USING (address_id)
JOIN cities USING (city_id)
WHERE surname LIKE '%1%' AND city_name LIKE '%3%';

-- Planning time: 1.2, Execution time: 153.5
CREATE INDEX surname_idx ON customers(surname);

DROP INDEX surname_idx;

-- Planning time: 0.8, Execution time: 1160.40
EXPLAIN ANALYZE
SELECT brand, period_of_renting, surname FROM cars
JOIN renting USING (car_id)
JOIN customers USING (customer_id)
WHERE price BETWEEN 800000 AND 400000
	OR period_of_renting > 20;

-- Planning time: 0.4, Execution time: 1131.20
CREATE INDEX cars_idx ON cars(brand, price);

-- Planning time: 1.1, Execution time: 464.57
EXPLAIN ANALYZE
SELECT date_of_renting, model, price, id_branch, tel FROM renting
JOIN cars USING (car_id)
JOIN branches USING (id_branch)
JOIN info USING (address_id)
WHERE model LIKE '%7' AND tel LIKE '%1%'
ORDER BY date_of_renting;
