import sqlite3

connection = sqlite3.connect('coachdata.sqlite')	# establish a connection to a database; this disk file is used to hold the database and its tables
cursor	= connection.cursor()	# create a cursor to the data
cursor.execute("""CREATE TABLE athletes(
					id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
					name TEXT NOT NULL,
					dob DATE NOT NULL
				)""")
cursor.execute("""CREATE TABLE timing_data(
						athlete_id INTEGER NOT NULL,
						value TEXT NOT NULL,
						FOREIGN KEY (athlete_id) REFERENCES athletes
				)""")
connection.commit()				# commit any changes, making them permanent
connection.close()				# close your connection when you're finished
