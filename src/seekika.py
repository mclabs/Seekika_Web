from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

class BaseHandler(webapp.RequestHandler):
    def render_template(self,template_name, template_values=dict()):
        path = os.path.join(os.path.dirname(__file__), template_name)
        self.response.out.write(template.render(path, template_values))

class Index(BaseHandler):
    def get(self):
        template_values={}
        self.render_template('index.html',template_values)

class Profile(webapp.RequestHandler):
    def get(self):
        self.response.out.write("user profile")


application = webapp.WSGIApplication([('/',Index)],debug=True)
    
def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()