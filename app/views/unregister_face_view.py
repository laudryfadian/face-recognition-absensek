from flask import Blueprint
from app.controllers.unregister_face_controller import *

unregister_bp = Blueprint('unregister', __name__, url_prefix='/unregister')

unregister_bp.route('', methods=['GET'])(get_unregs)
unregister_bp.route('', methods=['POST'])(create_unreg)
unregister_bp.route('/<string:unreg_id>', methods=['GET'])(get_unreg)
unregister_bp.route('/<string:unreg_id>', methods=['PUT'])(update_unreg)
unregister_bp.route('/<string:unreg_id>', methods=['DELETE'])(delete_unreg)
unregister_bp.route('/company/<string:company_id>', methods=['GET'])(get_unreg_by_id_company)
unregister_bp.route('/approve/<string:unreg_id>', methods=['GET'])(approve_face)
