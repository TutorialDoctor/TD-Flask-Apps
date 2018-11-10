This is a flask Crud app with a folder structure similar to Ruby on Rails using an sqlite database with a native bootstrap css library (you don't need to be connected to the internet to see the styling).

I created this application as the basis for a full social media app with flask to test my skills and understanding of webapp development. I also created this app to be a good transitional project to Ruby on Rails.

This project demonstrates a good understanding of:

- Python
- SQL database design
- One-To-Many relationship
- The MVC architecture
- UI Design
- Web App Development
- HTML & CSS
- Gitflow


![](https://github.com/TutorialDoctor/TD-Flask-Apps/blob/master/Apps/flask_crud_rorStructure_sqlite_bootstrap/app/assets/screen.png)

This app was built from scratch to mimic the Ruby on Rails framework. There was some difficulty with imports initially.

This is derived from the `flask_postgres_advanced` project and transformed to use a sqlite database rather than a postgresql database (some queries were modifed).

`pip install flask-sqlalchemy`

**Note:** This is a work in progress. Currently you can submit the users and posts without entering information to get auto-generated data. There are still some issues with the manual data entry currently.


## To Create your own Models, Views and Controllers:

Copy one of the existing models and its view and controller counterparts and modify to your needs.

Controllers can be named as Plural and lowercase and Models can be named as singular uppercase. However, you can choose your own naming convention. There is no restriction on how they can be named.

You must run `db.create_all()` once to create the database from the model files. I just run the server `python3 main.py` and then comment out the `db.create_all()` line and restart the server. You can also do this from the terminal by importing `db` from the `setup.py` file and running `db.create_all()`. I left commented code for the postgreSQL setup, but the `.sql` files would need to be adjusted for the rest of the app to work.

New controllers and models should be imported at the bottom of the `setup.py` file.

## Summary of the Process

1. Copy and edit corresponding model, controller and view files for any new objects.
2. Create the database with `db.create_all()`
3. Import the models and controllers at the bottom of the `setup.py` file.

## Included Items

- In the `\assets` directory I've included the .sql files for the initial data so that you can see how the tables and their data types.
- I've included the full css for bootstrap so that you don't have to be online to view styling.
- I've included a backup file of the single-file flask app in the `\temp` directory
- You can add additional bootstrap components to the components directory and include them in several files.
- I've included notes below on how I was able to import files into other files

<pre>

- If the import module in the same dir, use e.g: from . import core
- If the import module in the top dir, use e.g: from .. import core
- If the import module in the other subdir, use e.g: from ..other import core</pre>

## Other Software Used

I use [DB Browser](https://sqlitebrowser.org) for the mac to manage the sqlite database directly 

https://www.techiediaries.com/sqlite-create-table-foreign-key-relationships/


