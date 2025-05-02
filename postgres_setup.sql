-- Create the 'Ecoomerce_db' database
CREATE DATABASE Ecommerce_db;

-- Swictch to the 'Ecomerce_db' Database
USE Ecommerce_db;

-- Create the 'ecommerce_events' table

CREATE TABLE ecommerce_events (
    event_id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    product_name varchar(255),
	product_id UUID NOT null,
    event_type VARCHAR(50) NOT NULL,
    event_time TIMESTAMP NOT NULL
);


select *
from ecommerce_events;


    