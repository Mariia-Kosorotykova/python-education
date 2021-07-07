-- view of customer's info
CREATE VIEW customer_info
AS
SELECT surname, name, city_name, street, house, tel
FROM customers
JOIN info USING (address_id)
JOIN cities USING (city_id);

SELECT * FROM customer_info;

DROP VIEW customer_info;

-- view of car's renting
CREATE VIEW car_renting_info
AS
SELECT brand, model, date_of_renting, period_of_renting
FROM cars
JOIN renting USING (car_id);

SELECT * FROM car_renting_info;

DROP VIEW car_renting_info;

-- materialized view of profirable rent
CREATE MATERIALIZED VIEW profitable_rent
AS
SELECT brand, model, name, surname, (price * period_of_renting) AS income
FROM cars
JOIN renting USING (car_id)
JOIN customers USING (customer_id)
WHERE price > 500000 AND period_of_renting > 5
ORDER BY income DESC;

SELECT * FROM profitable_rent;

DROP MATERIALIZED VIEW profitable_rent;
