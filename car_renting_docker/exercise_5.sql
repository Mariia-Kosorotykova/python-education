CREATE OR REPLACE PROCEDURE modify_price(id_selected_car INT)
LANGUAGE plpgsql
AS $$
DECLARE
    update_price INT;
BEGIN
	SAVEPOINT sp;
	UPDATE cars
	SET price = price - price * 0.2
	WHERE car_id = id_selected_car
	RETURNING price INTO update_price;
  	IF update_price > 100000 THEN
    	COMMIT;
    ELSE
    	ROLLBACK TO SAVEPOINT sp;
   	END IF;
END;
$$;

CALL modify_price(6);

DROP PROCEDURE modify_price;

CREATE OR REPLACE PROCEDURE update_cars(selected_car_id INT)
LANGUAGE plpgsql
AS $$
DECLARE
    changed_car_id INT;
BEGIN
    UPDATE cars
    SET id_branch = 20
    WHERE car_id = selected_car_id
	RETURNING car_id
    INTO changed_car_id;
	INSERT INTO cars
	VALUES (5433, 20, 'Brand-1', 'Model-1', 10000);
    IF selected_car_id >= 2000 THEN
		COMMIT;
        DELETE FROM cars
		WHERE car_id = 5000;
		COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END;$$;

CALL update_cars(2002);
DROP PROCEDURE update_cars;
