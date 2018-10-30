CREATE TABLE people3(
    id serial PRIMARY KEY,
    name VARCHAR (255)
)

-- DELETE FROM people3 name
/*MultiLine Comment*/

CREATE TABLE users(
  id serial PRIMARY KEY,
  first_name VARCHAR (255) NOT NULL,
  last_name VARCHAR (255) NOT NULL,
  birth_date DATE,
  age VARCHAR(16),
  gender VARCHAR (6),
  email VARCHAR (255) NOT NULL,
  website VARCHAR (255),
  alive VARCHAR(6),
  created_at TIMESTAMP
  
)

-- DELETE FROM people3 name
/*MultiLine Comment*/

INSERT INTO users (first_name, last_name, birth_date, age, gender, email, website, alive, created_at) VALUES
    ('Joe', 'Mars', '1900-01-01','34','Male','joe@gmail.com','http://joe.com',False,'2001-09-28 01:00:00'),
    ('Sarah', 'Hill', '1900-01-01','19','Female','sarah@gmail.com','http://sarah.com',True,'2001-09-28 01:00:00');
    

/*SELECT first_name,last_name,birth_date FROM users
ORDER BY first_name desc*/