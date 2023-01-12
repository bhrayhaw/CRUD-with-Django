# CRUD-with-Django
CRUD with Django
This project is an example of how to implement CRUD (Create, Read, Update, and Delete) functionality with Django.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You will need to have Python and Django installed on your machine.

Installing
Clone the repository to your local machine

git clone https://github.com/bhrayhaw/crud-with-django.git

Change into the project directory
cd crud-with-django

Install the required packages
pip install -r requirements.txt

Apply the migrations to create the necessary database tables
python manage.py makemigrations
python manage.py migrate

Running the tests
To run the tests, use the following command:
python manage.py test

Running the server
To start the development server, use the following command:
python manage.py runserver

Usage
Once the server is running, you can access the CRUD functionality by visiting the following URLs:
home or 127.0.0.1:8000/ - to view the list of records
form/ - to create a new record
update_artist/<int:artist_id>/ - to update a specific artist details (replace 'id' with the actual id of the record)
update_album/<int:album_id>/ - to update a specific album details (replace 'id' with the actual id of the record)
delete_album/<int:album_id>/ - to delete a specific album (replace 'id' with the actual id of the record)
delete_artist/<int:artist_id>/ - to delete a specific artist (replace 'id' with the actual id of the record)

Built With
Django - The web framework used
Authors
Elijah Apreko - Initial work - github.com/bhrayhaw

Acknowledgments
@Kazi Ariyan
[etc]
