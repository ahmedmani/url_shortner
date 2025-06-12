import psycopg2, traceback, re, random, string, json
from flask import Flask, request
from psycopg2.extras import DictCursor
from flask import abort, redirect
from datetime import datetime
from urllib.parse import urlparse


SECRET_KEY = ""

DB_PARAMS = {
    "database": "url_shortner",
    "host": "localhost",
    "user": "postgres",
    "password": "DB_PASSWORD",
    "port": "5432"
}


cursor = ""
def connect_to_db():
	global cursor
	try:
		connection = psycopg2.connect(database="url_shortner",
			host="localhost",
			user="postgres",
			password="123456",
			port="5432")
		connection.autocommit = True
	except Exception as ex:
		app.logger.error("error connecting to database")
		app.logger.error(traceback.format_exc())
	else:
		cursor = connection.cursor(cursor_factory=DictCursor)

app = Flask(__name__)
connect_to_db()


@app.route("/<short_url>/", methods=['GET'])
def process_get(short_url):
	try:
		if (len(short_url) == 0) or not short_url:
			return abort(code=400)
		if cursor:
			try:
				cursor.execute('SELECT * FROM url_mappings WHERE short_url = %s;', (short_url, ))
			except Exception as ex:
				app.logger.error(f"exception occured while searching database for short_url {short_url}")
				app.logger.error(traceback.format_exc())
			else:
				long_url = cursor.fetchall()
				if len(long_url) == 0:
					app.logger.error("short url not found in database")
					return abort(code=404)
					
				if (long_url[0].get("long_url") != None):
					destination = long_url[0].get("long_url")
					return redirect(destination, code=302)
		else:
			connect_to_db()
			return redirect(request.url)
	except:
		return abort(code=500)


def is_valid_url(url):
	regex = re.compile(
		r'^(?:http|ftp)s?://'
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
		r'localhost|'
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
		r'(?::\d+)?' 
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)
	return re.match(regex, url) is not None

@app.route("/urls/add_url/", methods=['POST'])
def add_long_url():
	headers = [i.lower() for i in request.headers.keys()]
	if request.headers.get("secret-key", "") != SECRET_KEY:
		app.logger.error('client not authorized')
		return abort(code=401)

	if (request.is_json) and ("long_url" in request.json.keys()) :
		long_url = request.json.get("long_url")
		if is_valid_url(long_url):
			try:
				for _ in range(2):
					short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
					try:
						cursor.execute('INSERT INTO url_mappings (short_url, long_url, created_at) VALUES (%s, %s, %s)', (short_url, long_url, datetime.now()))
					except psycopg2.errors.UniqueViolation:
						continue
					else:
						return json.dumps({"status": "created", "short_url": f"https://{request.host}/{short_url}"})

			except Exception as ex:
				app.logger.error("Exception occured while generating short url")
				app.logger.error(traceback.format_exc())
				return abort(code=500)
		else:
			app.logger.debug(f"{long_url} is not a valid url, returning 404")      
	return abort(code=400)

