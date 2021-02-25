import json
from tests.BaseCase import BaseCase



class CreateAudioTest(BaseCase):
	def test_successful_create_audio(self):

		audioFileType = 'song'
		audioFileID = 1

		payload1 = json.dumps({
                          "name_of_song":"fall",
                          "duration_of_song":300}
                          )

		payload2 = json.dumps({
                          "name_of_podcast":"how to grow your income",
                          "duration_of_podcast":350,
                          "host":"John Mclean",
                          "participants":["Samuel", "Paul", "John"]}
                          )

		payload3 = json.dumps({
                          "name_of_podcast":"Life in a day II",
                          "duration_of_podcast":150,
                          "host":"Abel Smith",
                          "participants":["Sam", "John"]}
                          )

		payload4 = json.dumps({
                          "title_of_audiobook":"Think and Grow Rich",
                          "author_of_audiobook":"Napoleon Hill",
                          "narrator":"Kate Collins",
                          "duration_of_audiobook":600}
                          )

		response = self.app.put(f'/update_audio/{audioFileType}/{audioFileID}', headers={"Content-Type": "application/json"}, data=payload1)

		self.assertEqual(str, type("Action is successful: 200 OK"))
		self.assertEqual(200, response.status_code)
