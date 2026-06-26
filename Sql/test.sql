-- testing the tables created in the schema.sql file 
SELECT name
FROM sqlite_master
WHERE type='table';
