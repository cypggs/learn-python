from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms
from google.appengine.api import users	# imports GAE's Google Accounts API
import hfwwgDB		# import your GAE data model code

class SightingForm(djangoforms.ModelForm):
	class Meta:
		model = hfwwgDB.Sighting
		#exclude = ['which_user']	# do not include the user information in the generated form

class SightingInputPage(webapp.RequestHandler):
	def get(self):
		html = template.render('templates/header.html', {'title': 'Report a Possible Sighting'})
		html = html + template.render('templates/form_start.html', {})
		html = html + str(SightingForm())
		html = html + template.render('templates/form_end.html', {'sub_title': 'Submit Sighting'})
		html = html + template.render('templates/footer.html', {'links': ''})
		self.response.out.write(html)
	def post(self):
		new_sighting = hfwwgDB.Sighting()	# create a new Sighting object to hold your data
		new_sighting.name = self.request.get('name')
		new_sighting.email = self.request.get('email')
		new_sighting.date = self.request.get('date')
		new_sighting.time = self.request.get('time')
		new_sighting.location = self.request.get('location')
		new_sighting.fin_type = self.request.get('fin_type')
		new_sighting.whale_type = self.request.get('whale_type')
		new_sighting.blow_type = self.request.get('blow_type')
		new_sighting.wave_type = self.request.get('wave_type')
		#new_sightine.which_user = users.get_current_user()	# this line includes the Google ID of the currently logged-in user
		new_sighting.put()		# store your data in the GAE datastore
		html = template.render('templates/header.html', {'title': 'Thank you!'})
		html = html + "<p>Thank you for providing your sighting data.</p>"
		html = html + template.render('templates/footer.html', {'links': 'Enter <a href="/">another sighting</a>.'})	
		self.response.out.write(html)
		
app = webapp.WSGIApplication([('/.*', SightingInputPage)], debug=True)

def main():
	run_wsgi_app(app)
	
if __name__ == '__main__':
	main()