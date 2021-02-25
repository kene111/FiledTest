import json
from tests.BaseCase import BaseCase



class CreateAudioTest(BaseCase):
	def test_successful_create_audio(self):
		payload1 = json.dumps({
    					"audioFileType":"song",
    					"audioFileMetadata": {
    					  "song_id":1,
                          "name_of_song":"rise",
                          "duration_of_song":300}
                          })

		payload2 = json.dumps({
    					"audioFileType":"podcast",
    					"audioFileMetadata": {
    					  "podcast_id":1,
                          "name_of_podcast":"how to grow your income",
                          "duration_of_podcast":3500,
                          "host":"John Mclean",
                          "participants":["Samuel", "Paul", "Mike"]}
                          })

		payload3 = json.dumps({
    					"audioFileType":"podcast",
    					"audioFileMetadata": {
    					  "podcast_id":2,
                          "name_of_podcast":"Life in a day",
                          "duration_of_podcast":1500,
                          "host":"Abel Smith",
                          "participants":[]}
                          })

		payload4 = json.dumps({
    					"audioFileType":"audiobook",
    					"audioFileMetadata": {
    					  "audiobook_id":3,
                          "title_of_audiobook":"Think and Grow Rich",
                          "author_of_audiobook":"Napoleon Hill",
                          "narrator":"Sandra Collins",
                          "duration_of_audiobook":7000}
                          })


		response = self.app.post('/add_audio', headers={"Content-Type": "application/json"}, data=payload1)

		self.assertEqual(str, type("Action is successful 200 OK"))
		self.assertEqual(200, response.status_code)
