from flask import Blueprint
from app.controllers.config_controller import *

config_bp = Blueprint('config', __name__, url_prefix='/config')

config_bp.route('/<string:config_id>', methods=['GET'])(get_config)
