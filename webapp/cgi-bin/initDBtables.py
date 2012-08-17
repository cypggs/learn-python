import pickle
import sqlite3
import glob
import athletemodel
from athletelist import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error (get_coach_data): ' + str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))
    return(all_athletes)
#---------------------------------------------------------------------------------------

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

# grab the data from the existing model
data_files = glob.glob("../data/*.txt")
athletes = put_to_store(data_files)

for each_ath in athletes:
	# get the athletes name and dob from the pickled data
	name = athletes[each_ath].name
	dob = athletes[each_ath].dob
	cursor.execute("SELECT id from athletes WHERE name=? AND dob=?", (name, dob))	# query the athletes table for the ID
	the_current_id = cursor.fetchone()[0]				# returns a list
	for each_time in athletes[each_ath].clean_data:
		cursor.execute("INSERT INTO timing_data(athlete_id, value) VALUES (?, ?)", (the_current_id, each_time))

	
connection.commit()	
connection.close()
