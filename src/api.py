'''
This handler will manage all the API calls
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models.models import *
from google.appengine.api import users
'''
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
use_library('django', '1.2')
'''

class Auth(webapp.RequestHandler):
    def get(self,username,password):
        self.response.out.write("auth" + self.request.get("username") + self.request.get("password"))
        
class Signup(webapp.RequestHandler):
    def post(self,username,email,password):
        user=User()
        user.username=self.request.get('username')
        user.email=self.request.get('email')
        user.password=self.request.get('password')
        self.response.out.write("sign up complete")

class Stories(webapp.RequestHandler):
    def get(self):
        self.response.out.write("stories")
        
class UserStories(webapp.RequestHandler):
    def get(self,user_id):
        self.response.out.write('a user"s stories')

class CommentOnStory(webapp.RequestHandler):
    def get(self,story_id,comment):
        self.response.out.write('comment')
        
application = webapp.WSGIApplication([('/api/auth/(.*)(.*)',Auth),
                                      ('/api/stories/.*',Stories)],debug=True)
    
def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()

