CREATE TABLE users(id int, name VARCHAR(70), PRIMARY KEY (id));
CREATE INDEX name_idx ON users (name); 
COPY users (id, name) FROM '/docker-entrypoint-initdb.d/userdata.csv' WITH (FORMAT csv, HEADER true);