from .db import db
import mongoengine_goodjson as gj
from datetime import datetime


class Song(gj.Document):
	song_id = db.IntField(required=True, unique=True)
	name_of_song = db.StringField(max_length=100, required=True) 
	duration_of_song = db.IntField(required=True)
	upload_time = db.DateTimeField(default=datetime.now, required=True)


	
class Podcast(gj.Document):
	podcast_id =  db.IntField(required=True, unique=True)
	name_of_podcast = db.StringField(max_length=100, required=True)  
	duration_of_podcast = db.IntField(required=True)
	upload_time = db.DateTimeField(default=datetime.utcnow, required=True)
	host = db.StringField(max_length=100, required=True)
	participants = db.ListField(db.StringField(max_length=100),max_length=10,required=False)

	def __str__(self):
		return self.name_of_podcast



class Audiobook(gj.Document):
	audiobook_id = db.IntField(required=True, unique=True)
	title_of_audiobook = db.StringField(max_length=100, required=True)
	author_of_audiobook = db.StringField(max_length=100, required=True)
	narrator = db.StringField(max_length=100, required=True) 
	duration_of_audiobook = db.IntField(required=True)
	upload_time = db.DateTimeField(default=datetime.utcnow, required=True)


	def __str__(self):
		return self.title_of_audiobook

