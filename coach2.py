"""
This function removes '-' and ':' from a string
and replaces it with a '.'
"""
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)
"""
This function reads the data from a file
and returns it as a list structure
"""
def get_coach_data(filename):
	try:
		with open(filename) as fh:
			data = fh.readline()
		templ = data.strip().split(',')
		return({'Name': templ.pop(0),
				'DOB': templ.pop(0),
				'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3])
				})
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)
		
james = get_coach_data('james2.txt')
print(james['Name'] + "'s fastest times are: " + james['Times'])
julie = get_coach_data('julie2.txt')
print(julie['Name'] + "'s fastest times are: " + julie['Times'])
mikey = get_coach_data('mikey2.txt')
print(mikey['Name'] + "'s fastest times are: " + mikey['Times'])
sarah = get_coach_data('sarah2.txt')
print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])
