CREATE USER apiuser WITH PASSWORD 'YOUR_APIUSER_PASSWORD';
CREATE DATABASE spay;
\c spay;
CREATE TABLE users(id int, name VARCHAR(70), PRIMARY KEY (id));
CREATE INDEX name_idx ON users (name); 
GRANT SELECT, INSERT, UPDATE ON users TO apiuser;
\copy users (id, name) FROM '/dbinit/userdata.csv' WITH (FORMAT csv, HEADER true);