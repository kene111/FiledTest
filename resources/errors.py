from werkzeug.exceptions import HTTPException

class InternalServerError(HTTPException):
    pass

class SchemaValidationError(HTTPException):
    pass

class AudioFileAlreadyExistsError(HTTPException):
    pass

class UpdatingAudioFileError(HTTPException):
    pass

class DeletingAudioFileError(HTTPException):
    pass

class AudioFileNotExistsError(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "Something went wrong": "500 InternalServerError"
    },
     "SchemaValidationError": {
         "The request is invalid": "400 Bad Request"
     },
     "AudioFileAlreadyExistsError": {
         "The request is invalid": "400 Bad Request"
     },
     "UpdatingAudioFileError": {
         "The request is invalid": "400 Bad Request"
     },
     "DeletingAudioFileError": {
         "The request is invalid": "400 Bad Request"
     },
     "AudioFileNotExistsError": {
         "The request is invalid": "400 Bad Request"
     }
}