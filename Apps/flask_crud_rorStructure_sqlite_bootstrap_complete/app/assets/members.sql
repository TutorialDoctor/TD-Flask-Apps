CREATE TABLE members
(
    id integer PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR (128) NOT NULL
)

INSERT INTO members
    (username, email, password)
VALUES
    ('myuser', 'myemail@domain.com', 'mypassword')