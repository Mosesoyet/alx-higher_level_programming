-- Convert hbtn_0c_0 database to UTF8(utf8mb4_unicode, collate utf8mb4_unicode_ci)
-- Convert all the following to UTF8
--      hbtn_0c_0
--      first_table
--      name in first_table

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
