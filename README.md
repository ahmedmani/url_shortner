# Flask URL Shortener

A simple and lightweight URL shortener built using Flask and Postgresql. It provides a REST api to create short URLs and automatically redirects users when they access the shortened links.


# Usage
Clone the repo using:
```git clone https://github.com/ahmedmani/url_shortner.git``` 

Make sure you're using Python 3.6+ and install the required libraries:
```python
pip install flask psycopg2
```
Set up PostgreSQL:
Import "database.sql" into postgres

In the script, set:
```python 
DB_PARAMS = {
    "database": "url_shortner",
    "host": "localhost",
    "user": "postgres",
    "password": "your_db_password",
    "port": "5432"
}
```
To run the app for testing:
```python
python -m flask --app url_shortner.py run
```

When deploying to production make sure to use gunicorn or nginx and setup proper tls certs
