-- Creation of Users table
CREATE TABLE IF NOT EXISTS Users (
    user_id serial PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    is_staff int2,
    country VARCHAR(255),
    city VARCHAR(255),
    address text
);

-- Creation Categories table
CREATE TABLE IF NOT EXISTS Categories (
    category_id serial PRIMARY KEY,
    category_title VARCHAR(255) UNIQUE,
    category_description text
);

-- Creation Products table
CREATE TABLE IF NOT EXISTS Products (
    product_id serial PRIMARY KEY,
    product_title VARCHAR(255) UNIQUE,
    product_description text,
    in_stock INT,
    price FLOAT,
    slug VARCHAR(45),
    category_id INT,
    FOREIGN KEY (category_id)
            REFERENCES Categories(category_id)
);

-- Creation of Carts table
CREATE TABLE IF NOT EXISTS Carts (
    cart_id serial PRIMARY KEY,
    Users_user_id INT,
    subtotal DECIMAL,
    total DECIMAL,
    timestamp TIMESTAMP(2),
    FOREIGN KEY (Users_user_id)
            REFERENCES Users(user_id)
);

-- Creation Cart product table
CREATE TABLE IF NOT EXISTS Cart_product (
    carts_cart_id INT,
    products_product_id INT,
    FOREIGN KEY (carts_cart_id)
            REFERENCES Carts(cart_id),
    FOREIGN KEY (products_product_id)
            REFERENCES Products(product_id)
);

-- Creation of Order status table
CREATE TABLE IF NOT EXISTS Order_status (
    order_status_id serial PRIMARY KEY,
    status_name VARCHAR(255)
);

-- Creation of Orders table
CREATE TABLE IF NOT EXISTS Orders (
    order_id serial PRIMARY KEY,
    Carts_cart_id INT,
    Order_status_order_status_id INT,
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2),
    FOREIGN KEY (Carts_cart_id)
            REFERENCES Carts(cart_id),
    FOREIGN KEY (Order_status_order_status_id)
            REFERENCES Order_status(order_status_id)
);
