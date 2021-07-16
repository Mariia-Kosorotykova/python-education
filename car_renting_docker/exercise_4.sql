CREATE OR REPLACE FUNCTION displays_customers(amount_customers INT)
RETURNS TABLE (
		customer_id INT,
		surname VARCHAR,
		name VARCHAR,
		city_name VARCHAR,
		street VARCHAR,
		house INT,
		tel VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
 	FOR i IN 1..amount_customers + 1
	LOOP
 	RETURN QUERY
 		SELECT c.customer_id, c.surname, c.name, cts.city_name, inf.street, inf.house, inf.tel
  		FROM customers c
  		JOIN info inf USING (address_id)
 		JOIN cities cts USING (city_id)
 		WHERE c.customer_id = i;
	END LOOP;
END;
$$;

SELECT * FROM displays_customers(50);

DROP FUNCTION IF EXISTS displays_customers;

CREATE OR REPLACE FUNCTION clients_by_period_of_renting(rent_period INT)
RETURNS text
LANGUAGE plpgsql
AS $$
DECLARE
	cur_client CURSOR(rent_period INT)
		FOR SELECT date_of_renting, name, surname
		FROM renting
		JOIN customers USING (customer_id)
		WHERE period_of_renting = rent_period;
	client_info text default '';
	rec record;
BEGIN
   OPEN cur_client(rent_period);
   LOOP
      FETCH cur_client into rec;
      EXIT WHEN NOT FOUND;
	  client_info := UPPER(rec.name) || UPPER(rec.surname) || 'Date of renting: ' || rec.date_of_renting;
   END LOOP;
   CLOSE cur_client;
   RETURN client_info;
END; $$;

SELECT clients_by_period_of_renting(15);

DROP FUNCTION IF EXISTS clients_by_period_of_renting;
