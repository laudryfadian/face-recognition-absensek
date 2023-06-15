from flask import Blueprint
from app.controllers.setting_controller import *

setting_bp = Blueprint('setting', __name__, url_prefix='/settings')

setting_bp.route('', methods=['GET'])(get_settings)
setting_bp.route('', methods=['POST'])(create_setting)
setting_bp.route('/<string:setting_id>', methods=['GET'])(get_setting)
setting_bp.route('/<string:setting_id>', methods=['PUT'])(update_setting)
setting_bp.route('/<string:setting_id>', methods=['DELETE'])(delete_setting)
