-- CREATE TABLE hinded (id INTEGER PRIMARY KEY AUTOINCREMENT, 
-- type INTEGER, 
-- subject INTEGER,
-- value TEXT NOT NULL, 
-- added_date TIMESTAMP, 
-- FOREIGN KEY (subject) REFERENCES subjects (id));

INSERT INTO hinded (type, value, subject)
VALUES (1, "2", 3);

-- CREATE TABLE subjects (id INTEGER PRIMARY KEY AUTOINCREMENT, 
-- subject_name TEXT NOT NULL);

-- INSERT INTO subjects (subject_name)
-- VALUES ("Matemaatika");