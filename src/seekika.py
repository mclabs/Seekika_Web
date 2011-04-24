from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
import os
from google.appengine.ext.webapp import template

_DEBUG=True

class BaseHandler(webapp.RequestHandler):
    def generate(self,template_name, template_values=dict()):
        directory = os.path.dirname(__file__)
        path = os.path.join(directory, os.path.join('templates', template_name))
        self.response.out.write(template.render(path, template_values,debug=_DEBUG))

class Index(BaseHandler):
    def get(self):
        template_values={}
        self.generate('index.html',template_values)

class Profile(BaseHandler):
    def get(self):
        template_values={}
        self.response.out.write("user profile")

class UserStories(BaseHandler):
    def get(self,user_id):
        template_values={}
        '''return users stories '''
        self.generate('stories.html',template_values)
        

application = webapp.WSGIApplication([('/',Index)],debug=True)
    
def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()