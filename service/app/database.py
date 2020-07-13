import psycopg2
import os
# import logger

def _create_table():
	_cursor.execute("select exists (select * from information_schema.tables where table_name=%s)",(table_name,))
	if _cursor.fetchone()[0] == False:
	  _cursor.execute("create table " + table_name + " ( timestamp timestamp, temperature real, moisture real , irrigation boolean )")
	  _connection.commit()
	  print("plant_properties table created")
	  # return 0

def insert_sensor_data(temperature,moisture,irrigation):
	sql_statement = "INSERT INTO " + table_name + " VALUES ( current_timestamp , " + str(temperature) + ", " + str(moisture) + ", " + str(irrigation) + ");"
	_cursor.execute(sql_statement)
	_connection.commit()
	#return 0
	
def select_all_sensor_data():
	_cursor.execute("SELECT * FROM " + table_name + ";")
	return _cursor.fetchall()

def close_connection():
  _cursor.close()
  _connection.close()


dbname = os.environ["DATABASE_NAME"]
user = os.environ["DATABASE_USER"]
password = os.environ["DATABASE_PASSWORD"]
host = os.environ["DATABASE_HOST"]
port = os.environ["DATABASE_PORT"]

_connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
)

_connection = psycopg2.connect(DATABASE_URL, sslmode="require")
_cursor = _connection.cursor()
table_name = 'plant_properties' #private
_create_table()

