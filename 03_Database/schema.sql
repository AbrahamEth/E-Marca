CREATE DATABASE IF NOT EXISTS ecommerce_demo;
USE ecommerce_demo;

-- admins table
CREATE TABLE IF NOT EXISTS admins (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL
);

-- customers table
CREATE TABLE IF NOT EXISTS customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL
);

-- products table
CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add a demo admin and customer (passwords are plain for demo - change to hashed in production)
INSERT INTO admins (username, password_hash) VALUES ('Bianca', 'Maricar', 'Ethan', 'admin123') ON DUPLICATE KEY UPDATE username=username;
INSERT INTO customers (username, password_hash) VALUES ('','') ON DUPLICATE KEY UPDATE username=username;
