CREATE TABLE posts(
  id serial PRIMARY KEY,
  title VARCHAR (255) NOT NULL,
  content VARCHAR (255) NOT NULL,
  created_at TIMESTAMP 
)

-- DELETE FROM people3 name
/*MultiLine Comment*/

INSERT INTO posts (title,content,created_at) VALUES
    ('Post1', 'This is the first post','2001-09-28 01:00:00'),
    ('Post2', 'This is the 2nd post','2001-09-28 01:00:00');
    

/*SELECT first_name,last_name,birth_date FROM users
ORDER BY first_name desc*/