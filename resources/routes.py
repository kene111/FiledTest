from .api import AudioCreate,AudioGet,AudioDelete,AudioUpdate

def initialize_routes(api):
 api.add_resource(AudioCreate, '/add_audio')
 api.add_resource(AudioGet, '/get_audio/<audioFileType>/<audioFileID>')
 api.add_resource(AudioDelete, '/delete_audio/<audioFileType>/<audioFileID>')
 api.add_resource(AudioUpdate, '/update_audio/<audioFileType>/<audioFileID>')