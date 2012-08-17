import android
from urllib import urlencode
from urllib2 import urlopen

server_title = 'Which server should I use?'
server_msg = "Please confirm the server address/name to use for your athlete's timing data:"
timing_title = 'Enter data'
timing_msg = 'Provide a new timing value:'
web_server = 'http://9.56.60.157:8000'
add_time_cgi = '/cgi-bin/add_timing_data.py'

app = android.Android()
resp = app.dialogGetInput(server_title, server_msg, web_server).result	# the first dialog ask the user to confirm the web address and port to use

if resp is not None:	# if the user did NOT tap on the Cancel Button...
	web_server = resp
	resp = app.dialogGetInput(timing_title, timing_msg).result	# ...the second dialog ask for a new timing value
	if resp is not None:	# again, if the user did NOT tap on the Cancel button...
		new_time = resp
		send_to_server(web_server + add_time_cgi, {'Timing Value': new_time})	# ...the app sends the data to the web server

#------------------------------------------------------
def send_to_server(url, post_data=None):
	if post_data:
		page = urlopen(url, urlencode(post_data))
	else:
		page = urlopen(url)
	return(page.read().decode("utf8"))
