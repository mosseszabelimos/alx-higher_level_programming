-- Create a table with hbtn_0d with states
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `states`
(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	name VARCHAR(256)
);
