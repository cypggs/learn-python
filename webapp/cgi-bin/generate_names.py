#! /usr/local/bin/python3

import json
import athletemodel
import yate

names = athletemodel.get_namesID_from_store()

print(yate.start_response('application/json'))	# start with the appropriate "Content-type" line
print(json.dumps(sorted(names)))				# sort "names", then convert to JSON and send to STDOUT
