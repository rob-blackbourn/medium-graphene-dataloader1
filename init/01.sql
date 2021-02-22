CREATE DATABASE IF NOT EXISTS `example`;
GRANT ALL ON `example`.* TO 'rob'@'%';

CREATE TABLE example.product
(
	product_id  INT            NOT NULL AUTO_INCREMENT,
    name        VARCHAR(100)   NOT NULL,
    price       NUMERIC(10, 2) NOT NULL,

    PRIMARY KEY (product_id),
    UNIQUE (name)
);

CREATE TABLE example.customer
(
	customer_id INT            NOT NULL AUTO_INCREMENT,
    name        VARCHAR(100)   NOT NULL,
    address     VARCHAR(200)   NOT NULL,

    PRIMARY KEY (customer_id),
    UNIQUE (name)
);

CREATE TABLE example.order
(
	order_id    INT            NOT NULL AUTO_INCREMENT,
    customer_id INT            NOT NULL,
    product_id  INT            NOT NULL,
    quantity    INT            NOT NULL,
    cost        NUMERIC(10, 2) NOT NULL,

    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES example.customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES example.product(product_id)
);
