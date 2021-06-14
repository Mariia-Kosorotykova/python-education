-- Add new column phone_number(int) to Users table
ALTER TABLE Users
ADD COLUMN phone_number INT;

-- Change data type in column phone_number from int to varchar
ALTER TABLE Users
ALTER COLUMN phone_number TYPE VARCHAR;