-- creates atable and add multiple rows
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id,  name, score) VALUES
(1, 'john', 10),
(2, 'alex', 3),
(3, 'bob',14),
(4, 'george', 8);