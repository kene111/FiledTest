import json
from tests.BaseCase import BaseCase



class CreateAudioTest(BaseCase):
	def test_successful_delete_audio(self):

		audioFileType = 'song'
		audioFileID = 1



		response = self.app.delete(f'/delete_audio/{audioFileType}/{audioFileID}', headers={"Content-Type": "application/json"})

		self.assertEqual(str, type("Action is successful: 200 OK"))
		self.assertEqual(200, response.status_code)
