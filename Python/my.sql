CREATE TABLE friends(id INTEGER, name TEXT, birthday DATE);

INSERT INTO friends(id, name, birthday) VALUES (1, "Ororo Munroe", May 30th, 1940);

SELECT * FROM friends;

INSERT INTO friends(id, name, birthday) VALUES (2, "Till Lindemman", January 4th, 1963);

INSERT INTO friends(id, name, birthday) VALUES (3, "Paul Landers", December 8th, 1964);

UPDATE friends SET name="Storm" WHERE id=1;

ALTER TABLE friends ADD COLUMN email TEXT;

UPDATE friends SET email ='storm@codeacademy.com' where id=1;

UPDATE friends SET email ='lind@gmail.com' where id=2;

UPDATE friends SET email ='landers@gmail.com' where id=3;

DELETE FROM friends where id=1;

SELECT * FROM friends; 


