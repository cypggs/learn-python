import sqlite3
from athletelist import AthleteList

db_name = 'coachdata.sqlite'

"""Returns only the NAMES of all athletes in the database."""	
def get_names_from_store():
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	results = cursor.execute("""SELECT name FROM athletes""")
	response = [row[0] for row in results.fetchall()]
	connection.close()
	return(response)

"""Returns the NAMES and ID's of all athletes in the database."""	
def get_namesID_from_store():
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	results = cursor.execute("""SELECT name, id FROM athletes""")
	response = results.fetchall()
	connection.close()
	return(response)

"""Returns the data associted with a specific ID as a dictionary."""	
def get_athlete_from_id(athlete_id):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	results = cursor.execute("""SELECT name, dob FROM athletes WHERE id=?""", (athlete_id,))
	(name, dob) = results.fetchone()
	results = cursor.execute("""SELECT value FROM timing_data WHERE athlete_id=? ORDER BY value""", (athlete_id,))
	data = [row[0] for row in results.fetchall()]
	response = {'Name': name,
				'DOB': dob,
				'data': data,
				'top3': data[0:3]
				}
	connection.close()
	return(response)