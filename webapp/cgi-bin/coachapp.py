import android, json, time		#  time is for web-client functionality
from urllib import urlencode	#  for web-client functionality
from urllib2 import urlopen		#  for web-client functionality
#-----------------------------------------------------
def status_update(msg, how_long=2):
	app.makeToast(msg)
	time.sleep(how_long)
#-----------------------------------------------------
def send_to_server(url, post_data=None):
	if post_data:
		page = urlopen(url, urlencode(post_data))
	else:
		page = urlopen(url)
	return(page.read().decode("utf8"))
#-----------------------------------------------------
hello_msg = "Welcome to NUAC's Timing App"
list_title = 'Here is your list of athletes:'
quit_msg = "Quittin NUAC's App."
web_server = "http://192.168.1.6:8000"
get_names_cgi = '/cgi-bin/generate_names.py'	# CGI script to run on the web server
get_data_cgi = '/cgi-bin/generate_data.py'		# CGI script to run on the web server

app = android.Android()

status_update(hello_msg)
athletes = sorted(json.loads(send_to_server(web_server + get_names_cgi)))
athlete_names = [ath[0] for ath in athletes]
app.dialogCreateAlert(list_title)
app.dialogSetSingleChoiceItems(athlete_names)
app.dialogSetPositiveButtonText('Select')
app.dialogSetNegativeButtonText('Quit')
app.dialogShow()

resp = app.dialogGetResponse().result
if resp['which'] in  ('positive'):
	selected_athlete = app.dialogGetSelectedItems().result[0]	# the index values is in the first element of the list of results returned from the dialog
	which_athlete = athletes[selected_athlete][1]				# look up the athlete's name using the index value
	athlete = json.loads(send_to_server(web_server + get_data_cgi, {'which_athlete': which_athlete}))	# send a new web request to the server to fetch the athlete's data
	athlete_title = athlete['Name'] + ' (' + athlete['DOB'] + '), top 3 times:'		# dynamically create the dialog's title
	app.dialogCreateAlert(athlete_title)							# the user needs to see only the data this time, so you need to use "dialogSetItem()"
	app.dialogSetItems(athlete['top3'])						
	app.dialogSetPositiveButtonText('OK')
	app.dialogSetNegativeButtonText('Add Time')
	app.dialogShow()
	resp = app.dialogGetResponse().result				# wait for a tap from the user
	
	if resp['which'] in  ('positive'):
		pass
	elif resp['which'] in  ('negative'):
		timing_title = 'Enter a new time'
		timing_msg = 'Provide a new timing value ' + athlete['Name'] + ': '
		add_time_cgi = '/cgi-bin/add_timing_data.py'
		resp = app.dialogGetInput(timing_title, timing_msg).result
		if resp is not None:
			new_time = resp
			send_to_server(web_server + add_time_cgi, {'Time': new_time, 'Athlete': which_athlete})

status_update(quit_msg)
