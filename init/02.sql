INSERT INTO example.product(name, price) VALUES ('bike', 150.35);
INSERT INTO example.product(name, price) VALUES ('tyre', 21.99);
INSERT INTO example.product(name, price) VALUES ('chain', 8.50);

INSERT INTO example.customer(name, address) VALUES ('tom', '1 main street');
INSERT INTO example.customer(name, address) VALUES ('dick', '2 side road');
INSERT INTO example.customer(name, address) VALUES ('harry', '3 alley');

INSERT INTO example.order(customer_id, product_id, quantity, cost)
SELECT c.customer_id, p.product_id, 1, 1 * p.price
FROM example.customer AS c, example.product AS p
WHERE c.name = 'tom' AND p.name = 'bike';

INSERT INTO example.order(customer_id, product_id, quantity, cost)
SELECT c.customer_id, p.product_id, 1, 1 * p.price
FROM example.customer AS c, example.product AS p
WHERE c.name = 'tom' AND p.name = 'chain';

INSERT INTO example.order(customer_id, product_id, quantity, cost)
SELECT c.customer_id, p.product_id, 1, 1 * p.price
FROM example.customer AS c, example.product AS p
WHERE c.name = 'dick' AND p.name = 'chain';

INSERT INTO example.order(customer_id, product_id, quantity, cost)
SELECT c.customer_id, p.product_id, 2, 2 * p.price
FROM example.customer AS c, example.product AS p
WHERE c.name = 'dick' AND p.name = 'tyre';

INSERT INTO example.order(customer_id, product_id, quantity, cost)
SELECT c.customer_id, p.product_id, 1, 1 * p.price
FROM example.customer AS c, example.product AS p
WHERE c.name = 'harry' AND p.name = 'bike';
