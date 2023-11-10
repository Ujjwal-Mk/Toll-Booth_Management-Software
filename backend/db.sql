-- Active: 1696681355003@@127.0.0.1@3306@toll_booth
DROP DATABASE IF EXISTS toll_booth;

CREATE DATABASE toll_booth;

USE toll_booth;

-- CREATE USER IF NOT EXISTS 'seproj'@'localhost' IDENTIFIED BY 'seproj'

-- GRANT ALL PRIVILEGES ON toll_booth.* TO 'seproj'@'localhost';

-- FLUSH PRIVILEGES;


CREATE TABLE usr_info(
    usrid INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(25),
    minit VARCHAR(5),
    l_name VARCHAR(25),
    username VARCHAR(25) UNIQUE,
    hashed_pass VARCHAR(255),
    auth_level ENUM('0','1') DEFAULT '1',
    CONSTRAINT uname_pass UNIQUE (username,hashed_pass)
);


CREATE TABLE usr_info1 (
    usrid INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(25),
    minit VARCHAR(5),
    l_name VARCHAR(25),
    username VARCHAR(25) UNIQUE,
    hashed_pass VARCHAR(255),
    auth_level ENUM('0','1') DEFAULT '1',
    address VARCHAR(255), -- New column
    date_of_joining DATE, -- New column
    CONSTRAINT uname_pass UNIQUE (username, hashed_pass)
);

-- Step 4: Reinsert the values into the new table
INSERT INTO usr_info1 (f_name, l_name, minit, username, hashed_pass, auth_level, address, date_of_joining) VALUES
('John', 'Doe', 'A', 'johndoe1', 'pass123', '1', '123 Main St', '2023-01-01'),
('Alice', 'Smith', 'B', 'alice.smith', 'abc456', '1', '456 Oak St', '2023-02-15'),
('Bob', 'Johnson', 'C', 'bobj', 'bob789', '0', '789 Pine St', '2023-03-10'),
('Emily', 'Davis', 'D', 'emily_d', 'emily123', '1', '987 Elm St', '2023-04-05'),
('Michael', 'Wilson', 'E', 'mike.w', 'mike456', '1', '654 Birch St', '2023-05-20'),
('Sarah', 'Brown', 'F', 'sarah_b', 'sarah789', '1', '321 Cedar St', '2023-06-15'),
('David', 'Lee', 'G', 'davidl', 'david123', '1', '876 Pine St', '2023-07-01'),
('Laura', 'Clark', 'H', 'laura.c', 'laura456', '1', '543 Maple St', '2023-08-12'),
('James', 'Anderson', 'I', 'james123', 'pass789', '0', '234 Oak St', '2023-09-28'),
('Sophia', 'Martinez', 'J', 'sophiam', 'sophia123', '1', '789 Elm St', '2023-10-03'),
('Admin','Admin','','admin','abc','0', '555 Admin St', '2023-11-09'),
('Peter','Parker','P','ppparker','1234567890','0', '123 Web St', '2023-12-25'),
('James','May','','jamesmay','captainslow','1', '999 Slow St', '2024-01-10'),
('Richard','Hammond','','richardham','hamster','1', '777 Hamster St', '2024-02-14');

CREATE TABLE cost_matrix
(   
    destination VARCHAR(50) PRIMARY KEY,
    Car INT,
    Bus INT,
    Truck INT
);

INSERT INTO cost_matrix (destination, `Car`, `Bus`, `Truck`)
VALUES
('Clover Leaf',60,150,105),
('Kanakpura Road',90,225,150),
('Bannerghatta Road',130,340,225),
('Hosur Road',180,485,325),
('Mysore Road',85,215,145),
('Magadi Road',140,370,250),
('Tumkur Road',185,490,330);

SELECT * FROM cost_matrix;

-- SELECT
--     username,
--     CONCAT(f_name, ' ', l_name) AS full_name,
--     address,
--     date_of_joining,
--     CASE
--         WHEN auth_level = '0' THEN 'Admin'
--         WHEN auth_level = '1' THEN 'Toll Operator'
--         ELSE 'Unknown Role'
--     END AS role
-- FROM usr_info1;

-- SELECT * FROM usr_info1;

-- SELECT * FROM usr_info;

