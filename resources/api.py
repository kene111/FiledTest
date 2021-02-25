from flask import request, Response
from database.models import Song, Podcast, Audiobook
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist,NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError,AudioFileAlreadyExistsError, InternalServerError, UpdatingAudioFileError, DeletingAudioFileError, AudioFileNotExistsError


class AudioCreate(Resource):
	def post(self):
		data = request.get_json()
		audio_type = data['audioFileType']
		audio_data =  data['audioFileMetadata']

		try:

			if audio_type == 'song' and audio_data['duration_of_song'] > 0:
				song = Song(song_id=audio_data['song_id'], name_of_song=audio_data['name_of_song'], duration_of_song=audio_data['duration_of_song']).save()

				return Response("Action is successful: 200 OK", status=200)

			elif audio_type == 'podcast' and audio_data['duration_of_podcast'] > 0:

				podcast =  Podcast(podcast_id=audio_data['podcast_id'], name_of_podcast=audio_data['name_of_podcast'], duration_of_podcast=audio_data['duration_of_podcast'], host=audio_data['host'], participants=audio_data['participants']).save()
				return Response("Action is successful: 200 OK", status=200)

			elif audio_type == 'audiobook' and audio_data['duration_of_audiobook'] > 0:
				audiobook =  Audiobook(audiobook_id=audio_data['audiobook_id'], title_of_audiobook=audio_data['title_of_audiobook'], author_of_audiobook=audio_data['author_of_audiobook'], narrator=audio_data['narrator'], duration_of_audiobook=audio_data['duration_of_audiobook']).save()
				return Response("Action is successful: 200 OK", status=200)

			else: 
				return Response("This request is invalid: 400 Bad Request", status=400)

		except (FieldDoesNotExist, ValidationError):
			

			raise SchemaValidationError

		except NotUniqueError:

			raise AudioFileAlreadyExistsError

		except Exception as e:
			raise InternalServerError
			

class AudioGet(Resource):
	def get(self,audioFileType,audioFileID):


		try: 
			if audioFileType == 'song':

				song = Song.objects.get(song_id=audioFileID).to_json()
				return Response(song,mimetype="application/json", status=200)


			elif audioFileType == 'podcast':
				podcast = Podcast.objects.get(podcast_id=audioFileID).to_json()
				return Response(podcast,mimetype="application/json", status=200)
				

			elif audioFileType == 'audiobook':
				audiobook = Audiobook.objects.get(audiobook_id=audioFileID).to_json()
				return Response(audiobook,mimetype="application/json", status=200)

		except DoesNotExist:
			raise AudioFileNotExistsError

		except Exception:
			raise InternalServerError

class AudioDelete(Resource):
	def delete(self, audioFileType,audioFileID):

		try: 

			if audioFileType == 'song':
				song = Song.objects.get(song_id=audioFileID).delete()
				return Response("Action is successful: 200 OK", status=200)


			elif audioFileType == 'podcast':
				podcast = Podcast.objects.get(podcast_id=audioFileID).delete()
				return Response("Action is successful: 200 OK", status=200)
				

			elif audioFileType == 'audiobook':
				audiobook = Audiobook.objects.get(audiobook_id=audioFileID).delete()
				return Response("Action is successful: 200 OK", status=200)

		except DoesNotExist:

			raise DeletingAudioFileError

		except Exception as e:
			raise InternalServerError



class AudioUpdate(Resource):
	def put(self, audioFileType,audioFileID):

		data = request.get_json()

		try:

			if audioFileType == 'song' and data['duration_of_song'] > 0:
				song = Song.objects.get(song_id=audioFileID).update(song_id=audioFileID, name_of_song=data['name_of_song'], duration_of_song=data['duration_of_song'])
				return Response("Action is successful: 200 OK", status=200)


			elif audioFileType == 'podcast' and data['duration_of_podcast'] > 0:
				podcast = Podcast.objects.get(podcast_id=audioFileID).update(podcast_id=audioFileID, name_of_podcast=data['name_of_podcast'], duration_of_podcast=data['duration_of_podcast'], host=data['host'], participants=data['participants'])
				return Response("Action is successful: 200 OK", status=200)
				

			elif audioFileType == 'audiobook' and data['duration_of_audiobook'] > 0:
				audiobook = Audiobook.objects.get(audiobook_id=audioFileID).update(audiobook_id=audioFileID, title_of_audiobook=data['title_of_audiobook'], author_of_audiobook=data['author_of_audiobook'], narrator=data['narrator'], duration_of_audiobook=data['duration_of_audiobook'])
				return Response("Action is successful: 200 OK", status=200)

			else:

				return Response("This request is invalid: 400 Bad Request", status=400)


		except InvalidQueryError:

			raise SchemaValidationError

		except DoesNotExist:

			raise UpdatingAudioFileError

		except Exception as e:
			raise InternalServerError 


