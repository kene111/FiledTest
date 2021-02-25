# FiledTest


## Solution code to the Filed Python Test

## Repository Breakdown:


### Folders:
1) database folder: This folder contains the  db.py file and the models.py file.
2) resources folder : This folderr contains the an api.py file, error.py file and routes.py file.
3) tests folder: This folder contains the python files used in testing the api endpoints.

### Python files:
1) db.py : This file contains the database initialization code.
2) models.py: This file contains models used in creating the database.
3) api.py: This file contains the classes for each request endpoint.
4) errors.py: This file contains custom code for error handling.
5) routes.py: This file contains the route link for eact class.
6) test_create.py: This file contains the code used in testing the create api.
7) test_delete.py: This file contains the code used in testing the delete api.
8) test_update.py: This file contains the code used in testing the update api.
9) BaseCase.py: This file contains a common code used in all three test files.

### Other Files:
1) .env.test: File used in setting evironment variables for testing api endpoints.

### Tech Stack:
1) Flask
2) MongoDB

### Others technologies used:
PostMan: for testing the api endpoints.

### Note: 
1) Comment out the teardown function in BaseCase.py to test the update and delete api properly.
2) AudioFileType, AudioFileID, and  payloads parameters must be the same accross all test files to properly test the api endpoints
3) Running all test cases at once shows a test score of 2/3 and this is because the delete api is called before the update api.

example:
1) when testing the create api on "song" and its metadata, confirm that data = payload1 in test_create.py 
2) In the test_delete.py confirm that audioFileType is equal to "song" and audioFileID is equal to the same value as song_id in payload1 in test_create.py
3) In the test_update.py confirm that data =  payload1, audioFileType is equal to "song" and audioFileID is equal to the same value as song_id in payload1 in test_create.py
4) confirm to have commented out the teardown function in BaseCase.py

With this, you can create a new song data, update it and delete it.

