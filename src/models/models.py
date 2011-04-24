'''
All my Seekika models will be here
'''
from google.appengine.ext import db

'''User Model'''
class User(db.Model):
    email=db.StringProperty()
    username=db.StringProperty
    password=db.StringProperty()
    created_on=db.DateTimeProperty(auto_now_add=True)

''' Story Model '''    
class Story(db.Model):
    title=db.StringProperty()
    filename = db.StringProperty()
    created_on = db.DateTimeProperty(auto_now_add=True)
    user=db.ReferenceProperty(User,collection_name="story")
    status=db.BooleanProperty()
    
    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])

class StoryCategory(db.Model):
    category=db.StringProperty() 
    
class Comment(db.Model):
    comment=db.StringProperty(multiline=True)
    user=db.UserProperty(required=True)
    story=db.Reference(Story)
    created_on = db.DateTimeProperty(auto_now_add=True)
    
'''Locations Model'''
class Location(db.Model):
    location=db.StringProperty()
    lat=db.StringProperty()
    
    def to_dict(self):
        return dict([(p, unicode(getattr(self, p))) for p in self.properties()])