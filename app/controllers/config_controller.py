from app.models.config_model import Config
from app.utils import *

def get_config(config_id):
    config = Config.get_by_id(config_id)
    if config:
        return success_response(config)
    else:
        return error_response("Config tidak ada")
