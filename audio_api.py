import os
from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


api = Api(app, errors=errors)

#used for development
#app.config.from_envvar('ENV_FILE_LOCATION')


MONGODB_URI = os.environ.get('MONGODB_URI')

app.config['MONGODB_SETTINGS'] = {
    'host': MONGODB_URI
}


initialize_db(app)
initialize_routes(api)



if __name__ == '__main__':
	app.run(debug=False) 

# set FLASK_APP=audio_api.py
#set ENV_FILE_LOCATION=./.env