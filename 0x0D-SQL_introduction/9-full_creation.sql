-- Create a table second_table in the database hbtn_0c_0
-- second_table description
--   id(INT)
--   VARCHAR(256)
--   score(INT)
-- The database name will be passed as an argument to the mysql command
-- If the table second_table already exists, script should not fail
-- No use of SELECT and SHOW

CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);

-- Inserting the given data into the table

INSERT INTO `second_table`(`id`, `name`, `score`)
VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);
