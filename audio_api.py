from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors



app = Flask(__name__)
api = Api(app, errors=errors)

app.config.from_envvar('ENV_FILE_LOCATION')

#app.config['MONGODB_SETTINGS'] = {
#    'host': 'mongodb://localhost/audiodb'
#}


initialize_db(app)
initialize_routes(api)



if __name__ == '__main__':
	app.run(debug=False) 

# set FLASK_APP=audio_api.py
#set ENV_FILE_LOCATION=./.env