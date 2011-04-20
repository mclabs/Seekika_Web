'''
All my Seekika models will be here
'''
from google.appengine.ext import db

'''User Model'''
class User(db.Model):
    first_name=db.StringProperty()

''' Story Model '''    
class Story(db.Model):
    title=db.StringProperty()
    filename = db.StringProperty()
    created_on = db.DateTimeProperty(auto_now_add=True)
    user=db.ReferenceProperty(User,collection_name="story")
    status=db.BooleanProperty()
    
    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])
    
'''Locations Model'''
class Location(db.Model):
    location=db.StringProperty()
    
    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])