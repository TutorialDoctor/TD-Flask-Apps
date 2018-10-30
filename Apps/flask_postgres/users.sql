CREATE TABLE users(
  id serial PRIMARY KEY,
  first_name VARCHAR (255) NOT NULL,
  last_name VARCHAR (255) NOT NULL,
  birth_date DATE,
  age INTEGER,
  gender VARCHAR (6),
  email VARCHAR (255) NOT NULL,
  website VARCHAR (255),
  status VARCHAR (255),
  created_at TIMESTAMP
  
)

-- DELETE FROM people3 name
/*MultiLine Comment*/

INSERT INTO users (first_name, last_name, birth_date, age, gender, email, website, status, created_at) VALUES
    ('Joe', 'Mars', '01/01/1999', 34, 'Male','joe@gmail.com','http://joe.com','deceased','2001-09-28 01:00:00'),
    ('Sarah', 'Hill', '01/01/2002', 19, 'Female','sarah@gmail.com','http://sarah.com','alive','2001-09-28 01:00:00');
    

/*SELECT first_name,last_name,birth_date FROM users
ORDER BY first_name desc*/