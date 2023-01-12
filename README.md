
# CRUD with Django

This project is an example of how to implement CRUD (Create, Read, Update, and Delete) functionality with Django. It's a great starting point for any project that requires basic CRUD functionality. The project includes examples of how to create, read, update, and delete records using Django's built-in views and models.


![Logo](https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You will need to have Python and Django installed on your machine.


### Run Locally

Clone the project

```bash
  git clone https://github.com/bhrayhaw/crud-with-django.git

```

Go to the project directory

```bash
  cd crud-with-django

```

Install the required packages

```bash
  pip install -r requirements.txt

```

Apply the migrations to create the necessary database tables

```bash
  python manage.py makemigrations
  python manage.py migrate


```




#### Running Tests

To run tests, run the following command

```bash
  python manage.py test

```

#### Start the server

```bash
  python manage.py runserver
```
## Usage/Examples

```python
home or 127.0.0.1:8000/ - to view the list of records

form/ - to create a new record

update_artist/<int:artist_id>/ - to update a specific artist details (replace 'id' with the actual id of the record)

update_album/<int:album_id>/ - to update a specific album details (replace 'id' with the actual id of the record)

delete_album/<int:album_id>/ - to delete a specific album (replace 'id' with the actual id of the record)

delete_artist/<int:artist_id>/ - to delete a specific artist (replace 'id' with the actual id of the record)
```


## Authors

- [@bhrayhaw](https://www.github.com/bhrayhaw)


## Acknowledgements

 - [Kazi Ariya](https://web.facebook.com/kaziariyanbd/?_rdc=1&_rdr)
 
## Tech Stack

**Client:** HTML, Bootstrap, Python, Django

**DataBase:** pgadmin

