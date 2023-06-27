from flask import Blueprint
from app.controllers.category_controller import *

category_bp = Blueprint('category', __name__, url_prefix='/categorys')

category_bp.route('', methods=['GET'])(get_categorys)
category_bp.route('', methods=['POST'])(create_category)
category_bp.route('/<string:setting_id>', methods=['GET'])(get_category)
category_bp.route('/<string:setting_id>', methods=['PUT'])(update_category)
category_bp.route('/<string:setting_id>', methods=['DELETE'])(delete_category)
category_bp.route('/company/<string:company_id>', methods=['GET'])(get_category_by_id_company)
