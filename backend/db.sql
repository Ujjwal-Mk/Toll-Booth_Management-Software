-- Active: 1696681355003@@127.0.0.1@3306@toll_booth
DROP DATABASE IF EXISTS toll_booth;

CREATE DATABASE toll_booth;

USE toll_booth;

-- CREATE USER IF NOT EXISTS 'seproj'@'localhost' IDENTIFIED BY 'seproj'

-- GRANT ALL PRIVILEGES ON toll_booth.* TO 'seproj'@'localhost';

-- FLUSH PRIVILEGES;


CREATE TABLE employee_info (
    usrid INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(25),
    minit VARCHAR(5),
    l_name VARCHAR(25),
    -- username VARCHAR(25) UNIQUE,
    -- hashed_pass VARCHAR(255),
    auth_level ENUM('admin','operator', 'support') DEFAULT 'support',
    address VARCHAR(255), -- New column
    date_of_joining DATE -- New column
);




-- Step 4: Reinsert the values into the new table
INSERT INTO employee_info(f_name, l_name, minit, auth_level, address, date_of_joining) VALUES
('John', 'Doe', 'A', '1', '123 Main St', '2023-01-01'),
('Alice', 'Smith', 'B', '1', '456 Oak St', '2023-02-15'),
('Bob', 'Johnson', 'C', '0', '789 Pine St', '2023-03-10'),
('Emily', 'Davis', 'D', '1', '987 Elm St', '2023-04-05'),
('Michael', 'Wilson', 'E', '1', '654 Birch St', '2023-05-20'),
('Sarah', 'Brown', 'F', '1', '321 Cedar St', '2023-06-15'),
('David', 'Lee', 'G', '1', '876 Pine St', '2023-07-01'),
('Laura', 'Clark', 'H', '1', '543 Maple St', '2023-08-12'),
('James', 'Anderson', 'I', '0', '234 Oak St', '2023-09-28'),
('Sophia', 'Martinez', 'J', '1', '789 Elm St', '2023-10-03'),
('Admin','Admin','','0', '555 Admin St', '2023-11-09'),
('Peter','Parker','P','0', '123 Web St', '2023-12-25'),
('James','May','', '1', '999 Slow St', '2024-01-10'),
('Richard','Hammond','','1', '777 Hamster St', '2024-02-14');

CREATE TABLE login_user_info(
    usrid INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(25),
    minit VARCHAR(5),
    l_name VARCHAR(25),
    username VARCHAR(25) UNIQUE,
    hashed_pass VARCHAR(255),
    auth_level ENUM('admin','operator'),
    CONSTRAINT uname_pass UNIQUE (username,hashed_pass),
    CONSTRAINT usrid_fk FOREIGN KEY (usrid) REFERENCES employee_info(usrid)
);

INSERT INTO login_user_info(f_name, l_name, minit, username, hashed_pass, auth_level) VALUES
('John', 'Doe', 'A', 'johndoe1', 'pass123', '1'),
('Alice', 'Smith', 'B', 'alice.smith', 'abc456', '1'),
('Bob', 'Johnson', 'C', 'bobj', 'bob789', '0');

CREATE TABLE cost_matrix
(   
    -- destination VARCHAR(50) PRIMARY KEY,
    -- Car INT,
    -- Bus INT,
    -- Truck INT
    vehicle_type ENUM('Car', 'Mini Truck', "Bus or Medium Truck", "Large Truck") DEFAULT 'Car',
    single_trip int,
    double_trip int
);

INSERT INTO cost_matrix (vehicle_type, single_trip, double_trip) VALUES
("Car", 53, 79),
("Mini Truck", 91, 138),
("Bus or Medium Truck", 185, 227),
("Large Truck", 297, 445);

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

