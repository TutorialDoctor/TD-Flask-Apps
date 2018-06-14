 drop table if exists account_holder;
    create table account_holder (
    id integer primary key autoincrement,
    email text,
    username text,
    phone text,
    password text
);

 drop table if exists contact;
    create table contact (
    id integer primary key autoincrement,
    name text,
    phone text,
    username text,
    email text
);