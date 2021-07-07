CREATE OR REPLACE FUNCTION checking_period_of_renting()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
	IF NEW.period_of_renting > 60 THEN
		RAISE 'Max period of renting is 60 days';
    END IF;
        RETURN NEW.period_of_renting;
END;
$$;

CREATE TRIGGER check_period
AFTER INSERT OR UPDATE
ON renting
FOR EACH ROW
EXECUTE PROCEDURE checking_period_of_renting();

UPDATE renting
SET period_of_renting = 65
WHERE renting_id = 100;

CREATE OR REPLACE FUNCTION check_number_of_house()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
	IF new.house > 1000 THEN
    	RAISE 'Incorrect number of house. It must be less then 1000';
    END IF;
    	RETURN NEW.house;
END;
$$;

CREATE TRIGGER check_house
BEFORE INSERT OR UPDATE
ON info
FOR EACH ROW
EXECUTE PROCEDURE check_number_of_house();

INSERT INTO info
VALUES (6, 13, 'new_street', 1700, 'new_tel');
