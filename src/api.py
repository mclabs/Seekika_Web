'''
This handler will manage all the API calls
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models.models import *

class Auth(webapp.RequestHandler):
    def get(self):
        self.response.out.write("auth")

class Stories(webapp.RequestHandler):
    def get(self):
        self.response.out.write("stories")
        
application = webapp.WSGIApplication([('/api/auth/.*',Auth),
                                      ('/api/stories/.*',Stories)],debug=True)
    
def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()

