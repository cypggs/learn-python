#! /usr/local/bin/python3

import sys				# for debugging purposes
import cgi
import json
import athletemodel
import yate
from athletelist import AthleteList

form_data = cgi.FieldStorage()						# process the stat send with the request and extract the ahtlete's name
athlete_id = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_id)
print(yate.start_response('application/json'))		# start a web response, with JSON as the data type
print(json.dumps(athlete))							# include the indicated athlete's data in the web response, formatted by JSON
