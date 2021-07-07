-- Creation of Cities table
CREATE TABLE IF NOT EXISTS Cities (
    city_id serial PRIMARY KEY,
    city_name VARCHAR(30)
);

-- Creation Info table
CREATE TABLE IF NOT EXISTS Info (
    address_id serial PRIMARY KEY,
    city_id INT NOT NULL,
    street VARCHAR(50),
    house INT,
    tel VARCHAR(20),
    FOREIGN KEY (city_id)
        REFERENCES Cities(city_id)
);

-- Creation Customers table
CREATE TABLE IF NOT EXISTS Customers (
    customer_id serial PRIMARY KEY,
    address_id INT,
    surname VARCHAR(50),
    name VARCHAR(50),
    FOREIGN KEY (address_id)
            REFERENCES Info(address_id)
);

-- Creation Branches table
CREATE TABLE IF NOT EXISTS Branches (
    id_branch serial PRIMARY KEY,
    address_id INT,
    FOREIGN KEY (address_id)
        REFERENCES Info(address_id)
);

-- Creation of Cars table
CREATE TABLE IF NOT EXISTS Cars (
    car_id serial PRIMARY KEY,
    id_branch INT NOT NULL,
    brand VARCHAR(40) NOT NULL,
    model VARCHAR(15) NOT NULL,
    price INT NOT NULL,
    FOREIGN KEY (id_branch)
            REFERENCES Branches(id_branch)
);

-- Creation Renting table
CREATE TABLE IF NOT EXISTS Renting (
    renting_id serial PRIMARY KEY,
    customer_id INT,
    car_id INT NOT NULL,
    date_of_renting DATE NOT NULL,
    period_of_renting INT NOT NULL,
    FOREIGN KEY (customer_id)
            REFERENCES Customers(customer_id),
    FOREIGN KEY (car_id)
            REFERENCES Cars(car_id)
);

-- Insertion of 500 cities
CREATE SEQUENCE seq_cities
    INCREMENT 1
    START 1;

CREATE OR REPLACE PROCEDURE insert_cities()
LANGUAGE plpgsql
AS $$
DECLARE
    exit_loop INT := 500;
    current_row INT := 1;
BEGIN
    WHILE current_row <= exit_loop
        LOOP
            current_row = current_row + 1;
            INSERT INTO Cities
            VALUES (nextval('seq_cities'),
                    'City-' || currval('seq_cities'));
 	    END LOOP;
END;
$$;

CALL insert_cities();

-- Insertion of 1500 addresses
CREATE SEQUENCE seq_addresses
    INCREMENT 1
    START 1;

CREATE OR REPLACE PROCEDURE insert_adress()
LANGUAGE plpgsql
AS $$
DECLARE
    city_id INT;
    house INT;
    exit_loop INT := 1500;
    current_row INT := 1;
BEGIN
	WHILE current_row <= exit_loop
	LOOP
	    city_id := floor(random() * (500 - 1 + 1)) + 1;
	    house := floor(random() * (50 - 1 + 1)) + 1;
		current_row = current_row + 1;
		INSERT INTO Info
			VALUES (nextval('seq_addresses'),
			        city_id,
					'Street-' || currval('seq_addresses'),
					house,
					'Telephone-' || currval('seq_addresses'));
	END LOOP;
END;
$$;

CALL insert_adress();

-- Insertion of 2987 customers
CREATE SEQUENCE seq_customers
    INCREMENT 1
    START 1;

CREATE OR REPLACE PROCEDURE insert_customers()
LANGUAGE plpgsql
AS $$
DECLARE
    address_id INT;
    house INT;
    exit_loop INT := 2987;
    current_row INT := 1;
BEGIN
	WHILE current_row <= exit_loop
	LOOP
	    address_id := floor(random() * (1500 - 1 + 1)) + 1;
	    house := floor(random() * (50 - 1 + 1)) + 1;
		current_row = current_row + 1;
		INSERT INTO Customers
			VALUES (nextval('seq_customers'),
			        address_id,
					'Surname-' || currval('seq_customers'),
					'Name-' || currval('seq_customers'));
	END LOOP;
END;
$$;

CALL insert_customers();

-- Insertion of 234 branches
CREATE SEQUENCE seq_branches
    INCREMENT 1
    START 1;

CREATE OR REPLACE PROCEDURE insert_branches()
LANGUAGE plpgsql
AS $$
DECLARE
    address_id INT;
    exit_loop INT := 234;
    current_row INT := 1;
BEGIN
	WHILE current_row <= exit_loop
	LOOP
	    address_id := floor(random() * (1500 - 1 + 1)) + 1;
		current_row = current_row + 1;
		INSERT INTO Branches
			VALUES (nextval('seq_branches'),
			        address_id);
	END LOOP;
END;
$$;

CALL insert_branches();

-- Insertion of 5432 cars
CREATE SEQUENCE seq_cars
    INCREMENT 1
    START 1;

CREATE OR REPLACE PROCEDURE insert_cars()
LANGUAGE plpgsql
AS $$
DECLARE
    id_branch INT;
    price INT;
    exit_loop INT := 5432;
    current_row INT := 1;
BEGIN
	WHILE current_row <= exit_loop
	LOOP
	    id_branch := floor(random() * (234 - 1 + 1)) + 1;
	    price := floor(random() * (1000000 - 1 + 1)) + 1;
		current_row = current_row + 1;
		INSERT INTO Cars
			VALUES (nextval('seq_cars'),
			        id_branch,
					'Brand-' || currval('seq_cars'),
					'Model-' || currval('seq_cars'),
					price);
	END LOOP;
END;
$$;

CALL insert_cars();

-- Insertion of 9876 rent
CREATE SEQUENCE seq_rent
    INCREMENT 1
    START 1;

CREATE OR REPLACE PROCEDURE insert_rent()
LANGUAGE plpgsql
AS $$
DECLARE
    customer_id INT;
    car_id INT;
    period_of_renting INT;
    exit_loop INT := 9876;
    current_row INT := 1;
BEGIN
	WHILE current_row <= exit_loop
	LOOP
	    customer_id := floor(random() * (2987 - 1 + 1)) + 1;
	    car_id := floor(random() * (5432 - 1 + 1)) + 1;
	    period_of_renting := floor(random() * (60 - 1 + 1)) + 1;
		current_row = current_row + 1;
		INSERT INTO Renting
			VALUES (nextval('seq_rent'),
			        customer_id,
			        car_id,
					timestamp '2010-01-01 07:00:00' + random() *
					    (timestamp '2021-07-07 07:00:00' - timestamp '2010-01-01 07:00:00'),
					period_of_renting);
	END LOOP;
END;
$$;

CALL insert_rent();
